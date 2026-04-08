import streamlit as st

# ✅ Demo credentials (can be replaced later)
VALID_USERS = {
    "admin": "admin123",
    "interviewer": "interview123"
}

def login():
    st.title("🔐 Secure Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if username in VALID_USERS and VALID_USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("✅ Login successful")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

    return st.session_state.get("logged_in", False)


def logout():
    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()
