# 🤖 P018: Markdown Project Planning Agent

## 📖 Description
This project demonstrates how to enforce strict output formatting from a Local Large Language Model (LLM) using Ollama. The script takes a high-level project goal from the user and instructs the LLM to act as an expert Project Manager, generating a structured, step-by-step project plan outputted *specifically in Markdown format*.

## ✨ Key Features/Constraints
* **Local LLM Integration:** Uses Ollama/local models (e.g., Llama 3) for privacy and resource control.
* **Structured Output Control:** Enforces specific Markdown formatting (Headings, Bolding, Bullet Points) for the entire plan.
* **Project Management Persona:** Assigns a strict role to the model to enhance response quality.

## 🛠️ Technology Stack
* **Language:** Python
* **Local LLM:** Ollama (requires an installed model like `llama3`)
* **Libraries:** `ollama`

## ⚙️ Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone [Your-Repo-URL]
    cd P018_Project_Planning_Agent
    ```
2.  **Create and activate the virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Ensure Ollama is running and a model is pulled:**
    ```bash
    # Example: Pulling a model if you don't have one
    ollama pull llama3
    ```
5.  **Run the script:**
    ```bash
    python planner_agent.py
    ```

## ✍️ Author
**Author:** mmainomad-ship-it
**GitHub:** https://github.com/mmainomad-ship-it