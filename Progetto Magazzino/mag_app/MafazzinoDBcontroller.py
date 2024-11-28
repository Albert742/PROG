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
        'database': 'magazzino',
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
        # Gestione prodotti e fornitori
        "Fornitori": """
            ID_Fornitore INT PRIMARY KEY AUTO_INCREMENT,
            Nome VARCHAR(255) NOT NULL,
            Indirizzo VARCHAR(255),
            Telefono VARCHAR(20),
            Email VARCHAR(255),
            PartitaIVA VARCHAR(20) UNIQUE NOT NULL
        """,
        "Prodotti": """
            ID_Prodotto INT PRIMARY KEY AUTO_INCREMENT,
            ID_Fornitore INT,
            Nome VARCHAR(255) NOT NULL,
            Produttore VARCHAR(255),
            Tipo ENUM('Alimentare', 'Farmaceutico') NOT NULL,
            UnitaMisura VARCHAR(50),
            UNIQUE(Nome, Produttore),
            FOREIGN KEY (ID_Fornitore) REFERENCES Fornitori(ID_Fornitore) ON DELETE SET NULL
        """,
        # Gestione magazzino e lotti
        "Zone": """
            ID_Zona INT PRIMARY KEY AUTO_INCREMENT,
            Nome VARCHAR(255) NOT NULL,
            Tipo ENUM('Stoccaggio_Alimentari', 'Stoccaggio_Farmaceutici', 'Carico', 'Scarico') NOT NULL,
            Descrizione TEXT
        """,
        "Scaffalature": """
            ID_Scaffalatura INT PRIMARY KEY AUTO_INCREMENT,
            ID_Zona INT NOT NULL,
            Nome VARCHAR(255) NOT NULL,
            Capacita INT,
            FOREIGN KEY (ID_Zona) REFERENCES Zone(ID_Zona) ON DELETE CASCADE
        """,
        "Lotti": """
            ID_Lotto INT PRIMARY KEY AUTO_INCREMENT,
            ID_Prodotto INT NOT NULL,
            ID_Zona INT NOT NULL,
            ID_Scaffalatura INT NOT NULL,
            Lotto VARCHAR(255),
            Scadenza DATE,
            Quantita INT,
            PrezzoAcquisto DECIMAL(10, 2),
            DataRicevimento DATE,
            Stato ENUM('Disponibile', 'In transito', 'Prenotato') DEFAULT 'Disponibile',
            FOREIGN KEY (ID_Prodotto) REFERENCES Prodotti(ID_Prodotto) ON DELETE CASCADE,
            FOREIGN KEY (ID_Zona) REFERENCES Zone(ID_Zona) ON DELETE CASCADE,
            FOREIGN KEY (ID_Scaffalatura) REFERENCES Scaffalature(ID_Scaffalatura) ON DELETE CASCADE,
            UNIQUE (ID_Prodotto, Lotto)
        """,
        # Gestione clienti e ordini
        "Clienti": """
            ID_Cliente INT PRIMARY KEY AUTO_INCREMENT,
            Nome VARCHAR(255) NOT NULL,
            Indirizzo VARCHAR(255),
            Telefono VARCHAR(20),
            Email VARCHAR(255),
            PartitaIVA VARCHAR(20) UNIQUE NOT NULL
        """,
        "Ordini": """
            ID_Ordine INT PRIMARY KEY AUTO_INCREMENT,
            DataOrdine TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            Tipo ENUM('Entrata', 'Uscita') NOT NULL,
            ID_Fornitore INT,
            ID_Cliente INT,
            Stato ENUM('In elaborazione', 'Spedito', 'Concluso') DEFAULT 'In elaborazione',
            FOREIGN KEY (ID_Fornitore) REFERENCES Fornitori(ID_Fornitore) ON DELETE SET NULL,
            FOREIGN KEY (ID_Cliente) REFERENCES Clienti(ID_Cliente) ON DELETE SET NULL
        """,
        "DettagliOrdini": """
            ID_DettaglioOrdine INT PRIMARY KEY AUTO_INCREMENT,
            ID_Ordine INT NOT NULL,
            ID_Lotto INT NOT NULL,
            Quantita INT,
            FOREIGN KEY (ID_Ordine) REFERENCES Ordini(ID_Ordine) ON DELETE CASCADE,
            FOREIGN KEY (ID_Lotto) REFERENCES Lotti(ID_Lotto) ON DELETE CASCADE
        """,
        # Gestione baie di carico/scarico e sensori
        "BaieCaricoScarico": """
            ID_Baia INT PRIMARY KEY AUTO_INCREMENT,
            ZonaID INT NOT NULL,
            Nome VARCHAR(255) NOT NULL,
            Tipo ENUM('Carico', 'Scarico') NOT NULL,
            Stato ENUM('Libera', 'Occupata', 'Manutenzione') DEFAULT 'Libera',
            FOREIGN KEY (ZonaID) REFERENCES Zone(ID_Zona) ON DELETE CASCADE,
            UNIQUE (ZonaID, Nome)
        """,
        "Sensori": """
            ID_Sensore INT PRIMARY KEY AUTO_INCREMENT,
            Tipo ENUM('Presenza', 'Temperatura', 'Umidità') NOT NULL,
            ID_Zona INT,
            Valore FLOAT,
            DataLettura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (ID_Zona) REFERENCES Zone(ID_Zona) ON DELETE SET NULL
        """,
        # Gestione robot
        "StazioneRicarica": """
            ID_Ricarica INT PRIMARY KEY AUTO_INCREMENT,
            ZonaID INT NOT NULL,
            Nome VARCHAR(255) NOT NULL,
            Stato ENUM('Libera', 'Occupata', 'Manutenzione') DEFAULT 'Libera',
            FOREIGN KEY (ZonaID) REFERENCES Zone(ID_Zona) ON DELETE CASCADE,
            UNIQUE (ZonaID, Nome)
        """,
        "Robot": """
            ID_Robot INT PRIMARY KEY AUTO_INCREMENT,
            ID_Sensore INT NOT NULL,
            ID_Zona INT NOT NULL,
            Nome VARCHAR(255) NOT NULL,
            Stato ENUM('Disponibile', 'Occupato', 'Manutenzione') DEFAULT 'Disponibile',
            PosizioneAttuale VARCHAR(255),
            Capacita INT,
            ID_Ricarica INT,
            FOREIGN KEY (ID_Sensore) REFERENCES Sensori(ID_Sensore) ON DELETE CASCADE,
            FOREIGN KEY (ID_Zona) REFERENCES Zone(ID_Zona) ON DELETE CASCADE,
            FOREIGN KEY (ID_Ricarica) REFERENCES StazioneRicarica(ID_Ricarica) ON DELETE SET NULL
        """,

        "RichiesteMovimento": """
            ID_Richiesta INT PRIMARY KEY AUTO_INCREMENT,
            ID_Lotto INT NOT NULL,
            ID_Zona_Destinazione INT NOT NULL,
            ID_Scaffalatura_Destinazione INT NOT NULL,
            Priorita INT DEFAULT 1,
            Stato ENUM('In attesa', 'Assegnata', 'Completata', 'Annullata') DEFAULT 'In attesa',
            ID_Robot INT,
            DataRichiesta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            DataCompletamento TIMESTAMP,
            FOREIGN KEY (ID_Lotto) REFERENCES Lotti(ID_Lotto) ON DELETE CASCADE,
            FOREIGN KEY (ID_Robot) REFERENCES Robot(ID_Robot) ON DELETE SET NULL,
            FOREIGN KEY (ID_Zona_Destinazione) REFERENCES Zone(ID_Zona) ON DELETE CASCADE,
            FOREIGN KEY (ID_Scaffalatura_Destinazione) REFERENCES Scaffalature(ID_Scaffalatura) ON DELETE CASCADE
        """,
        "StoricoMovimentiMagazzino": """
            ID_Movimento INT PRIMARY KEY AUTO_INCREMENT,
            ID_Lotto INT NOT NULL,
            DataMovimento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            TipoMovimento ENUM('Entrata', 'Uscita', 'Spostamento') NOT NULL,
            Quantita INT,
            ID_Zona_Partenza INT,
            ID_Zona_Arrivo INT,
            FOREIGN KEY (ID_Lotto) REFERENCES Lotti(ID_Lotto) ON DELETE CASCADE,
            FOREIGN KEY (ID_Zona_Partenza) REFERENCES Zone(ID_Zona) ON DELETE SET NULL,
            FOREIGN KEY (ID_Zona_Arrivo) REFERENCES Zone(ID_Zona) ON DELETE SET NULL
        """,
        "ControlloQualitaMovimenti": """
            ID_Controllo INT PRIMARY KEY AUTO_INCREMENT,
            ID_Richiesta INT NOT NULL,
            ID_Robot INT NOT NULL,
            Esito ENUM('Successo', 'Fallimento') NOT NULL,
            Note TEXT,
            DataControllo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (ID_Richiesta) REFERENCES RichiesteMovimento(ID_Richiesta) ON DELETE CASCADE,
            FOREIGN KEY (ID_Robot) REFERENCES Robot(ID_Robot) ON DELETE CASCADE
        """,
        # Gestione veicoli e consegne
        "Veicoli": """
            ID_Veicolo INT PRIMARY KEY AUTO_INCREMENT,
            Tipo ENUM('Bilico', 'Furgone', 'Carrello_Elevatore') NOT NULL,
            Capacita INT NOT NULL,
            Stato ENUM('Disponibile', 'In uso', 'Manutenzione') DEFAULT 'Disponibile',
            Targa VARCHAR(20) NOT NULL UNIQUE
        """,
        "Consegne": """
            ID_Consegna INT PRIMARY KEY AUTO_INCREMENT,
            ID_Ordine INT NOT NULL,
            ID_Veicolo INT,
            DataConsegna DATE,
            Stato ENUM('Pianificata', 'In corso', 'Completata', 'Annullata') DEFAULT 'Pianificata',
            FOREIGN KEY (ID_Ordine) REFERENCES Ordini(ID_Ordine) ON DELETE CASCADE,
            FOREIGN KEY (ID_Veicolo) REFERENCES Veicoli(ID_Veicolo) ON DELETE SET NULL
        """,
        # Gestione manutenzione
        "ManutenzioneRobot": """
            ID_Manutenzione INT PRIMARY KEY AUTO_INCREMENT,
            ID_Robot INT NOT NULL,
            DataManutenzione DATE NOT NULL,
            Tipo VARCHAR(255) NOT NULL,
            Stato ENUM('Programmata', 'Completata', 'Annullata') DEFAULT 'Programmata',
            Note TEXT,
            FOREIGN KEY (ID_Robot) REFERENCES Robot(ID_Robot) ON DELETE CASCADE
        """,
        "ManutenzioneScaffalature": """
            ID_Manutenzione INT PRIMARY KEY AUTO_INCREMENT,
            ID_Scaffalatura INT NOT NULL,
            DataManutenzione DATE NOT NULL,
            Tipo VARCHAR(255) NOT NULL,
            Stato ENUM('Programmata', 'Completata', 'Annullata') DEFAULT 'Programmata',
            Note TEXT,
            FOREIGN KEY (ID_Scaffalatura) REFERENCES Scaffalature(ID_Scaffalatura) ON DELETE CASCADE
        """,
        "ManutenzioneZone": """
            ID_Manutenzione INT PRIMARY KEY AUTO_INCREMENT,
            ID_Zona INT NOT NULL,
            DataManutenzione DATE NOT NULL,
            Tipo VARCHAR(255) NOT NULL,
            Stato ENUM('Programmata', 'Completata', 'Annullata') DEFAULT 'Programmata',
            Note TEXT,
            FOREIGN KEY (ID_Zona) REFERENCES Zone(ID_Zona) ON DELETE CASCADE
        """,
        "ManutenzioneVeicoli": """
            ID_Manutenzione INT PRIMARY KEY AUTO_INCREMENT,
            ID_Veicolo INT NOT NULL,
            DataManutenzione DATE NOT NULL,
            Tipo VARCHAR(255) NOT NULL,
            Stato ENUM('Programmata', 'Completata', 'Annullata') DEFAULT 'Programmata',
            Note TEXT,
            FOREIGN KEY (ID_Veicolo) REFERENCES Veicoli(ID_Veicolo) ON DELETE CASCADE
        """,
        # Gestione personale e accesso
        "Dipendenti": """
            ID_Dipendente INT PRIMARY KEY AUTO_INCREMENT,
            Nome VARCHAR(255) NOT NULL,
            Cognome VARCHAR(255) NOT NULL,
            Mansione VARCHAR(255),
            DataAssunzione DATE
        """,
        "TurniDipendenti": """
            ID_Turno INT PRIMARY KEY AUTO_INCREMENT,
            ID_Dipendente INT NOT NULL,
            DataInizio TIMESTAMP NOT NULL,
            DataFine TIMESTAMP NOT NULL,
            Mansione VARCHAR(255),
            FOREIGN KEY (ID_Dipendente) REFERENCES Dipendenti(ID_Dipendente) ON DELETE CASCADE
        """,
        "Credenziali": """
            ID_Utente INT PRIMARY KEY AUTO_INCREMENT,
            Username VARCHAR(255) NOT NULL UNIQUE,
            PasswordHash VARCHAR(255) NOT NULL,
            Ruolo ENUM('Amministratore', 'Operatore', 'Tecnico') NOT NULL,
            ID_Dipendente INT,
            FOREIGN KEY (ID_Dipendente) REFERENCES Dipendenti(ID_Dipendente) ON DELETE SET NULL
        """,
        "AccessiUtenti": """
            ID_Accesso INT PRIMARY KEY AUTO_INCREMENT,
            ID_Utente INT NOT NULL,
            DataOra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            Esito ENUM('Successo', 'Fallito') NOT NULL,
            IP VARCHAR(255),
            FOREIGN KEY (ID_Utente) REFERENCES Credenziali(ID_Utente) ON DELETE CASCADE
        """,
        "LogEventi": """
            ID_Log INT PRIMARY KEY AUTO_INCREMENT,
            DataOra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ID_Utente INT,
            Azione VARCHAR(255) NOT NULL,
            Dettagli TEXT,
            FOREIGN KEY (ID_Utente) REFERENCES Credenziali(ID_Utente) ON DELETE SET NULL
        """,
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
    """
    Popola il database con dati coerenti e pertinenti.
    """
    with connessione() as conn:
        # Lista di fornitori
        fornitori = [
            ("FreshFarm S.r.l.", "Via delle Mele 25, Torino", "0112233445", "info@freshfarm.it", "IT00112233445"),
            ("PharmaLife S.p.A.", "Viale della Salute 30, Bologna", "0519876543", "support@pharmalife.com", "IT55443322110"),
            ("BioNaturale S.r.l.", "Strada Verde 12, Firenze", "0551234567", "contact@bionaturale.it", "IT11223344556"),
            ("GlobalMed S.r.l.", "Piazza Ospedale 5, Roma", "0687654321", "info@globalmed.com", "IT66778899001"),
            ("QualityFood Distribuzione", "Via degli Orti 18, Palermo", "0916543210", "ordini@qualityfood.it", "IT88990011223"),
            ("NutrizionePlus S.p.A.", "Corso Benessere 8, Milano", "0245789631", "support@nutrizioneplus.it", "IT33445566778"),
            ("Farmacia del Sole", "Via della Scienza 2, Napoli", "0814567890", "info@farmaciasole.it", "IT22334455667"),
            ("Organic Italia", "Viale Bio 21, Genova", "0101230987", "info@organicitalia.it", "IT44556677889"),
            ("Distribuzione Salus", "Via Medica 10, Bari", "0803216547", "ordini@salus.com", "IT55667788990"),
            ("AlimentiTop S.r.l.", "Via Fresca 7, Venezia", "0416789123", "vendite@alimentitop.it", "IT77889900112"),
        ]

        # Inserimento nella tabella Fornitori
        for f in fornitori:
            add_record(conn, "Fornitori", 
                ["Nome", "Indirizzo", "Telefono", "Email", "PartitaIVA"], f)

        # Lista di prodotti
        prodotti = [
            # Alimentari
            (1, "Mela Golden", "FreshFarm S.r.l.", "Alimentare", "kg",),
            (1, "Insalata Bio", "BioNaturale S.r.l.", "Alimentare", "g",),
            (2, "Paracetamolo 500mg", "PharmaLife S.p.A.", "Farmaceutico", "compresse",),
            (3, "Farina di Grano Duro", "BioNaturale S.r.l.", "Alimentare", "kg",),
            (4, "Bende Sterili", "GlobalMed S.r.l.", "Farmaceutico", "pezzo",),
            (5, "Pasta di Gragnano", "QualityFood Distribuzione", "Alimentare", "kg",),
            (6, "Integratore Vitamina C", "NutrizionePlus S.p.A.", "Farmaceutico", "compresse",),
            (7, "Olio Extra Vergine di Oliva", "Organic Italia", "Alimentare", "litro",),
            (8, "Antibiotico Amoxicillina 250mg", "Distribuzione Salus", "Farmaceutico", "capsule",),
            (9, "Pancake Mix", "AlimentiTop S.r.l.", "Alimentare", "kg",),
            (10, "Crema Per il Dolore", "Farmacia del Sole", "Farmaceutico", "tubo",),
        ]

        # Inserimento nella tabella Prodotti
        for p in prodotti:
            add_record(conn, "Prodotti", 
                ["ID_Fornitore", "Nome", "Produttore", "Tipo", "UnitaMisura"], p)

        # Zone
        zone = [
            ("Stoccaggio Alimenti", "Stoccaggio_Alimentari", "Zona dedicata ai prodotti alimentari."),
            ("Stoccaggio Farmaci", "Stoccaggio_Farmaceutici", "Zona dedicata ai prodotti farmaceutici."),
            ("Baia Carico", "Carico", "Area di carico merci."),
            ("Baia Scarico", "Scarico", "Area di scarico merci."),
        ]
        for z in zone:
            add_record(conn, "Zone", 
                ["Nome", "Tipo", "Descrizione"], z)

        # Scaffalature
        scaffalature = [
            (1, "Scaffale A1", 100),  # Scaffale per alimentari
            (1, "Scaffale A2", 80),   # Scaffale per alimentari
            (2, "Scaffale B1", 150),  # Scaffale per farmaceutici
            (2, "Scaffale B2", 120),  # Scaffale per farmaceutici
            (3, "Scaffale C1", 50),   # Scaffale per carico
            (4, "Scaffale D1", 60)    # Scaffale per scarico
        ]

        # Inserimento nella tabella Scaffalature
        for s in scaffalature:
            add_record(conn, "Scaffalature", 
                ["ID_Zona", "Nome", "Capacita"], s)

        # Lotti
        lotti = [
            # Prodotti alimentari
            (1, 1, 1, "Lotto001", "2025-12-31", 500, 2.50, "2024-11-01", "Disponibile"),  # Mela Golden
            (1, 1, 2, "Lotto002", "2025-12-31", 300, 2.50, "2024-11-01", "Disponibile"),  # Mela Golden
            (3, 1, 1, "Lotto003", "2025-06-30", 200, 1.80, "2024-10-15", "Disponibile"),  # Farina di Grano Duro
            (5, 1, 2, "Lotto004", "2025-06-30", 400, 3.00, "2024-10-20", "Disponibile"),  # Pasta di Gragnano
            (7, 1, 1, "Lotto005", "2026-06-30", 100, 8.00, "2024-09-25", "Disponibile"),  # Olio Extra Vergine di Oliva
            # Prodotti farmaceutici
            (2, 2, 3, "Lotto006", "2026-01-15", 1000, 0.50, "2024-11-01", "Disponibile"),  # Paracetamolo 500mg
            (6, 2, 3, "Lotto007", "2026-01-15", 500, 15.00, "2024-10-10", "Disponibile"),  # Integratore Vitamina C
            (8, 2, 4, "Lotto008", "2027-01-01", 200, 5.00, "2024-11-05", "Disponibile"),  # Antibiotico Amoxicillina
            (10, 2, 4, "Lotto009", "2025-12-01", 50, 7.00, "2024-10-01", "Disponibile"),  # Crema Per il Dolore
        ]

        # Inserimento nella tabella Lotti
        for l in lotti:
            add_record(conn, "Lotti", 
                ["ID_Prodotto", "ID_Zona", "ID_Scaffalatura", "Lotto", "Scadenza", "Quantita", "PrezzoAcquisto", "DataRicevimento", "Stato"], l)
                
        # Clienti
        clienti = [
            ("Farmacia Rossi", "Via Milano 5, Torino", "0112233445", "rossi@farmacia.com", "IT11223344556"),
            ("Supermercato Verde", "Via Napoli 22, Roma", "0665544332", "verde@supermercati.com", "IT66778899001"),
        ]
        for c in clienti:
            add_record(conn, "Clienti", 
                ["Nome", "Indirizzo", "Telefono", "Email", "PartitaIVA"], c)

        # Ordini
        ordini = [
            ("2023-11-20 10:00:00", "Entrata", 1, None, "In elaborazione"),
            ("2023-11-25 15:30:00", "Uscita", None, 1, "Concluso"),
        ]
        for o in ordini:
            add_record(conn, "Ordini", 
                ["DataOrdine", "Tipo", "ID_Fornitore", "ID_Cliente", "Stato"], o)

        # Dettagli Ordini
        dettagli_ordini = [
            (1, 1, 50),
            (2, 2, 20),
        ]
        for d in dettagli_ordini:
            add_record(conn, "DettagliOrdini", 
                ["ID_Ordine", "ID_Lotto", "Quantita"], d)

        # Baie di Carico/Scarico
        baie = [
            (3, "Baia 1", "Carico", "Libera"),
            (4, "Baia 2", "Scarico", "Libera"),
        ]
        for b in baie:
            add_record(conn, "BaieCaricoScarico", 
                ["ZonaID", "Nome", "Tipo", "Stato"], b)

        # Dipendenti
        dipendenti = [
            ("Mario", "Rossi", "Magazziniere", "2020-01-15"),
            ("Giulia", "Verdi", "Responsabile Ordini", "2018-05-10"),
        ]
        for d in dipendenti:
            add_record(conn, "Dipendenti", 
                ["Nome", "Cognome", "Mansione", "DataAssunzione"], d)

        # Credenziali
        credenziali = [
            ("admin", "hashed_password_1", "Amministratore", 1),
            ("operatore1", "hashed_password_2", "Operatore", 2),
        ]
        for cred in credenziali:
            add_record(conn, "Credenziali", 
                ["Username", "PasswordHash", "Ruolo", "ID_Dipendente"], cred)

        # Veicoli
        veicoli = [
            ("Bilico", 2000, "Disponibile", "AA123BB"),
            ("Furgone", 500, "Disponibile", "CC456DD"),
        ]
        for v in veicoli:
            add_record(conn, "Veicoli", 
                ["Tipo", "Capacita", "Stato", "Targa"], v)

        # Consegne
        consegne = [
            (1, 1, "2023-11-21", "Pianificata"),
            (2, 2, "2023-11-26", "Completata"),
        ]
        for c in consegne:
            add_record(conn, "Consegne", 
                ["ID_Ordine", "ID_Veicolo", "DataConsegna", "Stato"], c)

        print("Database popolato con successo!")

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
    populateSQL()
    #askSQL()
    #alterSQL('Product', 'new_column', 'VARCHAR(50)')
    #dropSQL('ControlloQualitaMovimenti', if_exists=False)