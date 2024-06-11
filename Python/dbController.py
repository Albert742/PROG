import mariadb


def connessione(check=False):

    host = '127.0.0.1'
    user = 'root'
    pwd = '1234'
    database = 'lezione'
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
    """
    Deconnects to the Ismett database.
	"""

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



def creaPaziente(conn):
    sql = """CREATE TABLE IF NOT EXISTS Patient(
                patientID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT, 
                date_of_birth CHAR(10) NOT NULL, 
                gender CHAR(1) NOT NULL, 
                PRIMARY KEY (patientID)
        )"""

    return query4db(conn, sql, commit=True)



def creaEsercizi(conn):
    sql = """CREATE TABLE IF NOT EXISTS Exercise(
                exerciseID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT, 
                mywellness_id VARCHAR(450) NOT NULL, 
                exercise_name VARCHAR(450) NOT NULL, 
                exercise_type VARCHAR(45), 
                equipment_name VARCHAR(45), 
                equipment_type VARCHAR(45), 
                cardio BOOLEAN, 
                PRIMARY KEY (exerciseID)
        )"""

    return query4db(conn, sql, commit=True)


def creaAttivitaFisica(conn):
    sql = """CREATE TABLE IF NOT EXISTS Physical_Activity(
                physical_activityID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,  
                duration INT NOT NULL, 
                calories INT NOT NULL, 
                date_exercise CHAR(10) NOT NULL,
                patientID BIGINT(20) UNSIGNED NOT NULL, 
                exerciseID BIGINT(20) UNSIGNED NOT NULL, 
                PRIMARY KEY (physical_activityID), 
                FOREIGN KEY (patientID) REFERENCES Patient(patientID), 
                FOREIGN KEY (exerciseID) REFERENCES Exercise(exerciseID)
        )"""

    return query4db(conn, sql, commit=True)


def inizializza(conn):
    # Inizializzo le entità senza FK

    creaPaziente(conn)
    creaEsercizi(conn)

    # Inizializzo le altre entità
    creaAttivitaFisica(conn)


def createSQL():
    conn = connessione()
    inizializza(conn)
    disconnesione(conn)


###############################################################################################################################

def add_patient(conn, demetrixCode, data_arruolamento, data_Nascita, genere):
    sql = """INSERT INTO `ISMETT_PRENCD`.`Patient`(
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




def add_esercizi(conn, mywellness_id, exercise_name, exercise_type, equipment_name, equipment_type, cardio):
    sql = """INSERT INTO `ISMETT_PRENCD`.`Exercise`(
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


def add_Attivita_Fisica(conn, Durata, Caloria, Data, Trial, Trial_Giorno, PazienteID, EserciziID):
    sql = """INSERT INTO `ISMETT_PRENCD`.`Physical_Activity`(
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

    args = (Durata, Caloria, Data, Trial, Trial_Giorno, PazienteID, EserciziID, )

    return query4db(conn, sql, args=args, commit=True)




def populateSQL():
    pass



if __name__ == '__main__':
    createSQL()