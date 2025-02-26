# Q&A Chatbot using Cohere
import cohere
import streamlit as st
import os

# Initialize Cohere with your API key
cohere_api_key = "B2lU0Zy10rgQ1ys8joMX6HKGPiG7OBdSPecizAvg"
co = cohere.Client(cohere_api_key)

# Function to load Cohere model and get response
def get_cohere_response(question):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=question,
        max_tokens=100,
        temperature=0.5
    )
    return response.generations[0].text.strip()

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application with Cohere")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    response = get_cohere_response(input_text)
    st.subheader("The Response is:")
    st.write(response)
