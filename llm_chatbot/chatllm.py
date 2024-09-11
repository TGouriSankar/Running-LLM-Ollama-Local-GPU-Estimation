import requests
import json

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
                # Try to parse each chunk as JSON
                try:
                    json_chunk = json.loads(chunk.strip())
                    partial_response = json_chunk.get("response", "")
                    full_response += partial_response
                    
                    # Print the partial response directly as it arrives
                    print(partial_response, end="", flush=True)

                except json.JSONDecodeError:
                    # If it's not a complete JSON chunk, continue
                    continue

        # Return the full concatenated response once the streaming is done
        return full_response if full_response else "No response received from the LLM."

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

def chat_with_llm():
    while True:
        # Ask for user input
        prompt = input("You: ")

        if prompt.lower() in ['exit', 'quit', 'stop']:
            print("Exiting chat.")
            break

        # Query the LLM API and get the response
        response = query_llm(prompt)
        
        # If a response was printed in parts, this will just add the final newline.
        print("\nLLM: (complete)")

if __name__ == "__main__":
    chat_with_llm()


# curl -X POST http://127.0.0.1:11434/api/generate \
# > -H "Content-Type: application/json" \
# > -d '{"model": "llama3.1", "prompt": "Hello, LLM!"}'