import mariadb


def connessione(check=False):

    host = '127.0.0.1'
    user = 'root'
    pwd = '1234'
    database = 'hotel'
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

def creaHotel(conn):
    sql = """CREATE TABLE IF NOT EXISTS Hotel(
                hotelID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT, 
                name VARCHAR(45) NOT NULL, 
                address VARCHAR(45) NOT NULL, 
                PRIMARY KEY (hotelID)
        )"""

    return query4db(conn, sql, commit=True)

def creaClienti(conn):
    sql = """CREATE TABLE IF NOT EXISTS Clients(
                clientID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT, 
                firstname VARCHAR(45) NOT NULL, 
                lastname VARCHAR(45) NOT NULL, 
                email VARCHAR(45) NOT NULL, 
                phone CHAR(10), 
                address VARCHAR(45), 
                PRIMARY KEY (clientID)
        )"""

    return query4db(conn, sql, commit=True)



def creaStanze(conn):
    sql = """CREATE TABLE IF NOT EXISTS Rooms(
                roomID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT, 
                room_type VARCHAR(45) NOT NULL, 
                price DECIMAL(6,2) NOT NULL, 
                room_number VARCHAR(45) NOT NULL, 
                hotelID BIGINT(20) UNSIGNED NOT NULL,
                PRIMARY KEY (roomID),
                FOREIGN KEY (hotelID) REFERENCES Hotel(hotelID)
        )"""

    return query4db(conn, sql, commit=True)


def creaGestioneOrdini(conn):
    sql = """CREATE TABLE IF NOT EXISTS Order_Management(
                orderID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,  
                date_booking DATE NOT NULL, 
                date_checkin DATE NOT NULL, 
                date_checkout DATE NOT NULL, 
                payment_method VARCHAR(45) NOT NULL, 
                clientID BIGINT(20) UNSIGNED NOT NULL, 
                roomID BIGINT(20) UNSIGNED NOT NULL, 
                hotelID BIGINT(20) UNSIGNED NOT NULL,
                PRIMARY KEY (orderID), 
                FOREIGN KEY (clientID) REFERENCES Clients(clientID), 
                FOREIGN KEY (roomID) REFERENCES Rooms(roomID),
                FOREIGN KEY (hotelID) REFERENCES Hotel(hotelID)
        )"""

    return query4db(conn, sql, commit=True)


def inizializza(conn):
    # Inizializzo le entità senza FK
    
    creaHotel(conn)
    creaClienti(conn)

    # Inizializzo le altre entità

    creaStanze(conn)
    creaGestioneOrdini(conn)


def createSQL():
    conn = connessione()
    inizializza(conn)
    disconnesione(conn)
    

###############################################################################################################################

def add_Hotel(conn, name, address):
    sql = """INSERT INTO `hotel`.`Hotel`(
                                        `name`,
                                        `address`
                                        )
        VALUES
                (
                %s,
                %s
                );

        """

    args = (name, address, )

    return query4db(conn, sql, args=args, commit=True)
def add_Clienti(conn, firstname, lastname, email, phone, address):
    sql = """INSERT INTO `hotel`.`Clients`(
										`firstname`,
										`lastname`,
										`email`,
										`phone`,
										`address`
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

    args = (firstname, lastname,email, phone, address, )

    return query4db(conn, sql, args=args, commit=True)




def add_Stanze(conn, room_type, price, room_number, hotelID):
    sql = """INSERT INTO `hotel`.`Rooms`(
                                        `room_type`,
                                        `price`,
                                        `room_number`,
                                        `hotelID`
                                        )
		VALUES
				(
				%s,
				%s,
				%s,
                %s
				);

		"""

    args = (room_type, price, room_number, hotelID)

    return query4db(conn, sql, args=args, commit=True)


def add_Gestione_Ordini(conn, date_booking, date_checkin, date_checkout, payment_method, clientID, roomID, hotelID):
    sql = """INSERT INTO `hotel`.`Order_Management`(
                                        `date_booking`,
										`date_checkin`,
										`date_checkout`,
										`payment_method`,
										`clientID`,
										`roomID`,
                                        `hotelID`
                                        )
		VALUES
				(
				%s,
				%s,
				%s,
				%s,
				%s,
				%s,
                %s
				);

		"""

    args = (date_booking, date_checkin, date_checkout, payment_method, clientID, roomID, hotelID)
    return query4db(conn, sql, args=args, commit=True)


def get_booking_date(conn, orderID):
    sql = "SELECT `date_booking` FROM `hotel`.`Order_Management` WHERE `orderID` = %s"
    args = (orderID,)
    return query4db(conn, sql, args=args)[0][0]

def get_checkin_date(conn, orderID):
    sql = "SELECT `date_checkin` FROM `hotel`.`Order_Management` WHERE `orderID` = %s"
    args = (orderID,)
    return query4db(conn, sql, args=args)[0][0]

def get_checkout_date(conn, orderID):
    sql = "SELECT `date_checkout` FROM `hotel`.`Order_Management` WHERE `orderID` = %s"
    args = (orderID,)
    return query4db(conn, sql, args=args)[0][0]

def askSQL():
    
    conn = connessione()
    orderID = 1
    booking = get_booking_date(conn, orderID)
    chekin = get_checkin_date(conn, orderID)
    checkout = get_checkout_date(conn, orderID)
    print(f"Data prenotazione: {booking}")
    print(f"Data check-in: {chekin}")
    print(f"Data check-out: {checkout}")

    """
    get_booking_date(conn, orderID)
    get_checkin_date(conn, orderID)
    get_checkout_date(conn, orderID)
    """
    disconnesione(conn)

def populateSQL():
    
    conn = connessione()
    id_hotel = add_Hotel(conn, 'Hilton', '123 Main St')
    id_clienti = add_Clienti(conn, 'John', 'Doe', 'jdoe@me.com', '1234567890', '123 Second St')
    id_stanze = add_Stanze(conn, 'Single', 100.00, '101', id_hotel)
    add_Gestione_Ordini(conn, '2020-01-01', '2020-01-02', '2020-01-03', 'Credit Card', id_clienti, id_stanze, id_hotel)
    disconnesione(conn)
    

def alterSQL(table_name, column_name, column_type, position=None):
    """
    Modifica una tabella aggiungendo una colonna con il tipo specificato.
    
    Args:
        table_name (str): Nome della tabella da modificare.
        column_name (str): Nome della nuova colonna.
        column_type (str): Tipo della nuova colonna.
        position (str, optional): Posizione della nuova colonna (es. 'AFTER column_name').
    """
    conn = connessione()
    
    sql = f"""ALTER TABLE `{table_name}`
              ADD COLUMN `{column_name}` {column_type}"""
    
    if position:
        sql += f" {position}"
    
    sql += ";"
    
    try:
        query4db(conn, sql, commit=True)
        print(f"Colonna `{column_name}` aggiunta alla tabella `{table_name}`.")
    except mariadb.ProgrammingError as e:
        print(f"Errore nell'aggiunta della colonna `{column_name}`: {e}")
    finally:
        disconnesione(conn)

def dropSQL(tables, if_exists=True):
    """
    Cancella una o più tabelle dal database con gestione dei controlli delle chiavi esterne.
    
    Args:
        tables (str or list): Nome della tabella o lista delle tabelle da eliminare.
        if_exists (bool, optional): Se True, aggiunge la clausola IF EXISTS.
    """
    if isinstance(tables, str):
        tables = [tables]
    
    conn = connessione()
    
    # Disabilita i controlli delle chiavi esterne
    query4db(conn, "SET FOREIGN_KEY_CHECKS = 0;", commit=True)
    
    for table_name in tables:
        if if_exists:
            sql = f"""DROP TABLE IF EXISTS `{table_name}`;"""
        else:
            sql = f"""DROP TABLE `{table_name}`;"""
        
        try:
            query4db(conn, sql, commit=True)
            print(f"Tabella `{table_name}` eliminata.")
        except mariadb.ProgrammingError as e:
            print(f"Errore nell'eliminazione della tabella `{table_name}`: {e}")
    
    # Riabilita i controlli delle chiavi esterne
    query4db(conn, "SET FOREIGN_KEY_CHECKS = 1;", commit=True)
    
    disconnesione(conn)




if __name__ == '__main__':
    #createSQL()
    populateSQL()
    #askSQL()
    #alterSQL()
    #dropSQL(['hotel', 'clients', 'rooms', 'order_management'])


