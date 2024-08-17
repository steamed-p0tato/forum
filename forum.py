import streamlit as st

st.header("*Discussion forum* for :red[Protests] ")

if 'messages' not in st.session_state:
    st.session_state.messages = ["Garbage"]

message = st.chat_input("Enter a message")  # st.chat_input is not a valid Streamlit function

if message:
    st.session_state.messages.append(message)

for i in st.session_state.messages:
    st.text(f"Anon: {i}")