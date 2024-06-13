import mariadb


def connessione(check=False):

    host = '127.0.0.1'
    user = 'root'
    pwd = '1234'
    database = 'test'
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
                PRIMARY KEY (roomID)
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
                PRIMARY KEY (orderID), 
                FOREIGN KEY (clientID) REFERENCES Clients(clientID), 
                FOREIGN KEY (roomID) REFERENCES Rooms(roomID)
        )"""

    return query4db(conn, sql, commit=True)


def inizializza(conn):
    # Inizializzo le entità senza FK

    creaClienti(conn)
    creaStanze(conn)

    # Inizializzo le altre entità
    creaGestioneOrdini(conn)


def createSQL():
    conn = connessione()
    inizializza(conn)
    disconnesione(conn)
    

###############################################################################################################################

def add_Clienti(conn, firstname, lastname, email, phone, address):
    sql = """INSERT INTO `test`.`Clients`(
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

    args = (firstname, lastname, email, phone, address, )

    return query4db(conn, sql, args=args, commit=True)




def add_Stanze(conn, room_type, price, room_number):
    sql = """INSERT INTO `test`.`Rooms`(
                                        `room_type`,
                                        `price`,
                                        `room_number`
                                        )
		VALUES
				(
				%s,
				%s,
				%s
				);

		"""

    args = (room_type, price, room_number, )

    return query4db(conn, sql, args=args, commit=True)


def add_Gestione_Ordini(conn, date_booking, date_checkin, date_checkout, payment_method, clientID, roomID):
    sql = """INSERT INTO `test`.`Order_Management`(
                                        `date_booking`,
										`date_checkin`,
										`date_checkout`,
										`payment_method`,
										`clientID`,
										`roomID`
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

    args = (date_booking, date_checkin, date_checkout, payment_method, clientID, roomID)
    return query4db(conn, sql, args=args, commit=True)


def get_booking_date(conn, orderID):
    sql = "SELECT `date_booking` FROM `test`.`Order_Management` WHERE `orderID` = %s"
    args = (orderID,)
    return query4db(conn, sql, args=args)[0][0]

def get_checkin_date(conn, orderID):
    sql = "SELECT `date_checkin` FROM `test`.`Order_Management` WHERE `orderID` = %s"
    args = (orderID,)
    return query4db(conn, sql, args=args)[0][0]

def get_checkout_date(conn, orderID):
    sql = "SELECT `date_checkout` FROM `test`.`Order_Management` WHERE `orderID` = %s"
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
    id_clienti = add_Clienti(conn, 'John', 'Doe', 'jdoe@me.com', '1234567890', '123 Main St')
    id_stanze = add_Stanze(conn, 'Single', 100.00, '101')
    add_Gestione_Ordini(conn, '2020-01-01', '2020-01-02', '2020-01-03', 'Credit Card', id_clienti, id_stanze)
    disconnesione(conn)
    

def alterSQL():
    pass



def dropSQL():
    pass


if __name__ == '__main__':
    #createSQL()
    #populateSQL()
    askSQL()
