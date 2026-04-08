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

    result = authenticator.login(location="main")

    name = None
    authentication_status = None

    if isinstance(result, tuple):
        if len(result) == 3:
            name, authentication_status, _ = result
        elif len(result) == 2:
            authentication_status, name = result

    if authentication_status:
        st.session_state.logged_in = True
        st.session_state.user = name or "User"
    elif authentication_status is False:
        st.error("Invalid username or password")
    else:
        st.warning("Please login to continue")
``
