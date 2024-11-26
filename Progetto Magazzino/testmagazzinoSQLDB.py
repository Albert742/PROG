import mariadb


def connessione(check=False):

    host = '127.0.0.1'
    user = 'root'
    pwd = '1234'
    database = 'testmagazzino'
    port = 3307

    # Connessione al db
    db = mariadb.connect(host=host, user=user, passwd=pwd, db=database, port=port)

    db.auto_reconnect = True

    # Ottenimento del cursore
    cursor = db.cursor()

    if check:
        # Esecuzione della query SQL interrogazione versione
        sql = "SELECT VERSION()"
        cursor.execute(sql)

        # Lettura di una singola riga dei risultati della query
        data = cursor.fetchone()
        print("Connecting to the %s database." % database)
        print("Database version : %s " % data)
        print()

    return cursor, db


def disconnesione(conn):

    # Chiusura della connessione

    cursore, db = conn
    cursore.close()
    db.close()


def query4db(conn, sql, args=None, commit=False):
    """
    Performs a query to the database.

    RETURN the db answer.
    """
    cursore, db = conn

    # Lettura dei risultati
    # Esecuzione della query
    if args is None:
        cursore.execute(sql)
    else:
        cursore.execute(sql, args)

    if commit:
        db.commit()
        results = cursore.lastrowid
    else:
        # Risultati della query
        results = cursore.fetchall()

    return results



def creaProdotti(conn):
    sql = """CREATE TABLE IF NOT EXISTS Prodotti(
                ID_Prodotto INT PRIMARY KEY AUTO_INCREMENT,
                Nome VARCHAR(255) NOT NULL,
                Produttore VARCHAR(255),
                Tipo ENUM('Alimentare', 'Farmaceutico') NOT NULL,
                UnitaMisura VARCHAR(50)
        )"""

    return query4db(conn, sql, commit=True)


def creaLotti(conn):
    sql = """CREATE TABLE IF NOT EXISTS Lotti(
                ID_Lotto INT PRIMARY KEY AUTO_INCREMENT,
                ID_Prodotto INT,
                Lotto VARCHAR(255),
                Scadenza DATE,
                Quantita INT,
                PrezzoAcquisto DECIMAL(10, 2),
                Zona VARCHAR(255),
                Scaffalatura VARCHAR(255),
                DataRicevimento DATE,
                PosizioneRobot VARCHAR(255),
                Stato ENUM('Disponibile', 'In transito', 'Prenotato'),
                FOREIGN KEY (ID_Prodotto) REFERENCES Prodotti(ID_Prodotto)
        )"""

    return query4db(conn, sql, commit=True)


def creaAlimentari(conn):
    sql = """CREATE TABLE IF NOT EXISTS Alimentari(
                ID_Prodotto INT PRIMARY KEY,
                Allergeni TEXT,
                FOREIGN KEY (ID_Prodotto) REFERENCES Prodotti(ID_Prodotto)
        )"""

    return query4db(conn, sql, commit=True)


def creaFarmaceutici(conn):
    sql = """CREATE TABLE IF NOT EXISTS Farmaceutici(
                ID_Prodotto INT PRIMARY KEY,
                PrincipioAttivo VARCHAR(255),
                FOREIGN KEY (ID_Prodotto) REFERENCES Prodotti(ID_Prodotto)
        )"""

    return query4db(conn, sql, commit=True)

def creaFornitori(conn):
    sql = """CREATE TABLE IF NOT EXISTS Fornitori(
                ID_Fornitore INT PRIMARY KEY AUTO_INCREMENT,
                Nome VARCHAR(255) NOT NULL,
                Indirizzo VARCHAR(255),
                Telefono VARCHAR(20),
                Email VARCHAR(255)
        )"""

    return query4db(conn, sql, commit=True)

def creaClienti(conn):
    sql = """CREATE TABLE IF NOT EXISTS Clienti(
                ID_Cliente INT PRIMARY KEY AUTO_INCREMENT,
                Nome VARCHAR(255) NOT NULL,
                Cognome VARCHAR(255),
                Indirizzo VARCHAR(255),
                Telefono VARCHAR(20),
                Email VARCHAR(255)
        )"""

    return query4db(conn, sql, commit=True)

def creaOrdini(conn):
    sql = """CREATE TABLE IF NOT EXISTS Ordini(
                ID_Ordine INT PRIMARY KEY AUTO_INCREMENT,                
                ID_Cliente INT,
                ID_Lotto INT,
                ID_Fornitore INT,
                Tipo ENUM('Entrata', 'Uscita') NOT NULL
                DataOrdine DATE,
                FOREIGN KEY (ID_Cliente) REFERENCES Clienti(ID_Cliente),
                FOREIGN KEY (ID_Fornitore) REFERENCES Fornitori(ID_Fornitore)
        )"""




def inizializza(conn):
    # Inizializzo le entità senza FK

    creaProdotti(conn)
    creaLotti(conn)
    creaAlimentari(conn)


def createSQL():
    conn = connessione()
    inizializza(conn)
    disconnesione(conn)


###############################################################################################################################

def add_Paziente(conn, data_Nascita, genere):
    sql = """INSERT INTO `lezione`.`Patient`(
										`date_of_birth`,
										`gender`
                                        )
		VALUES
				(
				%s,
				%s
				);

		"""

    args = (data_Nascita,genere, )

    return query4db(conn, sql, args=args, commit=True)




def add_Esercizi(conn, mywellness_id, exercise_name, exercise_type, equipment_name, equipment_type, cardio):
    sql = """INSERT INTO `lezione`.`Exercise`(
                                        `mywellness_id`,
                                        `exercise_name`,
                                        `exercise_type`,
                                        `equipment_name`,
                                        `equipment_type`,
                                        `cardio`
                                        )
		VALUES
				(
				%s,
				%s,
				%s,
				%s,
				%s,
				%s
				);

		"""

    args = (mywellness_id, exercise_name, exercise_type, equipment_name, equipment_type, cardio, )

    return query4db(conn, sql, args=args, commit=True)


def add_Attivita_Fisica(conn, Durata, Caloria, Data, PazienteID, EserciziID):
    sql = """INSERT INTO `lezione`.`Physical_Activity`(
                                        `duration`,
										`calories`,
										`date_exercise`,
										`patientID`,
										`exerciseID`
                                        )
		VALUES
				(
				%s,
				%s,
				%s,
				%s,
				%s
				);

		"""

    args = (Durata, Caloria, Data, PazienteID, EserciziID, )

    return query4db(conn, sql, args=args, commit=True)


def get_DataNascita(conn, patientID):
    sql = "SELECT `date_of_birth` FROM `lezione`.`Patient` WHERE `patientID` = %s"
    args = (patientID,)
    return query4db(conn, sql, args=args)[0][0]

def get_all_DataNascita(conn):
    sql = "SELECT `date_of_birth` FROM `lezione`.`Patient`"
    return query4db(conn, sql)


def get_all_PatientInfo(conn, PazienteID):
    sql = "SELECT * FROM `lezione`.`Patient` WHERE `patientID` = %s"
    args = (PazienteID,)
    return query4db(conn, sql, args=args)

def askSQL():
    conn = connessione()
    patientID = 3
    #data_nascita = get_DataNascita(conn, patientID)
    "get_DataNascita(conn, patientID)"
    #print(f"Data nascita: {data_nascita}")
    dati_paziente = get_all_PatientInfo(conn, patientID)
    print(f"Dati paziente: {dati_paziente}")
    #date_nascita = get_all_DataNascita(conn)
    #print(f"Date nascita: {date_nascita}")
    disconnesione(conn)


def populateSQL():
    conn = connessione()
    id_paziente = add_Paziente(conn, '01/02/1995', 'F')
    id_esercizio = add_Esercizi(conn, '3', 'peso', 'gerarchico', 'ganci', 'palestra', False)
    add_Attivita_Fisica(conn, 75, 150, '22/06/2024', id_paziente, id_esercizio)
    disconnesione(conn)



if __name__ == '__main__':
    #createSQL()
    #populateSQL()
    askSQL()