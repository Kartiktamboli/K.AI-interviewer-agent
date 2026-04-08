import streamlit as st
from auth import login, logout
from agent import run_interview

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
