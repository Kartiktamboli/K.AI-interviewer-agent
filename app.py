import streamlit as st
from auth import login, logout
from agent import run_interview

st.markdown("""
<style>
/* Global */
body {
    background-color: #0e1117;
    color: #fafafa;
}

/* Titles */
h1, h2, h3 {
    color: #4fc3f7;
    font-weight: 700;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #1e88e5, #42a5f5);
    color: white;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 600;
    border: none;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #1565c0, #1e88e5);
}

/* Inputs */
input, textarea {
    border-radius: 8px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Cards */
.card {
    background: #1f2937;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 16px;
    box-shadow: 0 0 15px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="AI Interview Platform", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# ✅ Sidebar after login
st.sidebar.success(f"Logged in as {st.session_state.user}")
logout()

# ✅ Candidate Context
st.sidebar.header("Candidate Profile")
candidate_name = st.sidebar.text_input("Candidate Name")
candidate_email = st.sidebar.text_input("Candidate Email")

resume = st.sidebar.file_uploader("Upload Resume (PDF/Text)")

domain = st.sidebar.selectbox(
    "Interview Domain",
    [
        "DSA",
        "OOP",
        "SQL",
        "Frontend",
        "Backend",
        "System Design",
        "Cloud & DevOps"
    ]
)

resume_text = resume.read().decode("utf-8") if resume else "No resume provided"

run_interview(domain, resume_text)
