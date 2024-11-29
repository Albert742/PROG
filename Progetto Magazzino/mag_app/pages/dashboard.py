import streamlit as st
from datetime import datetime
from MagDBcontroller import connessione, query4db  # Importa le funzioni dal tuo modulo

# Configurazione della connessione al database
conn = connessione()

# Titolo della Dashboard
st.title("Dashboard Gestione Magazzino")

# Barra laterale per la navigazione
menu = st.sidebar.radio("Menu", ["Prodotti", "Ordini", "Fornitori", "Zone", "Report"])

# Funzione per visualizzare i dati in una tabella
def visualizza_tabella(conn, tabella):
    sql = f"SELECT * FROM {tabella}"
    dati = query4db(conn, sql)
    return dati

# Sezione Prodotti
if menu == "Prodotti":
    st.header("Gestione Prodotti")
    dati = visualizza_tabella(conn, "Prodotti")
    st.write("Dati dei Prodotti")
    st.dataframe(dati)

# Sezione Ordini
elif menu == "Ordini":
    st.header("Gestione Ordini")
    dati = visualizza_tabella(conn, "Ordini")
    st.write("Dati degli Ordini")
    st.dataframe(dati)

# Sezione Fornitori
elif menu == "Fornitori":
    st.header("Gestione Fornitori")
    dati = visualizza_tabella(conn, "Fornitori")
    st.write("Dati dei Fornitori")
    st.dataframe(dati)

# Sezione Zone
elif menu == "Zone":
    st.header("Gestione Zone")
    dati = visualizza_tabella(conn, "Zone")
    st.write("Dati delle Zone")
    st.dataframe(dati)

# Sezione Report
elif menu == "Report":
    st.header("Report Movimenti")
    dati = visualizza_tabella(conn, "StoricoMovimentiMagazzino")
    st.write("Storico Movimenti Magazzino")
    st.dataframe(dati)
