import streamlit as st
import streamlit_authenticator as stauth

# ✅ Pre-generated bcrypt hash for password: admin123
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
        cookie_name="ai_interviewer",
        key="secret_key",
        cookie_expiry_days=30
    )

    result = authenticator.login(location="main")

    # ✅ Handle both 2‑tuple and 3‑tuple safely
    if isinstance(result, tuple):
        if len(result) == 3:
            name, authentication_status, username = result
        else:
            authentication_status, username = result
            name = username
    else:
        authentication_status = None
        name = None

    if authentication_status:
        st.session_state.logged_in = True
        st.session_state.user = name
    elif authentication_status is False:
        st.error("Invalid username or password")
    else:
        st.warning("Please login to continue")
``
