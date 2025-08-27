from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

# st.title("chatbot with openAI and Langchain")
api_key = os.getenv("OPANAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

#llm model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
from langchain_core.messages import  HumanMessage

# print(llm.invoke([HumanMessage(content="I'm suji")]))
# print(llm.invoke([HumanMessage(content="whats my name?")]))


#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)


st.title("Chatbot with OpenAI and Langchain")
user_question = st.text_input("Ask a question about LLMs")
outputParser = StrOutputParser()
chain = prompt | llm | outputParser

if user_question:
    response = chain.invoke({"question":user_question})
    st.write(response)