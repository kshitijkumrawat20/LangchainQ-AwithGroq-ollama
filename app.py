import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
# langsmith tracking 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
# prompt templates 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please response to the user queries."),
        ("user","{question}"),   
    ]
)

def generate_response(question, api_key,llm,temperature,max_tokens):
    ChatGroq.api_key = api_key
    llm = ChatGroq(model = llm)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question":question})
    return answer

# Title of the app
st.title("ChatBot with Groq")

# side bars for settings 
st.sidebar.title("settings")
api_key = st.sidebar.text_input("Enter your Groq api key here:",type= "password")

# dropdown for model selection
llm = st.sidebar.selectbox("Select a model",["llama3-70b-8192","llama3-8b-8192","mixtral-8x7b-32768","gemma2-9b-it","llama-3.1-8b-instant","llama-3.1-70b-versatile"])

temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

# chat interface
st.write("ask questions")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide question")