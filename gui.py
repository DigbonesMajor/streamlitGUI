from dotenv import load_dotenv
from PIL import Image
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st

im = Image.open("Societe-Generale-Emblem.png")

st.set_page_config(page_title="Chat With SGenius",page_icon=im)

# Custom HTML/CSS for the banner
custom_html = """
<div>
    <img src="https://i.imgur.com/JqhplWm.png" style='height: 100%; width: 100%; object-fit: contain'>
</div>
<style>
    .banner {
        border-style: solid;
        border-width: thin;
        border-color: #FFFFFF;
    }
</style>

"""
# Display the custom HTML
st.components.v1.html(custom_html)




if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello! I'm your SGenius assistant. Ask me any query about the Company policy"),
    ]

load_dotenv()

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a single chat application")
    st.text_input("Host",value="localhost")
    st.text_input("Port",value="3306")
    st.text_input("Password",value="******")
    
    st.button("connect")

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI", avatar=im):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

user_query = st.chat_input("Type your Message:")

if user_query is not None and user_query.strip() != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    with st.chat_message("Human", avatar="🤔"):
        st.markdown(user_query)
        
    with st.chat_message("AI", avatar=im):
        response = "Hello! How are you doing 🙂"
        st.markdown(response)
        
    st.session_state.chat_history.append(AIMessage(content=response))