import streamlit as st
from scoring import score_answer
from copilot_client import fetch_questions, copilot_evaluate

def run_interview(domain, resume_text):
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if "questions" not in st.session_state:
        st.session_state.questions = fetch_questions(domain, resume_text)
        st.session_state.answers = {}

    st.header("🧠 Interview In Progress")

    for i, q in enumerate(st.session_state.questions):
        st.markdown(f"**Q{i+1}. {q}**")

        st.session_state.answers[i] = st.text_area(
            "Your answer",
            key=f"ans_{i}",
            disabled=st.session_state.submitted
        )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Submit Interview", disabled=st.session_state.submitted):
            st.session_state.submitted = True

    with col2:
        if st.button("🧹 Clear Answers"):
            st.session_state.answers = {}
            st.session_state.submitted = False
            st.rerun()

    if st.session_state.submitted:
        total = sum(score_answer(a) for a in st.session_state.answers.values())
        transcript = "\n".join(st.session_state.answers.values())

        st.session_state.last_result = copilot_evaluate(transcript, total)
        st.session_state.last_score = total
