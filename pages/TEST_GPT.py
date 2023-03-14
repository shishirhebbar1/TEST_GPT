import os
import openai
import streamlit as st
st.title("TEST GPT")
# Load your API key from an environment variable or secret management service
openai.api_key ="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"
prompt=st.text_input("WHAT WOULD YOU LIKE US TO DO : ")
if st.button('CLICK'):
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=1000)
    a=response["choices"]
    b=a[0]
    st.write(b["text"])
    

