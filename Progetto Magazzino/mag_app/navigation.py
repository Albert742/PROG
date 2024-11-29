import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.title("F&P Warehose Management System")
        st.write("")
        st.write("")

        if st.session_state.get("authenticated", False):
            st.page_link("pages/dashboard.py", label="Dashboard", icon="🔒")

            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "Acesso":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("accesso_form.py")


def logout():
    st.session_state["authenticated"] = False
    st.info("Utente disconnesso")
    sleep(0.5)
    st.switch_page("accesso_form.py")