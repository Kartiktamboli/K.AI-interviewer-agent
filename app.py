import streamlit as st
from auth import login
from agent import run_interview

st.set_page_config(page_title="AI Interviewer", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

st.sidebar.title(f"Welcome {st.session_state.user}")

domain = st.sidebar.selectbox(
    "Select Domain",
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

run_interview(domain)
``
