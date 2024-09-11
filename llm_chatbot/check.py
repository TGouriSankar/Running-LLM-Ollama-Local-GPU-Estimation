import json

# Sample response data
response_data = [
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:38.392394866Z", "response": "It", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:38.611680928Z", "response": "'s", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:38.832712116Z", "response": " nice", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:39.051949838Z", "response": " to", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:39.27532174Z", "response": " meet", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:39.49713464Z", "response": " you", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:39.716652016Z", "response": ".", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:39.935551626Z", "response": " Is", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:40.156252168Z", "response": " there", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:40.378204813Z", "response": " something", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:40.598683969Z", "response": " I", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:40.819409602Z", "response": " can", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:41.037801678Z", "response": " help", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:41.256937992Z", "response": " you", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:41.476880346Z", "response": " with", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:41.695857106Z", "response": " or", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:41.91619781Z", "response": " would", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:42.137463107Z", "response": " you", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:42.360193485Z", "response": " like", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:42.575692997Z", "response": " to", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:42.78998725Z", "response": " chat", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:43.010336113Z", "response": "?", "done": False},
    {"model": "llama3.1", "created_at": "2024-09-09T11:31:43.231582174Z", "response": "", "done": True, "done_reason": "stop", "context": [128009, 128006, 882, 128007, 271, 9906, 11, 445, 11237, 0, 128009, 128006, 78191, 128007, 271, 2181, 596, 6555, 311, 3449, 499, 13, 2209, 1070, 2555, 358, 649, 1520, 499, 449, 477, 1053, 499, 1093, 311, 6369, 30], "total_duration": 5754821836, "load_duration": 14017060, "prompt_eval_count": 16, "prompt_eval_duration": 857904000, "eval_count": 23, "eval_duration": 4839149000}
]

# Extract and concatenate the responses
response_text = ''.join(item['response'] for item in response_data)

# Print the complete response text
print(response_text)
