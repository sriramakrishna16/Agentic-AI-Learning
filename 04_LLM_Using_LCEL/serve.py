from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
import uvicorn
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
print(groq_api_key)
model = ChatGroq(model = "openai/gpt-oss-120b", groq_api_key = groq_api_key)

# craete prompt template 
system_template = "translate the following into {language}:"
prompt = ChatPromptTemplate.from_messages(
    [("system",system_template),
     ("user","{text}")]
)

parser = StrOutputParser()

# create chain
chain = prompt|model|parser

# app definition
app = FastAPI(title = "LangChain Server",
              version="1.0",
              description= "simple API server using langchain runnable interfaces")

# adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)
