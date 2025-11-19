# STEP 1: Import the Ollama client library
import ollama

# STEP 2: Define the model name to be used by the Ollama client,define the explicit host URL for the Ollama server
MODEL_NAME = "llama3"
OLLAMA_HOST = "http://localhost:11434"
# STEP 3: Prompt the user to enter their project goal
project_goal = input(
    "Enter a project goal to plan (e.g., 'Plan a marketing campaign for a new coffee shop'): "
)
# STEP 4: Print a confirmation message
print(f"\n--- Planning Project: '{project_goal}' ---")
# STEP 5: Define the SYSTEM_PROMPT to set the LLM's persona and formatting rules
SYSTEM_PROMPT = (
    "You are an expert Project Manager. Your sole task is to generate a project "
    "plan based on the user's goal. You must use **Markdown formatting** "
    "including **headings (##)**, **bolding (**), and **bullet points (-)**. "
    "Do not include any introductory or concluding conversation."
)


# STEP 6: Define the main function header that will execute the planning logic
def generate_project_plan(goal: str):
    # STEP 7: Construct the detailed USER_PROMPT using the input goal and strict structural requirements
    USER_PROMPT = (
        "Using the provided format constraints, create a project plan for the goal: "
        f"'{goal}'. The plan must contain exactly **5 main phases**, "
        "each with 3 key action items. Include a final 'Timeline Estimate' section."
    )
    # STEP 8: Initialize the Ollama client
    client = ollama.Client(host=OLLAMA_HOST)
    # STEP 9: Call the LLM using the configured model and combined prompts
    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT},
        ],
    )
    # STEP 10: Extract and return the generated text content from the response
    return response["message"]["content"]


# STEP 11 (Modified): Define the main execution block with error handling
if __name__ == "__main__":
    try:
        # STEP 12 (Modified): Call the function with the gathered input goal
        markdown_plan = generate_project_plan(project_goal)
        # STEP 13 (Modified): Print the result with clear separation, labeling it as Markdown output
        print("\n=======================================================")
        print("📋 Project Plan Generated (Markdown Format):")
        print("=======================================================")
        print(markdown_plan)
    except Exception as e:
        # STEP 14: Print any error that occurs during the API call
        print("\n❌ An error occurred during LLM communication:")
        print(f"Error: {e}")
        print("--- Check that Ollama is running and the model is pulled. ---")
