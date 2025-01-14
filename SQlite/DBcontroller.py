from sqlalchemy import create_engine, text, insert, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, IntegrityError
import time
import toml

def connessione():
    """
    Esegue la connessione al database SQLite specificato nel file secrets.toml
    e restituisce un oggetto Session per l'interazione con il database.

    Se la connessione non riesce dopo 3 tentativi, restituisce None.
    """

    toml_data = toml.load(".loc/DBloc.toml")
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
    toml_data = toml.load("C:/Users/alber/Desktop/SQlite/Location/DBloc.toml")
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
    Inizializza le tabelle del database.
    """
    tabelle = {
        "Attivita": """
            ID_Attivita INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL
        """,
        "Scadenziario": """
            ID_Scadenziario INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Attivita INTEGER NOT NULL,
            DataSchedulazione TEXT NOT NULL CHECK(datetime(DataSchedulazione) IS NOT NULL),
            DataEsecuzione TEXT CHECK(datetime(DataEsecuzione) IS NOT NULL OR DataEsecuzione IS NULL),
            DataScadenza TEXT NOT NULL CHECK(datetime(DataScadenza) IS NOT NULL),            
            Tipo TEXT NOT NULL CHECK(Tipo IN ('Ordinaria', 'Straordinaria', 'Urgente')),
            Stato TEXT DEFAULT 'Programmata' CHECK(Stato IN ('Programmata', 'Completata', 'Annullata')),
            Note TEXT,
            FOREIGN KEY (ID_Attivita) REFERENCES Attivita(ID_Attivita) ON DELETE CASCADE
        """,
        "Allarmi": """
            ID_Allarme INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Scadenziario INTEGER NOT NULL,
            DataAllarme TEXT NOT NULL CHECK(datetime(DataAllarme) IS NOT NULL),
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

        with session.begin():
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



def Test_menu():
    while True:
        print("\nMenu di Test funzionalità:")
        print("1. Crea database se non esiste")
        print("2. Inizializza tabelle")
        print("3. Aggiungi record")
        print("4. Aggiorna record")
        print("5. Elimina record")
        print("6. Seleziona record")
        print("7. Esci")

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
                print("Uscita dal programma. Arrivederci")
                break
            else:
                print("Scelta non valida.")
        except Exception as e:
            print(f"Errore imprevisto: {e}")

if __name__ == '__main__':
    Test_menu()