# 🧪 QA Retro AI Assistant

A simple command-line tool powered by OpenAI that helps QA teams collect feedback, group it, identify themes, and generate actionable improvements in retrospectives.

## 📦 Installation

### 1. Clone this repository

```bash
git clone 
cd qa-retro-ai-assistant
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API key

- Open `.env` and paste your OpenAI API key:

```bash
OPENAI_API_KEY=sk-xxxxxx
```

## 🚀 Usage

### Add Feedback

Add a new QA feedback item:

```bash
python retro.py add
```

You'll be prompted:

```
Enter feedback: Test environment goes down randomly
Enter QA name: QA1
✅ Saved feedback from QA1
```

Run the command again to add feedback from more QA team members.

### List Feedback

Show all collected feedback:

```bash
python retro.py list
```

Output:

```
--- All QA Feedback ---
[QA1] Test environment goes down randomly
[QA2] Too many flaky tests block automation
[QA3] CI/CD pipeline is too slow
```

### Summarize Feedback

Generate a comprehensive retro summary with per-QA notes, common themes, and actionable items:

```bash
python retro.py summarize
```

Example output:

```
--- QA Retro Summary ---

1. Per QA Feedback
- QA1: Test environment goes down randomly
- QA2: Too many flaky tests block automation  
- QA3: CI/CD pipeline is too slow

2. Common Themes
- Environment instability
- Flaky tests
- Slow CI/CD pipeline

3. Action Items
- Add monitoring to stabilize test environment
- Dedicate time to fix flaky tests
- Optimize CI/CD with caching
```

### Reset Feedback

Clear all saved feedback to start fresh:

```bash
python retro.py reset
```

Output:

```
🗑️ Cleared all feedback.
```

## 🛠 Requirements

- **Python 3.9+**
- **OpenAI API key** (get one at [platform.openai.com](https://platform.openai.com))

## 📁 Project Structure

```
qa-retro-ai-assistant/
├── retro.py              # Main CLI application
├── requirements.txt      # Python dependencies
├── .env                 # Your API keys (create from .env.example)
├── feedback.json        # Stored feedback data (auto-generated)
└── README.md           # This file
```

## 🎯 Features

- **Simple CLI interface** - Easy to use during team meetings
- **Persistent storage** - Feedback is saved locally in JSON format
- **AI-powered analysis** - Uses OpenAI to identify patterns and generate insights
- **Team-friendly** - Collect feedback from multiple QA team members
- **Actionable output** - Generates concrete action items for improvement

## 💡 Use Cases

- **Sprint retrospectives** - Collect and analyze QA feedback after each sprint
- **Process improvement** - Identify recurring issues and bottlenecks
- **Team alignment** - Surface common concerns across QA team members
- **Management reporting** - Generate structured summaries for leadership

**Happy retrospecting! 🎉**
