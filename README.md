# 🎭 Character Chatbot

An interactive AI-powered chatbot built with **Python**, **Streamlit**, and the **Groq API** that lets users chat with different AI personalities or create their own custom character.

---

## 🚀 Features

- 🎭 Chat with predefined AI characters:
  - Sherlock Holmes
  - Yoda
  - Tony Stark
- ✨ Create your own custom AI character
- 💬 Real-time conversational interface
- 🧠 Maintains conversation history
- 🔄 Switch characters anytime to start a fresh conversation
- 🗑️ Clear chat history with one click
- ⚡ Powered by Groq's **Llama 3.3 70B Versatile** model
- 🌐 Simple and responsive Streamlit web interface

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Groq API**
- **Python Dotenv**

---

## 📂 Project Structure

```
Character-Chatbot/
│── app.py
│── requirements.txt
│── README.md
│── .env.example
│── .gitignore
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Character-Chatbot.git
cd Character-Chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Create a file named `.env` in the project directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

> **Note:** Never upload your `.env` file to GitHub.

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 🎮 How to Use

1. Select a predefined character from the sidebar.
2. Or enter your own custom character description.
3. Type your message in the chat box.
4. Continue the conversation naturally.
5. Switch characters or clear the conversation whenever you like.

---

## 📸 Preview

<img width="900" alt="Character Chatbot" src="https://via.placeholder.com/900x450.png?text=Character+Chatbot+Screenshot">

> Replace this image with an actual screenshot of your application.

---

## 🤖 Available Characters

| Character | Personality |
|-----------|-------------|
| Sherlock Holmes | Intelligent detective with logical reasoning |
| Yoda | Wise Jedi Master with unique speech style |
| Tony Stark | Funny, sarcastic and highly intelligent |

Users can also create unlimited custom personalities.

---

## 📌 Future Improvements

- Voice input and output
- Multiple AI model selection
- Save chat history
- Export conversations
- Dark/Light theme toggle
- User authentication
- Chat streaming responses
- More built-in characters

---

## 🔐 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 📄 Requirements

```
groq
python-dotenv
streamlit
```

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further development.

---
