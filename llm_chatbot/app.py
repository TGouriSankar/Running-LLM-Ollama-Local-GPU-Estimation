from flask import Flask, request, jsonify, send_from_directory, Response
import requests
from flask_cors import CORS
import json

app = Flask(__name__, static_folder='frontend')
CORS(app)  # Enable CORS to allow communication between frontend and backend

def query_llm_stream(prompt):
    url = "http://127.0.0.1:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {"model": "llama3.1", "prompt": prompt}

    try:
        # Make a POST request to the LLM API
        response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        # Process each chunk of the response (assuming the response is sent in chunks)
        for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
            if chunk:
                # Try to parse each chunk as JSON
                try:
                    json_chunk = json.loads(chunk.strip())
                    partial_response = json_chunk.get("response", "")
                    if partial_response:
                        yield f"data: {partial_response}\n\n"
                except json.JSONDecodeError:
                    continue
        yield "data: [DONE]\n\n"

    except requests.exceptions.RequestException as e:
        yield f"data: Error: {e}\n\n"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("prompt")
    if not user_input:
        return jsonify({"error": "No prompt provided"}), 400
    
    # Use Flask's Response to stream data using generator
    return Response(query_llm_stream(user_input), mimetype='text/event-stream')

# Serve the static HTML file
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




# from flask import Flask, request, jsonify, send_from_directory
# import requests
# from flask_cors import CORS

# app = Flask(__name__, static_folder='frontend')
# CORS(app)  # Enable CORS to allow communication between frontend and backend

# # Function to send prompt to the LLM model
# def query_llm(prompt):
#     url = "http://127.0.0.1:11434/api/generate"
#     headers = {"Content-Type": "application/json"}
#     data = {"model": "llama3.1", "prompt": prompt}
#     response = requests.post(url, json=data)
    
#     try:
#         # Try to parse the JSON response
#         return response.json()
#     except requests.exceptions.JSONDecodeError:
#         # Print the raw response for debugging
#         print(f"Invalid JSON response: {response.text}")
#         return {"error": "Invalid response from LLM service"}

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get("prompt")
#     if not user_input:
#         return jsonify({"error": "No prompt provided"}), 400
    
#     # Send the prompt to LLM and return the response
#     llm_response = query_llm(user_input)
    
#     # Extract the response or return an error message
#     if 'error' in llm_response:
#         return jsonify({"response": llm_response['error']})
#     return jsonify({"response": llm_response.get("response", "No response")})

# # Serve the static HTML file
# @app.route('/')
# def serve_frontend():
#     return send_from_directory(app.static_folder, 'index.html')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
