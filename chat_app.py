import streamlit as st
from test_chatbot import get_bot_response
import uuid


st.title("Simple Chat Interface")
#fixed_bot_output = "This is a sample chat"
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
chat_container = st.container(border=True)
user_input = st.chat_input("Type your message")
if user_input:
    bot_response= get_bot_response(user_input, st.session_state.session_id)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))
with chat_container:
    st.subheader("Chat History")
    for role, content in st.session_state.chat_history:
        left, right = st.columns([1, 2])
    # st.write(f"**{role}**: {content}")
        if role == "You":
            with right:
                with st.chat_message("user"):
                    st.write(content)
        else:
            with left:
                with st.chat_message("assistant"):
                    st.write(content)