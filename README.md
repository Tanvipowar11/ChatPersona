# Character Chatbot

A simple terminal chatbot that lets you pick a character personality and chat
with it using the Groq API (`llama-3.3-70b-versatile`).

## Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Add your API key**

   Copy `.env.example` to `.env` and paste in your real Groq API key:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` so it looks like:

   ```
   GROQ_API_KEY=gsk_your_real_key_here
   ```

3. **Run it**

   ```bash
   python chatbot.py
   ```

## How it works

- `CHARACTERS` is a dictionary of preset personalities (Sherlock Holmes,
  Yoda, Tony Stark) plus a "Custom Character" option where you type your own
  description at runtime.
- `choose_character()` prints a menu and validates your input.
- `chat_with_character()` starts a fresh `messages` list with the character's
  system prompt as the **first and only** system message, then appends each
  user message and assistant reply so the model keeps full context.
- Type `switch` during a chat to go back to the character menu, or `quit` to
  exit.

## Adding your own characters

Open `chatbot.py` and add a new entry to the `CHARACTERS` dictionary:

```python
"5": {
    "name": "Your Character Name",
    "system_prompt": "You are ... (describe personality and speech style).",
},
```

## Web App Version (Streamlit)

There's also a browser-based version, `app.py`, built with
[Streamlit](https://streamlit.io) — a Python library that turns a script
into a web app without writing any HTML/CSS/JavaScript.

1. Install the extra dependency (already in `requirements.txt`):

   ```bash
   pip install -r requirements.txt
   ```

2. Run it:

   ```bash
   streamlit run app.py
   ```

3. It will automatically open a browser tab (usually at
   `http://localhost:8501`). Pick a character from the sidebar, or type a
   custom character description, and start chatting.

### How the web version differs from the terminal version

- Instead of `input()` and `print()`, it uses `st.chat_input()` and
  `st.chat_message()` to build a chat interface.
- Since Streamlit reruns the whole script on every interaction, it uses
  `st.session_state` to remember the conversation between reruns (otherwise
  the chat history would reset every time you sent a message).
- Switching characters in the sidebar automatically starts a new
  conversation, same as `switch` did in the terminal version.

### Sharing it with others

Running `streamlit run app.py` only makes it available on your own computer.
To share it with someone else without them installing anything, you can
deploy it for free on [Streamlit Community Cloud](https://streamlit.io/cloud) —
just push this project to a GitHub repo and connect it there. (You'd add
your API key as a "secret" in Streamlit Cloud's settings instead of a local
`.env` file, since `.env` shouldn't be uploaded to GitHub.)

## Notes

- Each character conversation is independent — switching characters starts a
  brand new `messages` list, so personalities don't bleed into each other.
- If an API call fails (e.g. bad key, rate limit, network issue), the error
  is caught and printed instead of crashing the program, so you can just try
  again.
