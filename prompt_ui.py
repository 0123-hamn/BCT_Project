from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

st.title("Professional Email Writer Assistant")

sender_name = st.text_input("Enter your name")

recipient_name = st.text_input("Reciver name")

purpose_input = st.text_input("Enter the purpose of writing the e-mail")

tone_input = st.selectbox('Select the tone',['Formal','Semi-Formal','Persuasive'])

template = load_prompt('email_generator_template.json')

if st.button('Generate'):

    chain = template|model
    result = chain.invoke({
        'sender_name':sender_name,
        'recipient_name':recipient_name,
        'tone_input':tone_input,
        'purpose_input': purpose_input
    })
    st.write(result.content)
