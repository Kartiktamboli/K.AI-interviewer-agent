import streamlit as st
import streamlit_authenticator as stauth

USERS = {
    "usernames": {
        "admin": {
            "name": "Admin",
            "password": "$2b$12$KIXQbZ8zN2Xz0pC4H7rC6u8xj5cH1fE4J7HqY0pZzv9P9wZ8xYHqG"
        }
    }
}

def login():
    authenticator = stauth.Authenticate(
        credentials=USERS,
        cookie_name="ai_interviewer",
        key="secret_key",
        cookie_expiry_days=30
    )

    authenticator.login(location="main")

    auth_status = st.session_state.get("authentication_status")

    if auth_status:
        st.session_state.logged_in = True
        st.session_state.user = st.session_state.get("name", "User")
        return True

    if auth_status is False:
        st.error("Invalid username or password")

    return False


def logout():
    authenticator = stauth.Authenticate(
        credentials=USERS,
        cookie_name="ai_interviewer",
        key="secret_key",
        cookie_expiry_days=30
    )
    authenticator.logout(location="sidebar")
