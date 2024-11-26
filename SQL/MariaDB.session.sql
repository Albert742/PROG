CREATE TABLE Prodotti (
    ID_Prodotto INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Produttore VARCHAR(255),
    Tipo ENUM('Alimentare', 'Farmaceutico') NOT NULL,
    UnitaMisura VARCHAR(50)
);

CREATE TABLE Lotti (
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
);


CREATE TABLE Alimentari (
    ID_Prodotto INT PRIMARY KEY,
    Allergeni TEXT,
    FOREIGN KEY (ID_Prodotto) REFERENCES Prodotti(ID_Prodotto)
);

CREATE TABLE Farmaceutici (
    ID_Prodotto INT PRIMARY KEY,
    PrincipioAttivo VARCHAR(255),
    FOREIGN KEY (ID_Prodotto) REFERENCES Prodotti(ID_Prodotto)
);

CREATE TABLE Fornitori (
    ID_Fornitore INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Indirizzo VARCHAR(255),
    Telefono VARCHAR(20),
    Email VARCHAR(255)
);

CREATE TABLE Clienti (
    ID_Cliente INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Indirizzo VARCHAR(255),
    Telefono VARCHAR(20),
    Email VARCHAR(255)
);

CREATE TABLE Ordini (
    ID_Ordine INT PRIMARY KEY AUTO_INCREMENT,
    DataOrdine TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Tipo ENUM('Entrata', 'Uscita') NOT NULL,
    ID_Fornitore INT,
    ID_Cliente INT,
    FOREIGN KEY (ID_Fornitore) REFERENCES Fornitori(ID_Fornitore),
    FOREIGN KEY (ID_Cliente) REFERENCES Clienti(ID_Cliente)
);


CREATE TABLE DettagliOrdini (
    ID_DettaglioOrdine INT PRIMARY KEY AUTO_INCREMENT,
    ID_Ordine INT,
    ID_Lotto INT,
    Quantita INT,
    FOREIGN KEY (ID_Ordine) REFERENCES Ordini(ID_Ordine),
    FOREIGN KEY (ID_Lotto) REFERENCES Lotti(ID_Lotto)
);


CREATE TABLE MovimentiMagazzino (
    ID_Movimento INT PRIMARY KEY AUTO_INCREMENT,
    ID_Lotto INT,
    DataMovimento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TipoMovimento ENUM('Entrata', 'Uscita', 'Spostamento') NOT NULL,
    Quantita INT,
    DaZona VARCHAR(255),
    AZona VARCHAR(255),
    FOREIGN KEY (ID_Lotto) REFERENCES Lotti(ID_Lotto)
);

CREATE TABLE Robot (
    ID_Robot INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Stato ENUM('Disponibile', 'Occupato', 'Manutenzione') DEFAULT 'Disponibile',
    PosizioneAttuale VARCHAR(255),
    Capacita INT
);

CREATE TABLE Sensori (
    ID_Sensore INT PRIMARY KEY AUTO_INCREMENT,
    Tipo ENUM('Presenza', 'Temperatura', 'Umidità') NOT NULL,  -- Aggiungi altri tipi se necessario
    Zona VARCHAR(255),
    Valore FLOAT,
    DataLettura TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE RichiesteMovimento (
    ID_Richiesta INT PRIMARY KEY AUTO_INCREMENT,
    ID_Lotto INT,
    Destinazione VARCHAR(255),
    Priorita INT DEFAULT 1, -- 1 = bassa, maggiore è il numero maggiore è la priorità
    Stato ENUM('In attesa', 'Assegnata', 'Completata', 'Annullata') DEFAULT 'In attesa',
    ID_Robot INT,
    DataRichiesta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    DataCompletamento TIMESTAMP,
    FOREIGN KEY (ID_Lotto) REFERENCES Lotti(ID_Lotto),
    FOREIGN KEY (ID_Robot) REFERENCES Robot(ID_Robot)
);

CREATE TABLE StoricoMovimentiRobot (
    ID_MovimentoRobot INT PRIMARY KEY AUTO_INCREMENT,
    ID_Robot INT,
    DataOra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Azione VARCHAR(255),
    FOREIGN KEY (ID_Robot) REFERENCES Robot(ID_Robot)
);


-- Tabella Dipendenti
CREATE TABLE Dipendenti (
    ID_Dipendente INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Cognome VARCHAR(255) NOT NULL,
    Mansione VARCHAR(255), -- Es. "Operatore", "Manutentore", "Supervisore"
    DataAssunzione DATE
);