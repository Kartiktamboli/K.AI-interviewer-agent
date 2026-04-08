import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import scoring
from question_bank import QUESTION_BANK

def run_interview(domain):
    questions = QUESTION_BANK[domain]
    total_score = 0

    st.subheader(f"📌 {domain} Interview")

    for i, q in enumerate(questions, 1):
        st.markdown(f"**Q{i}. {q}**")
        answer = st.text_area("Your answer:", key=f"{domain}_{i}")

        if answer:
            s = scoring.score_answer(answer)
            total_score += s

            if s == 0:
                st.warning("Answer is shallow. Please elaborate.")
            elif s == 1:
                st.info("Basic understanding observed.")
            else:
                st.success("Good depth and clarity.")

        st.divider()

    level = scoring.detect_level(total_score)

    st.success("✅ Interview Completed")
    st.markdown(f"### 🎯 Detected Level: **{level}**")
    st.markdown(f"**Total Score:** {total_score} / {len(questions)*2}")
