import streamlit as st
from MagDBcontroller import connessione, query4db, add_record
import bcrypt
from datetime import datetime
from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx
from navigation import make_sidebar

make_sidebar()

st.title("Welcome to Diamond Corp")

st.write("Please log in to continue (username `test`, password `test`).")
def get_remote_ip() -> str:
    """Get remote ip."""

    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None

        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception as e:
        return None

    return session_info.request.remote_ip

# Create a connection to the database
conn = connessione()

# Create a session state to store user authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["username"] = ""

# Create a tab for login and sign-up
tab_login, tab_signup = st.tabs(["Login", "Sign-up"])

# Login tab
with tab_login:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

    if submit_button:
        query = "SELECT password FROM Credenziali WHERE username = %s"
        results = query4db(conn, query, (username,))
        if results:
            stored_hashed_password = results[0][0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                st.session_state["authenticated"] = True
                st.session_state["username"] = username

                # Add record to AccessiUtenti table
                ip_address = get_remote_ip()
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], [username, datetime.now(), "Successo", ip_address])

                # Add record to LogEventi table
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], [username, datetime.now(), "Login", "Utente ha effettuato il login con successo"])
            else:
                st.error("Invalid username or password")

                # Add record to AccessiUtenti table
                ip_address = get_remote_ip()
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], [username, datetime.now(), "Fallito", ip_address])

                # Add record to LogEventi table
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], [username, datetime.now(), "Login", "Utente ha tentato di effettuare il login con credenziali errate"])
# Sign-up tab
with tab_signup:
    with st.form("signup_form"):
        id_dipendente = st.text_input("ID Dipendente")
        nome = st.text_input("Nome")
        cognome = st.text_input("Cognome")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit_button = st.form_submit_button("Sign-up")

    if submit_button:
        # Verifica se i dati sono presenti nella tabella Dipendenti
        query = "SELECT * FROM Dipendenti WHERE ID_Dipendente = %s AND Nome = %s AND Cognome = %s"
        results = query4db(conn, query, (id_dipendente, nome, cognome))
        if results:
            # Se i dati sono corretti, procedi con la registrazione
            if new_password != confirm_password:
                st.error("Passwords do not match")
            else:
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                ruolo = results[0][4]  # Ottieni il ruolo dal database
                add_record(conn, "Credenziali", ["username", "password", "Ruolo"], [new_username, hashed_password, ruolo])

                # Add record to AccessiUtenti table
                ip_address = get_remote_ip()
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], [new_username, datetime.now(), "Successo", ip_address])

                # Add record to LogEventi table
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], [new_username, datetime.now(), "Signup", "Utente ha creato un nuovo account"])

                st.success("Account creato con successo")
        else:
            st.error("Dati non trovati nella tabella Dipendenti")
            
# Display welcome message if user is authenticated
if st.session_state["authenticated"]:
    st.success(f"Welcome {st.session_state['username']}")