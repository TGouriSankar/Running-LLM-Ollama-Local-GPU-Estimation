from flask import Flask, request, Response
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to query the LLM model with a prompt
def query_llm(prompt):
    url = "http://127.0.0.1:11434/api/generate"  # The LLM API endpoint
    headers = {"Content-Type": "application/json"}
    data = {"model": "llama3.1", "prompt": prompt}

    try:
        # Make a POST request to the LLM API and stream the response
        response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        # Initialize the full response to concatenate
        for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
            if chunk:
                # Try to parse each chunk as JSON
                try:
                    json_chunk = json.loads(chunk.strip())
                    partial_response = json_chunk.get("response", "")
                    yield partial_response + "\n"  # Send partial response as a stream

                except json.JSONDecodeError:
                    continue  # If it's not a valid JSON chunk, continue processing

    except requests.exceptions.RequestException as e:
        yield f"Request error: {e}\n"

# Flask route to handle the chat API
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')

    # Call the LLM model and stream the response
    return Response(query_llm(prompt), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import requests
# import json

# app = Flask(__name__)
# CORS(app)

# @app.route('/api/chat', methods=['POST'])
# def chat():
#     data = request.json
#     prompt = data.get("prompt", "")

#     url = "http://127.0.0.1:11434/api/generate"
#     headers = {"Content-Type": "application/json"}
#     request_data = {"model": "llama3.1", "prompt": prompt}

#     try:
#         response = requests.post(url, headers=headers, data=json.dumps(request_data), stream=True)
#         response.raise_for_status()

#         full_response = ""
#         for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
#             if chunk:
#                 try:
#                     json_chunk = json.loads(chunk.strip())
#                     partial_response = json_chunk.get("response", "")
#                     full_response += partial_response
#                 except json.JSONDecodeError:
#                     continue

#         return jsonify({"response": full_response if full_response else "No response received from the LLM."})

#     except requests.exceptions.RequestException as e:
#         return jsonify({"response": f"Request error: {e}"}), 500

# if __name__ == "__main__":
#     app.run(port=5000)
