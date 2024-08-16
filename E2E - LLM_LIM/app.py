from dotenv import load_dotenv
load_dotenv()  #Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


#Function to load Gemini Pro Model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#Streamlit App
st.set_page_config(page_title="Question and Answering Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

##When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is: ")
    st.write(response)