# planner_agent.py

# STEP 1: Import the necessary libraries.
# 'ollama' is for communicating with the local LLM.
# 'datetime' is for getting the current timestamp for logging.
import ollama
import datetime

# --- Configuration (STEP 2) ---

# Define the model name used by the Ollama client.
MODEL_NAME = "llama3"
# Define the explicit host URL for robust connection (best practice).
OLLAMA_HOST = "http://localhost:11434"
# Define the file name where the project plans will be logged.
LOG_FILE = "project_plans.txt"

# STEP 3: Prompt the user to enter their project goal
project_goal = input(
    "Enter a project goal to plan (e.g., 'Plan a marketing campaign for a new coffee shop'): "
)

# STEP 4: Print a confirmation message
print(f"\n--- Planning Project: '{project_goal}' ---")

# STEP 5: Define the SYSTEM_PROMPT to set the LLM's persona and formatting rules.
# This strictly enforces Markdown output and the expert role.
SYSTEM_PROMPT = (
    "You are an expert Project Manager. Your sole task is to generate a project "
    "plan based on the user's goal. You must use **Markdown formatting** "
    "including **headings (##)**, **bolding (**), and **bullet points (-)**. "
    "Do not include any introductory or concluding conversation."
)

# --- Function Definitions ---


# STEP 6: Define the main function that handles LLM communication
def generate_project_plan(goal: str):
    # STEP 7: Construct the detailed USER_PROMPT using the input goal and strict structural requirements
    USER_PROMPT = (
        "Using the provided format constraints, create a project plan for the goal: "
        f"'{goal}'. The plan must contain exactly **5 main phases**, "
        "each with 3 key action items. Include a final 'Timeline Estimate' section."
    )
    # STEP 8: Initialize the Ollama client using the explicit host URL
    client = ollama.Client(host=OLLAMA_HOST)
    # STEP 9: Call the LLM using the configured model and combined system/user prompts
    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT},
        ],
    )
    # STEP 10: Extract and return the generated text content from the response
    return response["message"]["content"]


# STEP 11: Define a function to save the request and response to a log file
def save_plan_to_file(goal: str, plan: str):
    # STEP 11.1: Open the log file in append mode ('a')
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        # STEP 11.2: Write a clear separator and the project goal
        f.write("\n" + "=" * 80 + "\n")
        f.write(f"PROJECT GOAL: {goal}\n")

        # Get the current time for the log entry
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"GENERATION DATE: {current_time}\n")

        f.write("--- PROJECT PLAN (MARKDOWN) ---\n")
        # STEP 11.3: Write the generated Markdown plan
        f.write(plan)
        f.write("\n" + "=" * 80 + "\n")


# --- Main Execution Block ---

# STEP 12: Define the main execution block with error handling
if __name__ == "__main__":
    try:
        # STEP 13: Call the function with the gathered input goal
        markdown_plan = generate_project_plan(project_goal)
        # STEP 14: Print the result with clear separation
        print("\n=======================================================")
        print("📋 Project Plan Generated (Markdown Format):")
        print("=======================================================")
        print(markdown_plan)

        # STEP 15: Call the function to save the goal and the generated plan to the log file
        save_plan_to_file(project_goal, markdown_plan)
        print(f"\n✅ Plan successfully logged to **{LOG_FILE}**.")

    except Exception as e:
        # STEP 16: Catch and print any error that occurs during the LLM API call
        print("\n❌ An error occurred during LLM communication:")
        print(f"Error: {e}")
        print("--- Check that Ollama is running and the model is pulled. ---")
