import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assisstant.Please respond to the questions asked."),
        ("user","Question:{question}")
    ]
)

# streamlit framework
st.title("Langchain demo with gemma model")
input_text = st.text_input("what question you have in mind?")

# Ollama gemma model
llm = Ollama(model="gemma3:270m")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))