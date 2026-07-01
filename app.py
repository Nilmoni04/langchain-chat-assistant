import os
from dotenv import load_dotenv

load_dotenv(override=True)

import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------- Environment Variables -------------------- #

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "GenAIAPPWithGemini"

# -------------------- LangChain -------------------- #

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Answer the user's questions accurately and concisely."),
        ("user", "{question}")
    ]
)

llm = OllamaLLM(model="gemma:2b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# -------------------- Streamlit Config -------------------- #

st.set_page_config(
    page_title="LangChain Assistant",
    page_icon="",
    layout="centered",
)

# -------------------- Custom CSS -------------------- #

st.markdown(
    """
    <style>

    .main{
        padding-top:2rem;
    }

    .title{
        font-size:38px;
        font-weight:700;
        text-align:center;
        margin-bottom:0;
    }

    .subtitle{
        text-align:center;
        color:#808080;
        font-size:16px;
        margin-bottom:30px;
    }

    .footer{
        text-align:center;
        color:gray;
        font-size:13px;
        margin-top:40px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- Header -------------------- #

st.markdown("<div class='title'>LangChain Assistant</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Built with LangChain, Ollama, LangSmith and Streamlit</div>",
    unsafe_allow_html=True,
)

# -------------------- Sidebar -------------------- #

with st.sidebar:

    st.header("Application")

    st.write("**Model**")
    st.write("Gemma 2B")

    st.write("**Framework**")
    st.write("LangChain")

    st.write("**Tracing**")
    st.write("LangSmith")

    st.divider()

    st.write(
        "This application demonstrates a basic LangChain pipeline using "
        "Prompt Templates, Ollama LLM and Output Parsers."
    )

# -------------------- Chat History -------------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------- Chat Input -------------------- #

question = st.chat_input("Ask a question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Generating response..."):

            response = chain.invoke(
                {
                    "question": question
                }
            )

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# -------------------- Footer -------------------- #

st.markdown(
    """
    <div class='footer'>
        LangChain • Ollama • Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)