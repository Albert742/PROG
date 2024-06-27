import mariadb
import sys

def connessione():
    try:
        conn = mariadb.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='negozio',
            port=3306
        )
        cursor = conn.cursor()
        return cursor, conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

def disconnessione(conn):
    cursor, db = conn
    cursor.close()
    db.close()

def query4db(conn, sql, args=None, commit=False):
    cursor, db = conn
    try:
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        
        if commit:
            db.commit()
            return cursor.lastrowid
        else:
            return cursor.fetchall()
    except mariadb.Error as e:
        print(f"Error: {e}")
        return None

def create_database_and_tables():
    cursor, conn = connessione()
    
    queries = [
        "CREATE DATABASE IF NOT EXISTS ComputerStore;",
        "USE ComputerStore;",
        """CREATE TABLE IF NOT EXISTS Category (
            categoryID INT AUTO_INCREMENT,
            category_name VARCHAR(255) NOT NULL,
            PRIMARY KEY (categoryID)
        );""",
        """CREATE TABLE IF NOT EXISTS Supplier (
            supplierID INT AUTO_INCREMENT,
            supplier_name VARCHAR(255) NOT NULL,
            contact_name VARCHAR(255),
            contact_email VARCHAR(255),
            contact_phone VARCHAR(20),
            PRIMARY KEY (supplierID)
        );""",
        """CREATE TABLE IF NOT EXISTS Product (
            productID INT AUTO_INCREMENT,
            product_name VARCHAR(255) NOT NULL,
            categoryID INT,
            supplierID INT,
            price DECIMAL(10, 2) NOT NULL,
            stock INT NOT NULL,
            description TEXT,
            PRIMARY KEY (productID),
            FOREIGN KEY (categoryID) REFERENCES Category(categoryID),
            FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID)
        );""",
        """CREATE TABLE IF NOT EXISTS Customer (
            customerID INT AUTO_INCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(20),
            address VARCHAR(255),
            city VARCHAR(255),
            postal_code VARCHAR(10),
            country VARCHAR(255),
            PRIMARY KEY (customerID)
        );""",
        """CREATE TABLE IF NOT EXISTS `Order` (
            orderID INT AUTO_INCREMENT,
            order_date DATE NOT NULL,
            customerID INT,
            total_amount DECIMAL(10, 2) NOT NULL,
            status VARCHAR(50) NOT NULL,
            PRIMARY KEY (orderID),
            FOREIGN KEY (customerID) REFERENCES Customer(customerID)
        );""",
        """CREATE TABLE IF NOT EXISTS OrderItem (
            orderItemID INT AUTO_INCREMENT,
            orderID INT,
            productID INT,
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            PRIMARY KEY (orderItemID),
            FOREIGN KEY (orderID) REFERENCES `Order`(orderID),
            FOREIGN KEY (productID) REFERENCES Product(productID)
        );""",
        """CREATE TABLE IF NOT EXISTS Inventory (
            inventoryID INT AUTO_INCREMENT,
            productID INT,
            stock INT NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (inventoryID),
            FOREIGN KEY (productID) REFERENCES Product(productID)
        );"""
    ]
    
    for query in queries:
        query4db((cursor, conn), query, commit=True)
    
    disconnessione((cursor, conn))

if __name__ == '__main__':
    create_database_and_tables()
