# AI-Driven-Chatbot 🤖

A simple terminal-based AI chatbot built with **LangChain**, **LangGraph**, and **Groq's** free-tier LLM API (Llama 3.3 70B). Ask questions and get streamed responses right in your terminal.

## Features

- 💬 Interactive command-line chat interface
- ⚡ Powered by Groq's fast LLM inference (free tier)
- 🌊 Streamed responses for real-time output
- 🔧 Built on LangChain's agent framework, ready to extend with custom tools
- 🔐 API keys managed securely via environment variables

## Tech Stack

- [LangChain](https://python.langchain.com/) — agent orchestration
- [LangGraph](https://langchain-ai.github.io/langgraph/) — agent execution engine
- [langchain-groq](https://python.langchain.com/docs/integrations/chat/groq/) — Groq LLM integration
- [Groq API](https://console.groq.com/) — free-tier LLM inference
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management

## Prerequisites

- Python 3.10+
- A free [Groq API key](https://console.groq.com/keys)
- [uv](https://docs.astral.sh/uv/) (or pip) for dependency management

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Ahmedsatti1255/AI-Driven-Chatbot.git
   cd AI-Driven-Chatbot
   ```

2. **Install dependencies**

   Using `uv`:
   ```bash
   uv sync
   ```

   Or using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**

   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

   > ⚠️ Never commit your `.env` file. Make sure it's listed in `.gitignore`.

## Usage

Run the chatbot:

```bash
uv run main.py
```

Or with plain Python:

```bash
python main.py
```

Then just start chatting:

```
Welcome to the AI Chatbot! Type 'exit' to quit.
You can ask questions or give commands to the AI.

You: who created the computer
AI: The computer, as a concept, was...

You: exit
Exiting the AI Chatbot. Goodbye!
```

Type `exit` at any time to quit.

## Project Structure

```
.
├── main.py      # Main chatbot script
├── .env              # API keys (not committed)
├── .gitignore
├── pyproject.toml    # Project dependencies (uv)
└── README.md
```

## Configuration

The chatbot uses Groq's `llama-3.3-70b-versatile` model by default. You can change the model or adjust creativity via `temperature` in `main.py`:

```python
model = ChatGroq(
    model="llama-3.3-70b-versatile",  # or "llama-3.1-8b-instant" for faster responses
    temperature=0.7,
)
```

## Roadmap

- [ ] Add custom tools (web search, calculator, etc.)
- [ ] Add conversation memory across sessions
- [ ] Build a simple web UI
- [ ] Add unit tests

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) or open a pull request.

## Acknowledgments

- [Groq](https://groq.com/) for free, fast LLM inference
- [LangChain](https://www.langchain.com/) for the agent framework
