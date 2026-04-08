import streamlit as st
import streamlit_authenticator as stauth

# Pre-generated password hash for "admin123"
# Generated once using stauth.Hasher(["admin123"]).hash("admin123")
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
        USERS,
        "ai_interviewer",
        "secret_key",
        30
    )

    name, status, _ = authenticator.login("Login", "main")

    if status:
        st.session_state.logged_in = True
        st.session_state.user = name
    elif status is False:
        st.error("Invalid username or password")
    else:
        st.warning("Please login to continue")
``
