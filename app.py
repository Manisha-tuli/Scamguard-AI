import streamlit as st

st.title("My first streamlit application")

st.write("Hello World, Welcome to my application")
# st.title("Playing with widgets")
# name=st.text_input("enter your name")
# st.write(f"Hello,{name}")

# st.title("Playing with widgets - 3")

# col1, col2 = st.columns(2)

# with col1:

#     name = st.text_input("Enter your name")

# with col2:

#     age = st.slider("Select your age", 0, 100, 25)

# if(st.button("Submit")):

#     st.write(f"Hello, {name}!")

#     st.write(f"Your age is {age}")

# st.title("Widget Playground with Expanders")

# # Expander for personal details

# with st.expander(" Personal Details"):

#     name = st.text_input("Enter your name:")

#     age = st.slider("Select your age:", 0, 100, 25)

# # Expander for preferences

# with st.expander(" Preferences"):

#     color = st.selectbox("Choose your favorite color:", ["Red", "Green", "Blue"])

#     subscribe = st.checkbox("Subscribe to newsletter")

# # Expander for submission

# with st.expander(" Submit"):

#     if st.button("Submit"):

#         st.write(f"Hello {name}, you are {age} years old.")

#         st.write(f"Favorite color: {color}")

#         if subscribe:

#             st.success("You are subscribed! ")

#         else:

#             st.info("You are not subscribed.")

#6.
# st.title("Widget Playground with Tabs")

# # Create tabs

# tab1, tab2, tab3 = st.tabs([" Personal Details", " Preferences", " Submit"])

# # Tab 1 - Personal Details

# with tab1:

#     name = st.text_input("Enter your name:")

#     age = st.slider("Select your age:", 0, 100, 25)

# # Tab 2 - Preferences

# with tab2:

#     color = st.selectbox("Choose your favorite color:", ["Red", "Green", "Blue"])

#     subscribe = st.checkbox("Subscribe to newsletter")

# # Tab 3 - Submit

# with tab3:

#     if st.button("Submit"):

#         st.write(f"Hello {name}, you are {age} years old.")

#         st.write(f"Favorite color: {color}")

#         if subscribe:

#             st.success("You are subscribed! ")

#         else:

#             st.info("You are not subscribed.")
#7.
# def my_function(text):

#     return text[::-1]

# st.title("Streamlit app with functions")

# user_text = st.text_input("Enter your string to be reversed")

# if(st.button("Run")):

#     if(user_text.strip()):

#         result = my_function(user_text)

#         st.write(f"Your reversed text is - {result}")

#     else:

#         st.write("Please input a text")
####dataframes
# import pandas as pd

# data = {

#     "Name": ["Alice", "Bob", "Charlie", "David"],

#     "Age": [24, 30, 22, 28],

#     "City": ["New York", "Paris", "London", "Berlin"]

# }

# df = pd.DataFrame(data)

# st.subheader("Displaying DataFrames in Streamlit")

# st.dataframe(df)

# st.subheader("Static table")

# st.table(df)
### making a chat interface

### 10 - Making the chat interface with history

# import streamlit as st

# st.title("Simple Chat Interface")

# # Fixed output from bot

# fixed_bot_ouptut = "This is a sample chat"

# # Initialize chat history in session state

# if "chat_history" not in st.session_state:

#     st.session_state.chat_history = []

 

 

# chat_container = st.container(border= True)

# # Get user input

# user_input = st.text_input("You: ")

# if(st.button("Send")):

#     if(user_input.strip()):

#         # Append user input to chat history

#         st.session_state.chat_history.append(("You", user_input))

#         # Append bot response to chat history

#         st.session_state.chat_history.append(("Bot", fixed_bot_ouptut))

#     else:

#         st.write("Please input a text")

# # print the entire chat history

# # for role, content in st.session_state.chat_history:

# #     st.write(f"**{role}:** {content}")
# # Chat container



# with chat_container:

#     st.subheader("Chat History")

#     for role, content in st.session_state.chat_history:

#         st.write(f"**{role}:** {content}")

import streamlit as st

st.title("Simple Chat Interface")

# Fixed output from bot

fixed_bot_output = "This is a sample chat"

# Initialize chat history in session state

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# Chat container

chat_container = st.container(border = True)

# Input area

user_input = st.chat_input("You:")

if user_input:

    st.session_state.chat_history.append(("user", user_input))

    st.session_state.chat_history.append(("assistant", fixed_bot_output))

else:

    st.write("Please input a text")

 

 

# with chat_container:

#     st.subheader("Chat History")

    # for role, content in st.session_state.chat_history:

    #     st.write(f"**{role}:** {content}")

with chat_container:

    st.subheader("Chat History")

    for role, content in st.session_state.chat_history:

        with st.chat_message(role):

            st.write(content)

        