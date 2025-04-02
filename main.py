import datetime

import streamlit as st

from agent import chat_with_agent

# Set page title and configuration
st.set_page_config(page_title="Guess my PIN", page_icon="💬")
st.title("¡Adivina mi PIN!")
gemini_api_key = st.secrets["GEMINI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        st.caption(message["time"])

initial_text = "Hola, ¿en qué puedo ayudarte?"
user_input = st.chat_input(initial_text)

with st.sidebar:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if st.button("Limpiar", type="secondary"):
        st.session_state.messages = [{"role": "assistant", "content": initial_text, "time": current_time}]
        st.rerun()


if user_input:
    # Add user message to chat history
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append(
        {"role": "user", "content": user_input, "time": current_time}
    )
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
        st.caption(current_time)
    
    # Simulate assistant response
    with st.chat_message("assistant"):
        response = chat_with_agent(st.session_state.messages,gemini_api_key)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        st.write(response)
        st.caption(current_time)
    
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response, "time": current_time}
    )

