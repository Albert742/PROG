"""
import streamlit as st
from MagDBcontroller import connessione, add_record, selectSQL
import bcrypt
from datetime import datetime
from streamlit import runtime
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from navigation import make_sidebar

st.title("Benvenuto")
st.write("Per continuare, effettua il login o crea un account.")

def get_remote_ip() -> str:
    Get remote IP.
    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None

        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception:
        return None

    return session_info.request.remote_ip

# Crea una connessione al database
conn = connessione()

# Sessione per autenticazione utente
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["username"] = ""

# Creazione di tab per login e registrazione
tab_login, tab_signup = st.tabs(["Login", "Sign-up"])

# Login tab
with tab_login:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

    if submit_button:
        results = selectSQL("Credenziali", ["password"], f"username = '{username}'")
        if results:
            stored_hashed_password = results[0][0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                st.session_state["authenticated"] = True
                st.session_state["username"] = username

                # Registra l'accesso riuscito
                ip_address = get_remote_ip()
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], 
                           [username, datetime.now(), "Successo", ip_address])
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], 
                           [username, datetime.now(), "Login", "Accesso effettuato con successo"])
                
                st.success("Accesso riuscito")
                sleep(0.5)
                st.switch_page("pages/dashboard.py")
            else:
                st.error("Password o username errati")
                
                # Registra l'accesso fallito
                ip_address = get_remote_ip()
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], 
                           [username, datetime.now(), "Fallito", ip_address])
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], 
                           [username, datetime.now(), "Login", "Accesso fallito: credenziali errate"])
        else:
            st.error("Utente non trovato")

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
        # Verifica dipendente
        results = selectSQL("Dipendenti", ["*"], 
                            f"ID_Dipendente = '{id_dipendente}' AND Nome = '{nome}' AND Cognome = '{cognome}'")
        if results:
            if new_password != confirm_password:
                st.error("Le password non corrispondono")
            else:
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                ruolo = results[0][4]  # Ottieni il ruolo

                # Aggiungi credenziali
                add_record(conn, "Credenziali", ["username", "password", "Ruolo"], 
                           [new_username, hashed_password, ruolo])

                # Registra evento di creazione account
                ip_address = get_remote_ip()
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], 
                           [new_username, datetime.now(), "Successo", ip_address])
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], 
                           [new_username, datetime.now(), "Signup", "Nuovo account creato con successo"])
                
                st.success("Account creato con successo")
                sleep(0.5)
                st.switch_page("pages/dashboard.py")
        else:
            st.error("Dati non trovati nella tabella Dipendenti")
"""
import streamlit as st
from MagDBcontroller import connessione, add_record, selectSQL
import bcrypt
from datetime import datetime
from streamlit import runtime
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from navigation import make_sidebar

make_sidebar()

st.title("Benvenuto")
st.write("Per continuare, effettua il login.")

def get_remote_ip() -> str:
    """Get remote IP."""
    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None

        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception:
        return None

    return session_info.request.remote_ip

# Crea una connessione al database
conn = connessione()
if conn is None:
    st.error("Connessione al database fallita.")
    st.stop()

# Sessione per autenticazione utente
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["username"] = ""

# Creazione di tab per login e registrazione
tab_login, tab_signup = st.tabs(["Login", "Sign-up"])

# Login tab
with tab_login:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

    if submit_button:
        st.write("Eseguendo login...")
        results = selectSQL("Credenziali", ["password"], f"username = '{username}'")
        st.write(f"Risultati query credenziali: {results}")
        if results:
            stored_hashed_password = results[0][0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                st.session_state["authenticated"] = True
                st.session_state["username"] = username

                ip_address = get_remote_ip()
                st.write(f"IP remoto: {ip_address}")

                # Registra l'accesso riuscito
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], 
                           [username, datetime.now(), "Successo", ip_address])
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], 
                           [username, datetime.now(), "Login", "Accesso effettuato con successo"])
                
                st.success("Accesso riuscito")
                sleep(0.5)
                st.switch_page("pages/dashboard.py")
            else:
                ip_address = get_remote_ip()
                st.write(f"IP remoto: {ip_address}")
                st.error("Password o username errati")
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], 
                           [username, datetime.now(), "Fallito", ip_address])
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], 
                           [username, datetime.now(), "Login", "Accesso fallito: credenziali errate"])
        else:
            st.error("Utente non trovato")

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
        st.write(f"Step 1: ID: {id_dipendente}, Nome: {nome}, Cognome: {cognome}")
        st.write("Eseguendo query verifica dipendente...")
        query_conditions = (
            f"ID_Dipendente = '{id_dipendente}' AND "
            f"Nome = '{nome}' AND "
            f"Cognome = '{cognome}'"
        )
        st.write(f"Condizioni query: {query_conditions}")

        results = selectSQL("Dipendenti", ["*"], query_conditions)
        st.write(f"Risultati query dipendente: {results}")

        if results:
            if new_password != confirm_password:
                st.error("Le password non corrispondono")
            else:
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                ruolo = results[0][4]  # Ottieni il ruolo

                # Aggiungi credenziali
                st.write(f"Registrando nuovo utente con ruolo: {ruolo}")
                add_record(conn, "Credenziali", ["username", "password", "Ruolo"], 
                           [new_username, hashed_password, ruolo])

                ip_address = get_remote_ip()
                st.write(f"IP remoto: {ip_address}")

                # Registra evento di creazione account
                add_record(conn, "AccessiUtenti", ["ID_Utente", "DataOra", "Esito", "IP"], 
                           [new_username, datetime.now(), "Successo", ip_address])
                add_record(conn, "LogEventi", ["ID_Utente", "DataOra", "Azione", "Dettagli"], 
                           [new_username, datetime.now(), "Signup", "Nuovo account creato con successo"])
                
                st.success("Account creato con successo")
                sleep(0.5)
                st.switch_page("pages/dashboard.py")
        else:
            st.error("Dati non trovati nella tabella Dipendenti")
            st.write("Verifica i dati inseriti e riprova.")

# Mostra messaggio di benvenuto se autenticato
if st.session_state["authenticated"]:
    st.success(f"Benvenuto {st.session_state['username']}")
    sleep(0.5)
    st.switch_page("pages/dashboard.py")
