import requests
import json
import gradio as gr

# Function to query the LLM model (same as before)
def query_llm(prompt):
    url = "http://127.0.0.1:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {"model": "llama3.1", "prompt": prompt}

    try:
        # Make a POST request to the LLM API
        response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        # Initialize the full response to concatenate
        full_response = ""

        # Process each chunk of the response (assuming the response is sent in chunks)
        for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
            if chunk:
                try:
                    json_chunk = json.loads(chunk.strip())
                    partial_response = json_chunk.get("response", "")
                    full_response += partial_response

                except json.JSONDecodeError:
                    continue

        return full_response if full_response else "No response received from the LLM."

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

# Gradio chat interface logic
def chat_with_llm_gradio(prompt):
    response = query_llm(prompt)
    return response

# Create Gradio Interface
iface = gr.Interface(fn=chat_with_llm_gradio, 
                     inputs=gr.Textbox(label="Enter your prompt"), 
                     outputs=gr.Textbox(label="LLM Response"),
                     title="Chat with LLM",
                     description="Enter your prompt and interact with the LLM in real-time.")

# Launch the UI
iface.launch()
