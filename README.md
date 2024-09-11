# Running-LLM-Ollama-Local-GPU-Estimation
This guide provides instructions for setting up and running the LLM-Ollama application locally with Docker, along with estimating GPU requirements. It includes steps for installing Docker, setting up the Ollama Docker image, and running the application.

**Installation Instructions**

**Prerequisites**

  - **Linux-based operating system**
  - **Docker installed**
  - **NVIDIA GPU with appropriate drivers (for GPU estimation)**

---

Installing Docker (if not installed)

If Docker is not installed on your system, follow these steps:
- **How to Install 🚀**
  # Update package index
      sudo apt-get update
      
  # Install packages to allow apt to use a repository over HTTPS
      sudo apt-get install \
          apt-transport-https \
          ca-certificates \
          curl \
          gnupg \
          lsb-release
      
  # Add Docker’s official GPG key
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
      
  # Set up the stable repository
      echo \
        "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
      
  # Install Docker Engine
      sudo apt-get update
      sudo apt-get install docker-ce docker-ce-cli containerd.io
---

  Start with Docker 🐳
  
  Setting up LLM-Ollama Docker Image

  - **Pull the Ollama Docker image**:
    
        docker pull ollama/ollama

 - **Run the Ollama container with GPU support**:

       docker run -d --gpus=all -v /home/player/karna:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

-  **Verify container status**:

    docker ps

- **Access the container for model installation**:

      docker exec -it ollama /bin/bash

- **Inside the container**, install the desired model (e.g., Llama3.1):

    ollama model download llama3.1

Running the Application

  - **Clone the LLM repository** and navigate to the application directory:

        git clone <repository_url>
        cd <repository_directory>

- **Start the backend**:

      python3 app.py

- **For the frontend (assuming it’s a Svelte Kit application named my-llm-chat)**:

      cd my-llm-chat
      npm install
      npm run dev
  
---

Running Open WebUI (Optional)

  - **Clone the Open WebUI repository**:

        git clone https://github.com/open-webui/open-webui.git

- **Run Open WebUI in a Docker container**:

      docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

    Access Open WebUI at http://localhost:3000 in your browser.
---

Additional Notes

  For GPU estimation, refer to the GPU Estimation document here.
    Ensure Docker and NVIDIA GPU drivers are compatible for optimal performance.

This README structure covers installation, setup, and running instructions for your LLM-Ollama application, along with optional steps for integrating Open WebUI. Adjust paths and specific commands as per your setup.

---

License 📜
This project is licensed under the MIT License. See the LICENSE file for details.
---
Made with ❤️ by T.Gouri Sankar

