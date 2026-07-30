"""
Character Chatbot - Web App Version
------------------------------------
Same chatbot as chatbot.py, but running in the browser using Streamlit.

Run with: streamlit run app.py
"""

import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# ---------------------------------------------------------
# 1. Load the API key from the .env file
# ---------------------------------------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error(
        "No API key found. Make sure you have a .env file with:\n\n"
        "GROQ_API_KEY=your_key_here"
    )
    st.stop()  # stops the app here instead of crashing further down

client = Groq(api_key=api_key)
MODEL = "llama-3.3-70b-versatile"

# ---------------------------------------------------------
# 2. Define the available characters (same as chatbot.py)
# ---------------------------------------------------------
CHARACTERS = {
    "Sherlock Holmes": (
        "You are Sherlock Holmes, the brilliant detective from 221B Baker "
        "Street. You speak precisely and formally, notice tiny details "
        "about the people you talk to, and enjoy making sharp deductions. "
        "Keep your replies fairly short and in character."
    ),
    "Yoda": (
        "You are Yoda from Star Wars. Speak in Yoda's distinctive "
        "inverted sentence style (e.g. 'Much to learn, you still have.'). "
        "Give calm, wise advice. Keep replies short and in character."
    ),
    "Tony Stark": (
        "You are Tony Stark: witty, confident, a little sarcastic, but "
        "brilliant and ultimately helpful. Keep replies punchy and in "
        "character, with the occasional joke."
    ),
}

# ---------------------------------------------------------
# 3. Page setup + sidebar (character selection menu)
# ---------------------------------------------------------
st.set_page_config(page_title="Character Chatbot", page_icon="🎭")
st.title("🎭 Character Chatbot")

with st.sidebar:
    st.header("Choose a character")
    selected_name = st.selectbox("Character", list(CHARACTERS.keys()))

    st.divider()
    custom_text = st.text_area(
        "...or describe a custom character",
        placeholder="e.g. A grumpy medieval blacksmith who complains a lot",
    )
    use_custom = st.button("Use custom character")

    st.divider()
    if st.button("🗑️ Clear conversation"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------------------------------
# 4. Figure out which character is active
# ---------------------------------------------------------
# session_state is Streamlit's way of remembering things between reruns
# (every click/input causes the whole script to rerun from the top,
# so without session_state you'd lose your chat history each time).
if "active_character" not in st.session_state:
    st.session_state.active_character = selected_name
    st.session_state.system_prompt = CHARACTERS[selected_name]
    st.session_state.messages = []

if use_custom and custom_text.strip():
    st.session_state.active_character = "Custom Character"
    st.session_state.system_prompt = custom_text.strip()
    st.session_state.messages = []  # start fresh with the new character
    st.rerun()

elif selected_name != st.session_state.active_character and not use_custom:
    st.session_state.active_character = selected_name
    st.session_state.system_prompt = CHARACTERS[selected_name]
    st.session_state.messages = []  # start fresh when switching characters
    st.rerun()

st.caption(f"Currently chatting with: **{st.session_state.active_character}**")

# ---------------------------------------------------------
# 5. Show existing conversation
# ---------------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------------------------------
# 6. Chat input box at the bottom of the page
# ---------------------------------------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # show the user's message immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # build the full message list: system prompt + history
    api_messages = [
        {"role": "system", "content": st.session_state.system_prompt}
    ] + st.session_state.messages

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=api_messages,
                )
            reply = response.choices[0].message.content
            st.markdown(reply)
            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )
        except Exception as e:
            st.error(f"Error talking to the API: {e}")
