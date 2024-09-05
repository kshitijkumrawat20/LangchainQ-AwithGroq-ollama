from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please response to the user queries."),
        ("user","{question}")
    ]
)

def generate_response(question,engine, temperature, max_tokens):
    llm = ollama(model = engine)
    output_parser = StrOutputParser()
    chain = prompt |llm | output_parser
    answer =chain.invoke({"question":question})
    return answer

# Title of the app
st.title("ChatBot with Groq")


# dropdown for model selection
engine = st.sidebar.selectbox("Select a model",["gemma2:2b"])

temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

# chat interface
st.write("ask questions")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide question")