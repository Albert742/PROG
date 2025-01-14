from sqlalchemy import create_engine, text, insert, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, IntegrityError
from datetime import datetime
import time
import toml

def connessione():
    """
    Esegue la connessione al database SQLite specificato nel file DBloc.toml
    e restituisce un oggetto Session per l'interazione con il database.

    Se la connessione non riesce dopo 3 tentativi, restituisce None.
    """

    toml_data = toml.load("C:/Users/alber/Documents/PROG/SQlite/.loc/DBloc.toml")
    database = toml_data["sqlite"]["database"]

    connection_string = f"sqlite:///{database}"

    engine = None
    session = None
    max_retries = 3
    retry_delay = 2

    for attempt in range(1, max_retries + 1):
        try:
            engine = create_engine(connection_string)
            Session = sessionmaker(bind=engine)
            session = Session()
            print(f"Connessione al database riuscita (tentativo {attempt}).")
            return session
        except OperationalError as e:
            print(f"Errore di connessione al database (tentativo {attempt}/{max_retries}): {e}")
            if attempt < max_retries:
                print(f"Riprovando tra {retry_delay} secondi...")
                time.sleep(retry_delay)
            else:
                print("Numero massimo di tentativi di connessione raggiunto.")
                return None

    return None

def create_database():
    """
    Crea il database se non esiste già.
    """
    toml_data = toml.load(".loc/DBloc.toml")
    database = toml_data["sqlite"]["database"]

    connection_string = f"sqlite:///{database}"

    engine = create_engine(connection_string)
    with engine.connect() as conn:
        print(f"Database '{database}' creato con successo (se non esisteva già).")

def create_tableSQL(session, nome_tabella, definizione):
    """
    Crea una tabella nel database se non esiste.
    """
    try:
        table_name = get_table_name(session, nome_tabella)
        if table_name:
            print(f"La tabella {nome_tabella} esiste già.")
            return False

        with session.begin():
            # Remove backticks for SQLite compatibility
            sql = f"CREATE TABLE IF NOT EXISTS {nome_tabella} ({definizione})"
            # Enable foreign key support
            session.execute(text("PRAGMA foreign_keys = ON;"))
            session.execute(text(sql))
        return True
    except Exception as e:
        session.rollback()
        print(f"Errore durante la creazione della tabella {nome_tabella}: {e}")
        return False

def init_tables(session):
    """
    Tabelle da inizializzare del database.
    """
    tabelle = {
        "Attivita": """
            ID_Attivita INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            Nome TEXT NOT NULL,
            Descrizione TEXT
        """,
        "Scadenziario": """
            ID_Scadenziario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            ID_Attivita INTEGER NOT NULL,
            DataSchedulazione TEXT NOT NULL CHECK(datetime(DataSchedulazione) IS NOT NULL),
            DataEsecuzione TEXT CHECK(datetime(DataEsecuzione) IS NOT NULL OR DataEsecuzione IS NULL),
            DataScadenza TEXT NOT NULL CHECK(datetime(DataScadenza) IS NOT NULL),
            Tipo TEXT NOT NULL CHECK(Tipo IN ('Ordinaria', 'Straordinaria', 'Urgente')),
            Stato TEXT DEFAULT 'Programmata' CHECK(Stato IN ('Programmata', 'Completata', 'Annullata')),
            Note TEXT,
            FOREIGN KEY (ID_Attivita) REFERENCES Attivita(ID_Attivita) ON DELETE CASCADE
        """,
        "Notifica": """
            ID_Notifica INTEGER PRIMARY KEY AUTOINCREMEN NOT NULL UNIQUE,
            ID_Scadenziario INTEGER NOT NULL,
            DataNotifica TEXT NOT NULL CHECK(datetime(DataNotifica) IS NOT NULL),
            Tipo TEXT NOT NULL CHECK(Tipo IN ('Avviso', 'Allarme')),
            Stato TEXT DEFAULT 'Attivo' CHECK(Stato IN ('Attivo', 'Disattivato')),
            Messaggio TEXT,
            FOREIGN KEY (ID_Scadenziario) REFERENCES Scadenziario(ID_Scadenziario) ON DELETE CASCADE
        """,
        
    }
    for nome_tabella, definizione in tabelle.items():
        create_tableSQL(session, nome_tabella, definizione)



def initSQL():
    """
    Funzione per inizializzare le tabelle del database.
    
    Creazione delle tabelle del database in base alla definizione contenuta nel dizionario tabelle.
    
    Returns:
        None
    """
    with connessione() as conn:
        if conn:
            init_tables(conn)

def get_table_name(session, nome_tabella):
    """
    Restituisce il nome della tabella esistente nel database, indipendentemente dalle maiuscole/minuscole.

    Args:
        session: L'oggetto sessione SQLAlchemy.
        nome_tabella (str): Il nome della tabella da cercare.

    Returns:
        str: Il nome della tabella esistente nel database.
    """
    metadata = MetaData()
    metadata.reflect(bind=session.bind)
    table_names = metadata.tables.keys()
    for table_name in table_names:
        if table_name.lower() == nome_tabella.lower():
            return table_name
    return None

def add_recordSQL(session, nome_tabella, dati):
    try:
        table_name = get_table_name(session, nome_tabella)
        if not table_name:
            print(f"Errore: La tabella {nome_tabella} non esiste.")
            return False

        with session.begin_nested():
            session.execute(text("PRAGMA foreign_keys = ON"))
            colonne = ", ".join(key for key in dati.keys())
            valori = ", ".join(f":{key}" for key in dati.keys())
            sql = f"INSERT INTO {table_name} ({colonne}) VALUES ({valori})"
            session.execute(text(sql), dati)
        return True
    except Exception as e:
        session.rollback()
        print(f"Errore durante l'inserimento: {e}")
        return False

def update_recordSQL(session, nome_tabella, dati_aggiornamento, condizione, args):
    try:
        table_name = get_table_name(session, nome_tabella)
        if not table_name:
            print(f"Errore: La tabella {nome_tabella} non esiste.")
            return False

        with session.begin():
            session.execute(text("PRAGMA foreign_keys = ON"))
            set_clause = ", ".join(f"{key} = :{key}" for key in dati_aggiornamento)
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {condizione}"
            result = session.execute(text(sql), dati_aggiornamento | args)
        return result.rowcount
    except Exception as e:
        session.rollback()
        print(f"Errore durante l'aggiornamento: {e}")
        return False

def delete_recordSQL(session, nome_tabella, condizione, args):
    try:
        table_name = get_table_name(session, nome_tabella)
        if not table_name:
            print(f"Errore: La tabella {nome_tabella} non esiste.")
            return False

        with session.begin():
            session.execute(text("PRAGMA foreign_keys = ON"))
            sql = f"DELETE FROM {table_name} WHERE {condizione}"
            result = session.execute(text(sql), args or {})
            rows_deleted = result.rowcount
        return rows_deleted if rows_deleted > 0 else 0
    except Exception as e:
        session.rollback()
        print(f"Errore durante l'eliminazione: {e}")
        return False

def select_recordsSQL(session, nome_tabella, colonne="*", condizione=None, args=None, ordina_per=None, limite=None):
    try:
        table_name = get_table_name(session, nome_tabella)
        if not table_name:
            print(f"Errore: La tabella {nome_tabella} non esiste.")
            return False

        with session.begin():
            sql = f"SELECT {colonne} FROM {table_name}"
            if condizione:
                sql += f" WHERE {condizione}"
            if ordina_per:
                sql += f" ORDER BY {ordina_per}"
            if limite:
                sql += f" LIMIT {limite}"

            result = session.execute(text(sql), args or {})
            return [dict(row._mapping) for row in result] if result.returns_rows else []
    except Exception as e:
        print(f"Errore durante la selezione: {e}")
        return False

def add_attività_e_scadenziario():
    """
    Aggiunge un'attività e uno scadenziario collegato.
    """
    try:
        # Inserimento dati per l'attività
        print("Inserisci i dati per la nuova attività:")
        nome_attivita = input("Nome attività: ")
        descrizione_attivita = input("Descrizione attività (opzionale): ")

        attivita_data = {
            "Nome": nome_attivita,
            "Descrizione": descrizione_attivita if descrizione_attivita else None
        }

        # Connessione al database
        session = connessione()
        if not session:
            print("Errore di connessione al database.")
            return

        try:
            # Aggiunta dell'attività
            success = add_recordSQL(session, "Attivita", attivita_data)
            if not success:
                print("Errore nell'aggiunta dell'attività.")
                return

            # Recupero dell'ID dell'attività appena aggiunta
            attivita_id = session.execute(text("SELECT last_insert_rowid()")).scalar()

            # Inserimento dati per lo scadenziario
            print("Inserisci i dati per il nuovo scadenziario collegato all'attività:")
            data_schedulazione = datetime.now().strftime("%Y-%m-%d")
            data_esecuzione = input("Data esecuzione (YYYY-MM-DD, opzionale): ")
            data_scadenza = input("Data scadenza (YYYY-MM-DD): ")
            tipo = input("Tipo (Ordinaria, Straordinaria, Urgente): ")
            note = input("Note (opzionale): ")

            scadenziario_data = {
                "ID_Attivita": attivita_id,
                "DataSchedulazione": data_schedulazione,
                "DataEsecuzione": data_esecuzione if data_esecuzione else None,
                "DataScadenza": data_scadenza,
                "Tipo": tipo,
                "Stato": 'Programmata',
                "Note": note if note else None
            }

            # Aggiunta dello scadenziario
            success = add_recordSQL(session, "Scadenziario", scadenziario_data)
            if success:
                print("Attività e scadenziario aggiunti con successo.")
            else:
                print("Errore nell'aggiunta dello scadenziario.")
        finally:
            session.close()
    except Exception as e:
        print(f"Errore imprevisto: {e}")

def select_attività_e_update_scadenziario():
    """
    Seleziona un'attività, stampa i dettagli dello scadenziario e chiede se si desidera aggiornare lo stato in "Completata" o "Annullata".
    Se lo stato viene aggiornato in "Completata", la data di esecuzione verrà aggiornata con la data corrente.
    """
    try:
        with connessione() as session:
            if not session:
                print("Errore di connessione al database.")
                return

            # Seleziona tutte le attività
            attivita = select_recordsSQL(session, "Attivita")
            if not attivita:
                print("Nessuna attività trovata.")
                return

            # Stampa le attività trovate
            print("Attività trovate:")
            for idx, att in enumerate(attivita, start=1):
                print(f"{idx}. ID: {att['ID_Attivita']}, Nome: {att['Nome']}, Descrizione: {att['Descrizione']}")

            # Chiede all'utente di selezionare un'attività
            scelta = int(input("Seleziona l'ID dell'attività: "))
            attivita_scelta = next((att for att in attivita if att['ID_Attivita'] == scelta), None)

            if not attivita_scelta:
                print("Attività non trovata.")
                return

            # Seleziona gli scadenziari collegati all'attività scelta
            scadenziari = select_recordsSQL(session, "Scadenziario", condizione="ID_Attivita = :id", args={"id": attivita_scelta['ID_Attivita']})
            if not scadenziari:
                print("Nessuno scadenziario trovato per l'attività selezionata.")
                return

            # Stampa i dettagli degli scadenziari trovati
            print("Scadenziari trovati:")
            for idx, scad in enumerate(scadenziari, start=1):
                print(f"{idx}. ID: {scad['ID_Scadenziario']}, DataSchedulazione: {scad['DataSchedulazione']}, DataScadenza: {scad['DataScadenza']}, Tipo: {scad['Tipo']}, Stato: {scad['Stato']}, Note: {scad['Note']}")

            # Chiede all'utente di selezionare uno scadenziario
            scelta_scadenziario = int(input("Seleziona l'ID dello scadenziario da aggiornare: "))
            scadenziario_scelto = next((scad for scad in scadenziari if scad['ID_Scadenziario'] == scelta_scadenziario), None)

            if not scadenziario_scelto:
                print("Scadenziario non trovato.")
                return

            # Stampa i dettagli dello scadenziario selezionato
            print(f"Dettagli dello scadenziario selezionato: ID: {scadenziario_scelto['ID_Scadenziario']}, DataSchedulazione: {scadenziario_scelto['DataSchedulazione']}, DataScadenza: {scadenziario_scelto['DataScadenza']}, Tipo: {scadenziario_scelto['Tipo']}, Stato: {scadenziario_scelto['Stato']}, Note: {scadenziario_scelto['Note']}")

            # Chiede se si desidera aggiornare lo stato
            nuovo_stato = input("Vuoi aggiornare lo stato in 'Completata' o 'Annullata'? (C/A): ").strip().upper()
            if nuovo_stato not in ['C', 'A']:
                print("Scelta non valida.")
                return

            stato = "Completata" if nuovo_stato == 'C' else "Annullata"
            data_esecuzione = datetime.now().strftime("%Y-%m-%d") if stato == "Completata" else None

            # Aggiorna lo stato dello scadenziario
            update_data = {"Stato": stato}
            if data_esecuzione:
                update_data["DataEsecuzione"] = data_esecuzione

            condizione = "ID_Scadenziario = :id"
            args = {"id": scadenziario_scelto['ID_Scadenziario']}

            rows_updated = update_recordSQL(session, "Scadenziario", update_data, condizione, args)
            if rows_updated:
                print(f"Stato dello scadenziario aggiornato con successo a '{stato}'.")
            else:
                print("Errore durante l'aggiornamento dello stato dello scadenziario.")
    except Exception as e:
        print(f"Errore imprevisto: {e}")

def invia_notifica_scadenziari():
    """
    Invia una notifica di avviso o allarme se uno o più scadenziari con stato "Programmata"
    hanno una data di scadenza vicina oppure scaduta. Crea un record nella tabella Notifica.
    """
    try:
        with connessione() as session:
            if not session:
                print("Errore di connessione al database.")
                return

            # Seleziona tutti gli scadenziari con stato "Programmata"
            scadenziari = select_recordsSQL(session, "Scadenziario", condizione="Stato = 'Programmata'")
            if not scadenziari:
                print("Nessuno scadenziario trovato con stato 'Programmata'.")
                return

            data_corrente = datetime.now().strftime("%Y-%m-%d")
            notifiche_inviate = 0

            for scadenziario in scadenziari:
                data_scadenza = scadenziario['DataScadenza']
                giorni_rimanenti = (datetime.strptime(data_scadenza, "%Y-%m-%d") - datetime.strptime(data_corrente, "%Y-%m-%d")).days

                if giorni_rimanenti <= 0:
                    tipo_notifica = 'Allarme'
                    messaggio = f"Lo scadenziario ID {scadenziario['ID_Scadenziario']} è scaduto."
                elif giorni_rimanenti <= 7:
                    tipo_notifica = 'Avviso'
                    messaggio = f"Lo scadenziario ID {scadenziario['ID_Scadenziario']} scadrà tra {giorni_rimanenti} giorni."
                else:
                    continue

                notifica_data = {
                    "ID_Scadenziario": scadenziario['ID_Scadenziario'],
                    "DataNotifica": data_corrente,
                    "Tipo": tipo_notifica,
                    "Stato": 'Attivo',
                    "Messaggio": messaggio
                }

                # Aggiunta della notifica
                success = add_recordSQL(session, "Notifica", notifica_data)
                if success:
                    notifiche_inviate += 1
                    print(f"Notifica di tipo '{tipo_notifica}' inviata per lo scadenziario ID {scadenziario['ID_Scadenziario']}. Messaggio: {messaggio}")

            if notifiche_inviate == 0:
                print("Nessuna notifica inviata.")
            else:
                print(f"Totale notifiche inviate: {notifiche_inviate}")

    except Exception as e:
        print(f"Errore imprevisto: {e}")


def Test_menu():
    while True:
        print("\nMenu di Test funzionalità:")
        print("1. Crea database se non esiste")
        print("2. Inizializza tabelle")
        print("3. Aggiungi record")
        print("4. Aggiorna record")
        print("5. Elimina record")
        print("6. Seleziona record")
        print("7. Aggiungi attività e scadenziario")
        print("8. Seleziona e aggiorna attività")
        print("9. Invia notifica scadenziari")
        print("10. Esci")

        choice = input("Inserisci la tua scelta: ")

        try:
            if choice == '1':
                create_database()
            elif choice == '2':
                initSQL()
            elif choice == '3':
                table_name = input("Nome della tabella: ")
                record_data = {}
                while True:
                    column_name = input("Nome colonna (o premi invio per terminare): ")
                    if not column_name:
                        break
                    value = input(f"Valore per {column_name}: ")
                    record_data[column_name] = value

                with connessione() as session:
                    success = add_recordSQL(session, table_name, record_data)
                    if success:
                        print(f"Record aggiunto alla tabella {table_name} con successo.")
                    else:
                        print(f"Errore nell'aggiunta del record alla tabella {table_name}. Controllare la presenza di errori nel log o verificare la correttezza dei dati inseriti.")
            elif choice == '4':
                table_name = input("Nome della tabella: ")
                update_data = {}
                condition_parts = []
                args = {}
                while True:
                    column_name = input("Nome colonna da aggiornare (o premi invio per terminare): ")
                    if not column_name:
                        break
                    value = input(f"Nuovo valore per {column_name}: ")
                    update_data[column_name] = value

                while True:
                    col_cond = input("Condizione per colonna (es. ID_Dipendente=:id, premi invio per terminare): ")
                    if not col_cond:
                        break
                    parts = col_cond.split("=")
                    if len(parts) == 2:
                        condition_parts.append(col_cond)
                        args[parts[1].replace(":", "")] = input(f"Valore per {parts[0].strip()}: ")

                condition = " AND ".join(condition_parts) if condition_parts else None
                if condition is None:
                    condition = input("Condizione WHERE (es. ID_Dipendente='TEC001', premi invio se nessuna condizione):")

                with connessione() as session:
                    rows_updated = update_recordSQL(session, table_name, update_data, condition, args)
                    if rows_updated:
                        print(f"Record aggiornato con successo. Righe aggiornate: {rows_updated}")
                    else:
                        print(f"Errore nell'aggiornamento del record nella tabella {table_name}.")
            elif choice == '5':
                table_name = input("Nome della tabella: ")
                condition_parts = []
                args = {}
                while True:
                    col_cond = input("Condizione per colonna (es. ID_Prodotto=:id, premi invio per terminare): ")
                    if not col_cond:
                        break
                    parts = col_cond.split("=")
                    if len(parts) == 2:
                        condition_parts.append(col_cond)
                        try:
                            args[parts[1].replace(":", "")] = int(input(f"Valore per {parts[0].strip()}: "))
                        except ValueError:
                            args[parts[1].replace(":", "")] = input(f"Valore per {parts[0].strip()}: ")

                condition = " AND ".join(condition_parts) if condition_parts else None
                if condition is None:
                    condition = input("Condizione WHERE (es. ID_Prodotto=1, premi invio se nessuna condizione): ")

                with connessione() as session:
                    rows_deleted = delete_recordSQL(session, table_name, condition, args)
                    if rows_deleted is False:
                        print(f"Errore nell'eliminazione dei record dalla tabella {table_name}.")
                    elif rows_deleted > 0:
                        print(f"Eliminati {rows_deleted} record dalla tabella {table_name}.")
                    else:
                        print(f"Nessun record eliminato dalla tabella {table_name}.")
            elif choice == '6':
                table_name = input("Nome della tabella: ")
                columns = input("Colonne da selezionare (separate da virgole, o * per tutte): ")
                condition = input("Condizione WHERE (opzionale, premi invio per nessuna condizione): ")
                order_by = input("Ordinamento ORDER BY (opzionale, premi invio per nessun ordinamento): ")
                limit = input("Limite LIMIT (opzionale, premi invio per nessun limite): ")

                args = {}
                if condition:
                    if ":id" in condition:
                        args["id"] = int(input("Inserisci l'ID: "))

                with connessione() as session:
                    results = select_recordsSQL(session, table_name, columns, condition, args, order_by, limit)
                    if results:
                        print("\nRisultati:")
                        for record in results:
                            print(record)
                    else:
                        print("Nessun risultato trovato.")
            elif choice == '7':
                add_attività_e_scadenziario()
            elif choice == '8':
                select_attività_e_update_scadenziario()
            elif choice == '9':
                invia_notifica_scadenziari()
            elif choice == '10':
                print("Uscita dal programma. Arrivederci")
                break
            else:
                print("Scelta non valida.")
        except Exception as e:
            print(f"Errore imprevisto: {e}")

if __name__ == '__main__':
    Test_menu()