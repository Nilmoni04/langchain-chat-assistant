# LangChain Ollama Chatbot

A simple AI chatbot built using LangChain, Ollama, Streamlit, and LangSmith.

## Features

- Chat interface with Streamlit
- LangChain Prompt Templates
- Output Parser
- Ollama (Gemma 2B)
- LangSmith Tracing
- Local LLM (No OpenAI API Required)

## Tech Stack

- Python
- LangChain
- Ollama
- Gemma 2B
- Streamlit
- LangSmith

## Installation

Clone the repository.

```bash
git clone https://github.com/your-username/langchain-ollama-chatbot.git
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Run Ollama.

```bash
ollama serve
```

Download the model.

```bash
ollama pull gemma:2b
```

Start the application.

```bash
streamlit run app.py
```

## Project Structure

```
.
├── app.py
├── requirements.txt
├── .env
└── README.md
```

## Environment Variables

Create a `.env` file.

```
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=GenAIAPPWithGemini
```

## Author

Nilmoni Pangas
