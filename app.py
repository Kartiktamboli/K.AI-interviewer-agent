import streamlit as st
from agent import run_interview

st.set_page_config(page_title="AI Interviewer", layout="centered")

st.title("🤖 AI Interviewer (Agentic)")
st.write("Select a domain to begin your interview.")

domain = st.selectbox(
    "Choose Interview Domain",
    [
        "DSA",
        "OOP",
        "SQL",
        "Frontend",
        "Backend",
        "System Design",
        "Cloud & DevOps",
        "Behavioral"
    ]
)

if st.button("🚀 Start Interview"):
    run_interview(domain)
