# 🛡️ Chat Moderation Agent (Streamlit + Gemini AI)

This project is an **AI-powered Chat Moderation Agent** that classifies messages as:

✅ **Safe**  
❌ **Abusive**  
⚠️ **Spam**  
📞 **Contains Phone Number**

Built with **Streamlit**, **Google Gemini API**, and **Plotly** for visualization.

---

## 🚀 Features

- **LLM-based Moderation** using **Gemini AI (gemini-1.5-flash)**  
- **Detects Phone Numbers** using Regex  
- **Attractive UI** with Sample Messages & Interactive Cards  
- **Sidebar Dashboard**:
  - Live **Pie Chart** of moderation stats  
  - **Recent Logs** with Emojis & Colors  
  - **Fun Tips** for Marketplace Safety  
- **Theme Toggle** (Light/Dark Mode)  
- **Session-based Log History**  
- **Streamlit Cloud Deployment Ready**  

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **Backend AI:** Google Gemini API (`gemini-1.5-flash`)
- **Visualization:** Plotly
- **Python Version:** 3.9+

---

## 📂 Project Structure
├── app.py # Main Streamlit App
├── agents/
│ └── chat_moderator.py # Chat Moderation Agent
├── utils/
│ └── validator.py # Utility Functions (Regex for phone number)
├── requirements.txt # Project Dependencies
└── README.md # Documentation

---

## 🔑 Setup & Installation

### 1️⃣ Clone the repository

git clone https://github.com/yourusername/chat-moderation-agent.git
cd chat-moderation-agent
2️⃣ Create Virtual Environment (Optional but recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add your Gemini API Key

Create a .streamlit/secrets.toml file:
[general]
GEMINI_API_KEY = "your_gemini_api_key"
OR set as environment variable:
export GEMINI_API_KEY="your_gemini_api_key"   # Linux/Mac
set GEMINI_API_KEY="your_gemini_api_key"      # Windows
▶ Run Locally
streamlit run app.py
☁ Deploy on Streamlit Cloud

Push your project to GitHub.

Go to Streamlit Cloud
.

Click New App → Connect GitHub Repo.

Add your GEMINI_API_KEY in Secrets:
GEMINI_API_KEY="your_gemini_api_key"
✅ Sample Inputs

Hello, is the product still available?

You idiot, I won't buy from you!

Call me at 9876543210

Click here for the best deal: http://spamlink.com

Can we negotiate the price?
