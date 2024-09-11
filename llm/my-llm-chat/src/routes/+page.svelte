<script>
    let userInput = ""; // User's current input
    let chatHistory = []; // Array to hold the entire chat history (user + LLM)

    let isLoading = false; // To indicate when a response is being fetched

    // Function to handle sending a prompt to the backend
    const sendPrompt = async () => {
        if (userInput.trim() === "") return; // Skip empty inputs

        // Append user's message to the chat history
        chatHistory = [...chatHistory, { type: "user", text: userInput }];

        isLoading = true; // Set loading state

        let fullResponse = "";

        try {
            // Sending user input to the backend
            const response = await fetch('http://127.0.0.1:5000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: userInput })
            });

            // Reading streamed response
            const reader = response.body.getReader();
            const decoder = new TextDecoder();

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                
                // Decoding streamed chunks
                fullResponse += decoder.decode(value, { stream: true });
                
                // Updating chat history with LLM response as it arrives
                chatHistory = [...chatHistory.slice(0, -1), { type: "llm", text: fullResponse }];
            }

        } catch (error) {
            console.error("Error while sending the prompt:", error);
        } finally {
            // Reset user input and clear loading state
            userInput = "";
            isLoading = false;
        }
    };
</script>

<style>
    .chat-container {
        max-width: 600px;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        background-color: #f9f9f9;
    }

    .chat-message {
        margin-bottom: 15px;
        padding: 10px;
        border-radius: 5px;
        max-width: 80%;
        word-wrap: break-word;
    }

    .user-message {
        background-color: #dcf8c6;
        align-self: flex-end;
    }

    .llm-message {
        background-color: #f1f0f0;
        align-self: flex-start;
    }

    .input-container {
        display: flex;
        margin-top: 20px;
    }

    .input-container input {
        flex: 1;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }

    .input-container button {
        padding: 10px 15px;
        margin-left: 10px;
        border: none;
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        cursor: pointer;
    }

    .loading {
        font-style: italic;
    }
</style>

<div class="chat-container">
    <div class="chat-box">
        <!-- Displaying chat history -->
        {#each chatHistory as message (message.text)}
            <div class="chat-message {message.type === 'user' ? 'user-message' : 'llm-message'}">
                {message.text}
            </div>
        {/each}

        <!-- Loading state -->
        {#if isLoading}
            <div class="chat-message llm-message loading">
                LLM is typing...
            </div>
        {/if}
    </div>

    <!-- Input area -->
    <div class="input-container">
        <input
            type="text"
            bind:value={userInput}
            placeholder="Type your message here"
            on:keydown={(e) => e.key === 'Enter' && sendPrompt()} />
        <button on:click={sendPrompt}>Send</button>
    </div>
</div>




<!-- <script>
    import { onMount } from 'svelte';
    import axios from 'axios';
    
    let prompt = ''; // The current input from the user
    let chatHistory = []; // Array to store the conversation history
    let loading = false; // Loading state to show spinner during response fetch

    // Function to send a prompt to the backend and update chat history
    async function sendPrompt() {
        if (!prompt.trim()) return; // Don't send empty prompts
        
        // Add user input to chat history
        chatHistory = [...chatHistory, { role: 'user', content: prompt }];
        
        // Clear the input field
        const userPrompt = prompt;
        prompt = '';
        loading = true;

        try {
            // Send the request to Flask backend
            const res = await axios.post('http://127.0.0.1:5000/api/chat', { prompt: userPrompt });

            // Append the LLM response to the chat history
            chatHistory = [...chatHistory, { role: 'assistant', content: res.data.response }];
        } catch (error) {
            chatHistory = [...chatHistory, { role: 'assistant', content: 'Error: Failed to fetch response' }];
        }

        loading = false;
    }

    // Function to handle the Enter key press
    function handleKeyPress(event) {
        if (event.key === 'Enter' && !loading) {
            sendPrompt();
        }
    }
</script>

<style>
    /* Basic chat UI styling */
    .chat-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f5f5f5;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    .message {
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
    }

    .user-message {
        background-color: #dcf8c6;
        text-align: right;
    }

    .assistant-message {
        background-color: #fff;
        text-align: left;
    }

    .input-container {
        display: flex;
        margin-top: 20px;
    }

    input {
        flex: 1;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
        outline: none;
        margin-right: 10px;
    }

    button {
        padding: 10px 15px;
        border: none;
        border-radius: 8px;
        background-color: #007bff;
        color: white;
        cursor: pointer;
    }

    button:disabled {
        background-color: #ccc;
    }

    .loading {
        text-align: center;
        margin-top: 10px;
        font-style: italic;
    }
</style>

<div class="chat-container">
    {#each chatHistory as message (message.content)}
        <div class="message {message.role === 'user' ? 'user-message' : 'assistant-message'}">
            {message.content}
        </div>
    {/each}

    {#if loading}
        <div class="loading">Thinking...</div>
    {/if}

    Input section -->
    <!-- <div class="input-container">
        <input
            type="text"
            bind:value={prompt}
            placeholder="Enter your prompt..."
            on:keypress={handleKeyPress}
            disabled={loading}
        />
        <button on:click={sendPrompt} disabled={loading || !prompt.trim()}>Send</button>
    </div>
</div> -->



<!-- <script>
    import { onMount } from 'svelte';
    import axios from 'axios';
    
    let prompt = "";
    let response = "";
    let loading = false;

    const sendPrompt = async () => {
        loading = true;
        try {
            const res = await axios.post('http://127.0.0.1:5000/api/chat', { prompt });
            response = res.data.response;
        } catch (error) {
            response = "Error occurred: " + "error.message";
        }
        loading = false;
    };
</script>

<main>
    <h1>Chat with LLM</h1>
    <textarea bind:value={prompt} placeholder="Enter your message" rows="4" cols="50"></textarea>
    <button on:click={sendPrompt} disabled={loading}>Send</button>
    {#if loading}
        <p>Loading...</p>
    {/if}
    <div>
        <h2>Response:</h2>
        <pre>{response}</pre>
    </div>
</main>

<style>
    main {
        padding: 1em;
        max-width: 800px;
        margin: 0 auto;
    }

    textarea {
        width: 100%;
        margin-bottom: 1em;
    }

    button {
        margin-bottom: 1em;
    }

    pre {
        white-space: pre-wrap;
        word-wrap: break-word;
    }
</style> -->
