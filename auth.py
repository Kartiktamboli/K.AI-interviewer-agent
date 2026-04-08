
import streamlit as st
import streamlit_authenticator as stauth

USERS = {
    "usernames": {
        "admin": {
            "name": "Admin",
            "password": stauth.Hasher(["admin123"]).generate()[0]
        }
    }
}


def login():
    authenticator = stauth.Authenticate(
        USERS,
        "ai_interviewer",
        "secret_key",
        1
    )
    name, status, _ = authenticator.login("Login", "main")
    if status:
        st.session_state.logged_in = True
        st.session_state.user = name
    elif status is False:
        st.error("Invalid credentials")
    else:
        st.warning("Please login")
