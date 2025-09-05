import os
import json
import requests
import typer
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()

API_KEY = os.getenv("OPENAI_API_KEY")
CHAT_URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
FILE = "feedback.json"


@app.command()
def add(feedback: str = typer.Option(None, prompt="Enter feedback"),
        qa: str = typer.Option(None, prompt="Enter QA name")):
    """Add feedback from a QA."""
    data = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)
    data.append({"qa": qa, "feedback": feedback})
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved feedback from {qa}")


@app.command()
def list():
    """Show all feedback."""
    if not os.path.exists(FILE):
        print("⚠️ No feedback yet.")
        return
    with open(FILE, "r") as f:
        data = json.load(f)
    print("\n--- All QA Feedback ---")
    for item in data:
        print(f"[{item['qa']}] {item['feedback']}")


@app.command()
def summarize():
    """Summarize feedback into per-QA notes, themes, and action items."""
    if not os.path.exists(FILE):
        print("⚠️ No feedback to summarize.")
        return
    with open(FILE, "r") as f:
        data = json.load(f)

    feedback_text = "\n".join(f"[{item['qa']}] {item['feedback']}" for item in data)

    # Prompt template
    prompt = f"""
You are a QA Retrospective assistant.
Here is the collected QA feedback:

{feedback_text}

Please provide the output in the following format:

1. **Per QA Feedback**
   - List each QA with their feedback separately.

2. **Common Themes**
   - Identify recurring patterns or issues across QAs.

3. **Action Items**
   - Suggest clear, actionable improvements the team can implement.
"""

    messages = [
        {"role": "system", "content": "You are a helpful QA Retrospective assistant."},
        {"role": "user", "content": prompt}
    ]

    response = requests.post(CHAT_URL, headers=HEADERS, json={
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.7
    })
    response.raise_for_status()
    summary = response.json()["choices"][0]["message"]["content"]

    print("\n--- QA Retro Summary ---")
    print(summary)


@app.command()
def reset():
    """Clear all feedback."""
    if os.path.exists(FILE):
        os.remove(FILE)
    print("🗑️ Cleared all feedback.")


if __name__ == "__main__":
    app()
