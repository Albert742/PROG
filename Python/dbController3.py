import mariadb
from datetime import datetime

def connessione(**kwargs):
    """
    Connessione al database con configurazione tramite kwargs.
    """
    default_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '1234',
        'database': 'negozio',
        'port': 3307
    }
    config = {**default_config, **kwargs}
    conn = mariadb.connect(**config)
    conn.auto_reconnect = True
    return conn

def query4db(conn, sql, args=None, commit=False):
    """
    Esegue una query sul database.
    """
    with conn.cursor() as cursore:
        cursore.execute(sql, args or ())
        if commit:
            conn.commit()
            return cursore.lastrowid
        else:
            return cursore.fetchall()

def crea_tabella(conn, nome_tabella, definizione):
    """
    Crea una tabella nel database se non esiste.
    """
    sql = f"CREATE TABLE IF NOT EXISTS `{nome_tabella}` ({definizione})"
    return query4db(conn, sql, commit=True)


def inizializza(conn):
    tabelle = {
        "Category": """
            categoryID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
            category VARCHAR(45) NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (categoryID)
        """,
        "Supplier": """
            supplierID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(45) NOT NULL,
            address VARCHAR(45) NOT NULL,
            phone VARCHAR(15),4
            email VARCHAR(45),
            PRIMARY KEY (supplierID)
        """,
        "Product": """
            productID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(45) NOT NULL,
            SKU VARCHAR(45) UNIQUE NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            description TEXT,
            added_on DATE,
            categoryID BIGINT(20) UNSIGNED NOT NULL,
            PRIMARY KEY (productID),
            FOREIGN KEY (categoryID) REFERENCES Category(categoryID)
        """,
        "Customer": """
            customerID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
            firstname VARCHAR(45) NOT NULL,
            lastname VARCHAR(45) NOT NULL,
            email VARCHAR(45) NOT NULL,
            phone CHAR(10),
            address VARCHAR(100),
            birthdate DATE,
            registered_on DATE,
            PRIMARY KEY (customerID)
        """,
        "Orders": """
            orderID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
            date DATE NOT NULL,
            status VARCHAR(20) DEFAULT 'Pending',
            total DECIMAL(10,2),
            customerID BIGINT(20) UNSIGNED NOT NULL,
            PRIMARY KEY (orderID),
            FOREIGN KEY (customerID) REFERENCES Customer(customerID)
        """,
        "Inventory": """
            inventoryID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
            productID BIGINT(20) UNSIGNED NOT NULL,
            supplierID BIGINT(20) UNSIGNED NOT NULL,
            quantity INT(11) NOT NULL,
            supply_price DECIMAL(10,2),
            updated_on DATE,
            PRIMARY KEY (inventoryID),
            FOREIGN KEY (productID) REFERENCES Product(productID),
            FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID)
        """,
        "Order_Item": """
            orderItemID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
            orderID BIGINT(20) UNSIGNED NOT NULL,
            productID BIGINT(20) UNSIGNED NOT NULL,
            quantity INT(11) NOT NULL,
            unit_price DECIMAL(10,2),
            PRIMARY KEY (orderItemID),
            FOREIGN KEY (orderID) REFERENCES Orders(orderID),
            FOREIGN KEY (productID) REFERENCES Product(productID)
        """
    }

    for nome_tabella, definizione in tabelle.items():
        crea_tabella(conn, nome_tabella, definizione)

def add_record(conn, table, fields, values):
    """
    Aggiunge un record a una tabella specificata.
    """
    placeholders = ', '.join(['%s'] * len(values))
    sql = f"INSERT INTO `{table}` ({', '.join(fields)}) VALUES ({placeholders})"
    return query4db(conn, sql, args=values, commit=True)

def createSQL():
    with connessione() as conn:
        inizializza(conn)

def populateSQL():
    with connessione() as conn:
        # Categorie
        categorie = [
            ('CPU', 'Unità di Elaborazione Centrale'),
            ('GPU', 'Unità di Elaborazione Grafica'),
            ('Scheda Madre', 'Schede madri per vari chipset'),
            ('RAM', 'Moduli di Memoria ad Accesso Casuale'),
            ('Archiviazione', 'Dispositivi SSD e HDD'),
            ('Alimentatore', 'Unità di alimentazione per PC'),
            ('Case', 'Case per PC di diverse dimensioni'),
            ('Raffreddamento', 'Soluzioni di raffreddamento per CPU e case'),
            ('Accessori', 'Accessori e periferiche per PC')
        ]
        categoria_ids = [add_record(conn, 'Category', ['category', 'description'], cat) for cat in categorie]

        # Fornitori
        fornitori = [
            ('Fornitori Intel', '123 Intel St', '1234567890', 'fornitori_intel@example.com'),
            ('Distributori AMD', '456 AMD Ave', '0987654321', 'distributori_amd@example.com'),
            ('Partner NVIDIA', '789 NVIDIA Blvd', '1231231234', 'partner_nvidia@example.com'),
            ('Fornitori Corsair', '101 Corsair Rd', '3213214321', 'fornitori_corsair@example.com'),
            ('Western Digital', '202 WD St', '5432109876', 'wd@example.com')
        ]
        fornitore_ids = [add_record(conn, 'Supplier', ['name', 'address', 'phone', 'email'], forn) for forn in fornitori]

        # Prodotti
        prodotti = [
            ('Intel Core i9-13900K', 600.00, categoria_ids[0], 'CPU-13900K', 'Intel Core i9 di 13a generazione, 24 core', '2024-01-15'),
            ('AMD Ryzen 9 7950X', 550.00, categoria_ids[0], 'CPU-7950X', 'AMD Ryzen 9, 16 core', '2024-01-10'),
            ('NVIDIA RTX 4090', 1500.00, categoria_ids[1], 'GPU-4090', 'NVIDIA GeForce RTX 4090, 24GB', '2024-01-12'),
            ('Corsair Vengeance 32GB DDR5', 200.00, categoria_ids[3], 'RAM-32GBDDR5', '32GB di RAM DDR5, 5200MHz', '2024-01-08'),
            ('Samsung 980 Pro 1TB', 150.00, categoria_ids[4], 'SSD-980PRO1TB', 'SSD NVMe da 1TB', '2024-01-05'),
            ('MSI MPG Z790', 300.00, categoria_ids[2], 'MB-MPGZ790', 'Scheda Madre MSI MPG Z790', '2024-01-07'),
            ('Corsair RM850x', 130.00, categoria_ids[5], 'PSU-RM850x', 'Alimentatore completamente modulare da 850W', '2024-01-09'),
            ('NZXT H510', 100.00, categoria_ids[6], 'CASE-H510', 'Case Mid-Tower ATX', '2024-01-06'),
            ('Noctua NH-D15', 100.00, categoria_ids[7], 'COOL-NHD15', 'Dissipatore CPU a doppia torre', '2024-01-11'),
            ('Logitech G502', 50.00, categoria_ids[8], 'ACC-G502', 'Mouse da gioco', '2024-01-04')
        ]
        prodotto_ids = [add_record(conn, 'Product', ['name', 'price', 'categoryID', 'SKU', 'description', 'added_on'], prod) for prod in prodotti]

        # Clienti
        clienti = [
            ('Giovanni', 'Rossi', 'giovanni.rossi@example.com', '1234567890', 'Via Roma, 123', '1980-05-15', '2024-01-01'),
            ('Maria', 'Bianchi', 'maria.bianchi@example.com', '0987654321', 'Via Milano, 456', '1990-08-20', '2024-01-02'),
            ('Alice', 'Verdi', 'alice.verdi@example.com', '1231231234', 'Via Torino, 789', '1985-11-30', '2024-01-03'),
            ('Roberto', 'Neri', 'roberto.neri@example.com', '3213214321', 'Via Napoli, 101', '1975-02-25', '2024-01-04'),
            ('Carlo', 'Gialli', 'carlo.gialli@example.com', '5432109876', 'Via Firenze, 202', '2000-07-10', '2024-01-05')
        ]
        cliente_ids = [add_record(conn, 'Customer', ['firstname', 'lastname', 'email', 'phone', 'address', 'birthdate', 'registered_on'], cli) for cli in clienti]

        # Ordini
        ordini = [
            ('2024-01-15', cliente_ids[0], 'Completato', 1200.00),
            ('2024-01-16', cliente_ids[1], 'In Attesa', 1500.00),
            ('2024-01-17', cliente_ids[2], 'Spedito', 600.00),
            ('2024-01-18', cliente_ids[3], 'Completato', 550.00),
            ('2024-01-19', cliente_ids[4], 'In Lavorazione', 100.00)
        ]
        ordine_ids = [add_record(conn, 'Orders', ['date', 'customerID', 'status', 'total'], ord) for ord in ordini]

        # Articoli dell'Ordine
        ordini_prodotti = [
            (ordine_ids[0], prodotto_ids[0], 1, 600.00),
            (ordine_ids[1], prodotto_ids[2], 1, 1500.00),
            (ordine_ids[2], prodotto_ids[1], 1, 550.00),
            (ordine_ids[3], prodotto_ids[5], 1, 300.00),
            (ordine_ids[4], prodotto_ids[7], 1, 100.00),
            (ordine_ids[0], prodotto_ids[3], 1, 200.00),
            (ordine_ids[1], prodotto_ids[8], 1, 100.00),
        ]
        [add_record(conn, 'Order_Item', ['orderID', 'productID', 'quantity', 'unit_price'], op) for op in ordini_prodotti]

        # Inventario
        inventario = [
            (prodotto_ids[0], fornitore_ids[0], 50, 500.00, '2024-01-16'),
            (prodotto_ids[1], fornitore_ids[1], 30, 450.00, '2024-01-17'),
            (prodotto_ids[2], fornitore_ids[2], 20, 1300.00, '2024-01-18'),
            (prodotto_ids[3], fornitore_ids[3], 100, 180.00, '2024-01-19'),
            (prodotto_ids[4], fornitore_ids[4], 70, 130.00, '2024-01-20'),
            (prodotto_ids[5], fornitore_ids[3], 40, 250.00, '2024-01-21'),
            (prodotto_ids[6], fornitore_ids[3], 60, 100.00, '2024-01-22'),
            (prodotto_ids[7], fornitore_ids[4], 80, 80.00, '2024-01-23'),
            (prodotto_ids[8], fornitore_ids[2], 90, 90.00, '2024-01-24'),
            (prodotto_ids[9], fornitore_ids[1], 120, 45.00, '2024-01-25')
        ]
        [add_record(conn, 'Inventory', ['productID', 'supplierID', 'quantity', 'supply_price', 'updated_on'], inv) for inv in inventario]

# Funzioni per ottenere i dettagli dell'ordine

def get_order_date(conn, orderID):
    sql = "SELECT `date` FROM `Orders` WHERE `orderID` = %s"
    args = (orderID,)
    return query4db(conn, sql, args=args)[0][0]

def get_order_status(conn, orderID):
    sql = "SELECT `status` FROM `Orders` WHERE `orderID` = %s"
    args = (orderID,)
    return query4db(conn, sql, args=args)[0][0]

def get_order_total(conn, orderID):
    sql = "SELECT `total` FROM `Orders` WHERE `orderID` = %s"
    args = (orderID,)
    return query4db(conn, sql, args=args)[0][0]

# Funzione principale per richiedere e stampare i dettagli dell'ordine

def askSQL():
    conn = connessione()
    orderID = 1
    order_date = get_order_date(conn, orderID)
    order_status = get_order_status(conn, orderID)
    order_total = get_order_total(conn, orderID)

    print(f"Data dell'ordine: {order_date}")
    print(f"Stato dell'ordine: {order_status}")
    print(f"Totale dell'ordine: {order_total}")

def alterSQL(table_name, column_name, column_type, position=None):
    """
    Aggiunge una colonna a una tabella esistente.
    """
    with connessione() as conn:
        sql = f"ALTER TABLE `{table_name}` ADD COLUMN `{column_name}` {column_type}"
        if position:
            sql += f" {position}"
        query4db(conn, sql, commit=True)

def dropSQL(tables, if_exists=True):
    """
    Elimina una o più tabelle dal database.
    """
    if isinstance(tables, str):
        tables = [tables]
    with connessione() as conn:
        query4db(conn, "SET FOREIGN_KEY_CHECKS = 0;", commit=True)
        for table_name in tables:
            sql = f"DROP TABLE IF EXISTS `{table_name}`;" if if_exists else f"DROP TABLE `{table_name}`;"
            query4db(conn, sql, commit=True)
        query4db(conn, "SET FOREIGN_KEY_CHECKS = 1;", commit=True)

if __name__ == '__main__':
    #createSQL()
    #populateSQL()
    askSQL()
    #alterSQL('Product', 'new_column', 'VARCHAR(50)')
    #dropSQL(['Product', 'Customer', 'Orders', 'Order_Item', 'Category', 'Supplier', 'Inventory'])
