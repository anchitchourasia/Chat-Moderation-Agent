import streamlit as st
import random
import pandas as pd
import plotly.express as px
from agents.chat_moderator import moderate_chat

# ✅ Page Configuration
st.set_page_config(page_title="🛡️ Chat Moderation Agent", page_icon="🛡️", layout="wide")

# ✅ Custom CSS
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 40px;
        color: #1890ff;
        margin-bottom: 10px;
    }
    .description {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 30px;
    }
    .sample-container {
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
        justify-content: center;
        margin-bottom: 20px;
    }
    .sample-card {
        background: #ffffff;
        border: 1px solid #ddd;
        border-radius: 12px;
        padding: 12px 18px;
        font-size: 14px;
        cursor: pointer;
        transition: 0.3s;
        color: #333;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .sample-card:hover {
        background: #e6f7ff;
        border-color: #1890ff;
        color: #1890ff;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Title & Description
st.markdown('<div class="main-title">🛡️ Chat Moderation Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Analyze messages to detect **Safe**, **Abusive**, **Spam**, or **Phone Numbers**.</div>', unsafe_allow_html=True)

# ✅ Sidebar Enhancements
st.sidebar.header("📊 Dashboard")
if "logs" not in st.session_state:
    st.session_state["logs"] = []

# ✅ Fun Facts / Tips
fun_facts = [
    "💡 Did you know? Detecting spam early can save 80% of fraud cases.",
    "🛡 AI moderation improves safety in online marketplaces.",
    "📞 Sharing phone numbers in chat can be risky for privacy.",
    "🤖 AI-powered moderation reduces manual work by 60%.",
    "⚠ Always verify buyer/seller before sharing personal details."
]

st.sidebar.markdown("### 🎯 Quick Tip")
st.sidebar.info(random.choice(fun_facts))

# ✅ Moderation Stats
status_counts = {"Safe": 0, "Abusive": 0, "Spam": 0, "Contains Phone Number": 0}
for log in st.session_state["logs"]:
    if log["status"] in status_counts:
        status_counts[log["status"]] += 1

if sum(status_counts.values()) > 0:
    df_stats = pd.DataFrame({"Status": list(status_counts.keys()), "Count": list(status_counts.values())})
    fig = px.pie(df_stats, names="Status", values="Count", title="Message Classification Distribution", color="Status",
                 color_discrete_map={"Safe": "green", "Abusive": "red", "Spam": "orange", "Contains Phone Number": "blue"})
    st.sidebar.plotly_chart(fig, use_container_width=True)

# ✅ Recent Logs with Colors
st.sidebar.markdown("### 🕒 Recent 5 Logs")
if st.session_state["logs"]:
    for log in reversed(st.session_state["logs"][-5:]):
        color = "✅" if log['status'] == "Safe" else "❌" if log['status'] == "Abusive" else "⚠️" if log['status'] == "Spam" else "📞"
        st.sidebar.markdown(f"{color} **{log['status']}**: {log['message'][:30]}...")

# ✅ Theme Toggle
theme = st.sidebar.radio("🎨 Choose Theme:", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("<style>body {background-color: #121212; color: white;}</style>", unsafe_allow_html=True)

# ✅ Sample Messages
sample_messages = [
    "Hello, is the product still available?",
    "You idiot, I won't buy from you!",
    "Call me at 9876543210",
    "This is the best deal ever! Click here: http://spamlink.com",
    "I am interested. Can we negotiate the price?"
]

# ✅ Display sample messages as clickable cards
st.markdown("### 🔍 Try a Sample Message:")
selected_message = st.session_state.get("selected_message", "")

st.markdown('<div class="sample-container">', unsafe_allow_html=True)
for i, msg in enumerate(sample_messages):
    if st.button(f"Sample {i+1}: {msg[:25]}...", key=f"sample_{i}"):
        selected_message = msg
        st.session_state["selected_message"] = msg
st.markdown('</div>', unsafe_allow_html=True)

# ✅ Input Area
message = st.text_area("✍️ Enter a chat message to analyze:", value=selected_message, height=120)

# ✅ Buttons
col1, col2 = st.columns([1, 1])
with col1:
    analyze = st.button("🔍 Analyze Message")
with col2:
    clear = st.button("🧹 Clear")

if clear:
    st.session_state["selected_message"] = ""
    message = ""

# ✅ Analyze Logic
if analyze:
    if message.strip():
        with st.spinner("🔍 Analyzing message..."):
            result = moderate_chat(message)

        st.subheader("📄 Classification Result (JSON)")
        st.json(result)

        # ✅ Display Status
        status = result.get("status", "Unknown")
        reason = result.get("reason", "No reason provided")

        st.markdown("### 🏷️ Status:")
        if status == "Safe":
            st.success(f"✅ {status}")
        elif status == "Abusive":
            st.error(f"❌ {status}")
        elif status == "Spam":
            st.warning(f"⚠️ {status}")
        elif status == "Contains Phone Number":
            st.info(f"📞 {status}")
        else:
            st.write(status)

        st.markdown(f"**💡 Reason:** {reason}")

        # ✅ Add to Sidebar Logs
        st.session_state["logs"].append({"message": message, "status": status, "reason": reason})
    else:
        st.warning("⚠️ Please enter a message to analyze.")
