-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: magazzino
-- ------------------------------------------------------
-- Server version	11.4.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accessiutenti`
--

DROP TABLE IF EXISTS `accessiutenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accessiutenti` (
  `ID_Accesso` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Utente` int(11) NOT NULL,
  `DataOra` timestamp NULL DEFAULT current_timestamp(),
  `Esito` enum('Successo','Fallito') NOT NULL,
  `IP` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_Accesso`),
  KEY `ID_Utente` (`ID_Utente`),
  CONSTRAINT `accessiutenti_ibfk_1` FOREIGN KEY (`ID_Utente`) REFERENCES `credenziali` (`ID_Utente`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accessiutenti`
--

LOCK TABLES `accessiutenti` WRITE;
/*!40000 ALTER TABLE `accessiutenti` DISABLE KEYS */;
/*!40000 ALTER TABLE `accessiutenti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `baiecaricoscarico`
--

DROP TABLE IF EXISTS `baiecaricoscarico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baiecaricoscarico` (
  `ID_Baia` int(11) NOT NULL AUTO_INCREMENT,
  `ZonaID` int(11) NOT NULL,
  `Nome` varchar(255) NOT NULL,
  `Tipo` enum('Carico','Scarico') NOT NULL,
  `Stato` enum('Libera','Occupata','Manutenzione') DEFAULT 'Libera',
  PRIMARY KEY (`ID_Baia`),
  UNIQUE KEY `ZonaID` (`ZonaID`,`Nome`),
  CONSTRAINT `baiecaricoscarico_ibfk_1` FOREIGN KEY (`ZonaID`) REFERENCES `zone` (`ID_Zona`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baiecaricoscarico`
--

LOCK TABLES `baiecaricoscarico` WRITE;
/*!40000 ALTER TABLE `baiecaricoscarico` DISABLE KEYS */;
/*!40000 ALTER TABLE `baiecaricoscarico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clienti`
--

DROP TABLE IF EXISTS `clienti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clienti` (
  `ID_Cliente` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) NOT NULL,
  `Indirizzo` varchar(255) DEFAULT NULL,
  `Telefono` varchar(20) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `PartitaIVA` varchar(20) NOT NULL,
  PRIMARY KEY (`ID_Cliente`),
  UNIQUE KEY `PartitaIVA` (`PartitaIVA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clienti`
--

LOCK TABLES `clienti` WRITE;
/*!40000 ALTER TABLE `clienti` DISABLE KEYS */;
/*!40000 ALTER TABLE `clienti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consegne`
--

DROP TABLE IF EXISTS `consegne`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consegne` (
  `ID_Consegna` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Ordine` int(11) NOT NULL,
  `ID_Veicolo` int(11) DEFAULT NULL,
  `DataConsegna` date DEFAULT NULL,
  `Stato` enum('Pianificata','In corso','Completata','Annullata') DEFAULT 'Pianificata',
  PRIMARY KEY (`ID_Consegna`),
  KEY `ID_Ordine` (`ID_Ordine`),
  KEY `ID_Veicolo` (`ID_Veicolo`),
  CONSTRAINT `consegne_ibfk_1` FOREIGN KEY (`ID_Ordine`) REFERENCES `ordini` (`ID_Ordine`) ON DELETE CASCADE,
  CONSTRAINT `consegne_ibfk_2` FOREIGN KEY (`ID_Veicolo`) REFERENCES `veicoli` (`ID_Veicolo`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consegne`
--

LOCK TABLES `consegne` WRITE;
/*!40000 ALTER TABLE `consegne` DISABLE KEYS */;
/*!40000 ALTER TABLE `consegne` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `controlloqualitamovimenti`
--

DROP TABLE IF EXISTS `controlloqualitamovimenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `controlloqualitamovimenti` (
  `ID_Controllo` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Richiesta` int(11) NOT NULL,
  `ID_Robot` int(11) NOT NULL,
  `Esito` enum('Successo','Fallimento') NOT NULL,
  `Note` text DEFAULT NULL,
  `DataControllo` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`ID_Controllo`),
  KEY `ID_Richiesta` (`ID_Richiesta`),
  KEY `ID_Robot` (`ID_Robot`),
  CONSTRAINT `controlloqualitamovimenti_ibfk_1` FOREIGN KEY (`ID_Richiesta`) REFERENCES `richiestemovimento` (`ID_Richiesta`) ON DELETE CASCADE,
  CONSTRAINT `controlloqualitamovimenti_ibfk_2` FOREIGN KEY (`ID_Robot`) REFERENCES `robot` (`ID_Robot`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `controlloqualitamovimenti`
--

LOCK TABLES `controlloqualitamovimenti` WRITE;
/*!40000 ALTER TABLE `controlloqualitamovimenti` DISABLE KEYS */;
/*!40000 ALTER TABLE `controlloqualitamovimenti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credenziali`
--

DROP TABLE IF EXISTS `credenziali`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `credenziali` (
  `ID_Utente` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) NOT NULL,
  `PasswordHash` varchar(255) NOT NULL,
  `Ruolo` enum('Amministratore','Operatore','Tecnico') NOT NULL,
  `ID_Dipendente` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_Utente`),
  UNIQUE KEY `Username` (`Username`),
  KEY `ID_Dipendente` (`ID_Dipendente`),
  CONSTRAINT `credenziali_ibfk_1` FOREIGN KEY (`ID_Dipendente`) REFERENCES `dipendenti` (`ID_Dipendente`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credenziali`
--

LOCK TABLES `credenziali` WRITE;
/*!40000 ALTER TABLE `credenziali` DISABLE KEYS */;
/*!40000 ALTER TABLE `credenziali` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dettagliordini`
--

DROP TABLE IF EXISTS `dettagliordini`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dettagliordini` (
  `ID_DettaglioOrdine` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Ordine` int(11) NOT NULL,
  `ID_Lotto` int(11) NOT NULL,
  `Quantita` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_DettaglioOrdine`),
  KEY `ID_Ordine` (`ID_Ordine`),
  KEY `ID_Lotto` (`ID_Lotto`),
  CONSTRAINT `dettagliordini_ibfk_1` FOREIGN KEY (`ID_Ordine`) REFERENCES `ordini` (`ID_Ordine`) ON DELETE CASCADE,
  CONSTRAINT `dettagliordini_ibfk_2` FOREIGN KEY (`ID_Lotto`) REFERENCES `lotti` (`ID_Lotto`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dettagliordini`
--

LOCK TABLES `dettagliordini` WRITE;
/*!40000 ALTER TABLE `dettagliordini` DISABLE KEYS */;
/*!40000 ALTER TABLE `dettagliordini` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dipendenti`
--

DROP TABLE IF EXISTS `dipendenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dipendenti` (
  `ID_Dipendente` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) NOT NULL,
  `Cognome` varchar(255) NOT NULL,
  `Mansione` varchar(255) DEFAULT NULL,
  `DataAssunzione` date DEFAULT NULL,
  PRIMARY KEY (`ID_Dipendente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dipendenti`
--

LOCK TABLES `dipendenti` WRITE;
/*!40000 ALTER TABLE `dipendenti` DISABLE KEYS */;
/*!40000 ALTER TABLE `dipendenti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fornitori`
--

DROP TABLE IF EXISTS `fornitori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fornitori` (
  `ID_Fornitore` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) NOT NULL,
  `Indirizzo` varchar(255) DEFAULT NULL,
  `Telefono` varchar(20) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `PartitaIVA` varchar(20) NOT NULL,
  PRIMARY KEY (`ID_Fornitore`),
  UNIQUE KEY `PartitaIVA` (`PartitaIVA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fornitori`
--

LOCK TABLES `fornitori` WRITE;
/*!40000 ALTER TABLE `fornitori` DISABLE KEYS */;
/*!40000 ALTER TABLE `fornitori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logeventi`
--

DROP TABLE IF EXISTS `logeventi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logeventi` (
  `ID_Log` int(11) NOT NULL AUTO_INCREMENT,
  `DataOra` timestamp NULL DEFAULT current_timestamp(),
  `ID_Utente` int(11) DEFAULT NULL,
  `Azione` varchar(255) NOT NULL,
  `Dettagli` text DEFAULT NULL,
  PRIMARY KEY (`ID_Log`),
  KEY `ID_Utente` (`ID_Utente`),
  CONSTRAINT `logeventi_ibfk_1` FOREIGN KEY (`ID_Utente`) REFERENCES `credenziali` (`ID_Utente`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logeventi`
--

LOCK TABLES `logeventi` WRITE;
/*!40000 ALTER TABLE `logeventi` DISABLE KEYS */;
/*!40000 ALTER TABLE `logeventi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lotti`
--

DROP TABLE IF EXISTS `lotti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lotti` (
  `ID_Lotto` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Prodotto` int(11) NOT NULL,
  `ID_Zona` int(11) NOT NULL,
  `ID_Scaffalatura` int(11) NOT NULL,
  `Lotto` varchar(255) DEFAULT NULL,
  `Scadenza` date DEFAULT NULL,
  `Quantita` int(11) DEFAULT NULL,
  `PrezzoAcquisto` decimal(10,2) DEFAULT NULL,
  `DataRicevimento` date DEFAULT NULL,
  `Stato` enum('Disponibile','In transito','Prenotato') DEFAULT 'Disponibile',
  PRIMARY KEY (`ID_Lotto`),
  UNIQUE KEY `ID_Prodotto` (`ID_Prodotto`,`Lotto`),
  KEY `ID_Zona` (`ID_Zona`),
  KEY `ID_Scaffalatura` (`ID_Scaffalatura`),
  CONSTRAINT `lotti_ibfk_1` FOREIGN KEY (`ID_Prodotto`) REFERENCES `prodotti` (`ID_Prodotto`) ON DELETE CASCADE,
  CONSTRAINT `lotti_ibfk_2` FOREIGN KEY (`ID_Zona`) REFERENCES `zone` (`ID_Zona`) ON DELETE CASCADE,
  CONSTRAINT `lotti_ibfk_3` FOREIGN KEY (`ID_Scaffalatura`) REFERENCES `scaffalature` (`ID_Scaffalatura`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lotti`
--

LOCK TABLES `lotti` WRITE;
/*!40000 ALTER TABLE `lotti` DISABLE KEYS */;
/*!40000 ALTER TABLE `lotti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manutenzionerobot`
--

DROP TABLE IF EXISTS `manutenzionerobot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manutenzionerobot` (
  `ID_Manutenzione` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Robot` int(11) NOT NULL,
  `DataManutenzione` date NOT NULL,
  `Tipo` varchar(255) NOT NULL,
  `Stato` enum('Programmata','Completata','Annullata') DEFAULT 'Programmata',
  `Note` text DEFAULT NULL,
  PRIMARY KEY (`ID_Manutenzione`),
  KEY `ID_Robot` (`ID_Robot`),
  CONSTRAINT `manutenzionerobot_ibfk_1` FOREIGN KEY (`ID_Robot`) REFERENCES `robot` (`ID_Robot`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manutenzionerobot`
--

LOCK TABLES `manutenzionerobot` WRITE;
/*!40000 ALTER TABLE `manutenzionerobot` DISABLE KEYS */;
/*!40000 ALTER TABLE `manutenzionerobot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manutenzionescaffalature`
--

DROP TABLE IF EXISTS `manutenzionescaffalature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manutenzionescaffalature` (
  `ID_Manutenzione` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Scaffalatura` int(11) NOT NULL,
  `DataManutenzione` date NOT NULL,
  `Tipo` varchar(255) NOT NULL,
  `Stato` enum('Programmata','Completata','Annullata') DEFAULT 'Programmata',
  `Note` text DEFAULT NULL,
  PRIMARY KEY (`ID_Manutenzione`),
  KEY `ID_Scaffalatura` (`ID_Scaffalatura`),
  CONSTRAINT `manutenzionescaffalature_ibfk_1` FOREIGN KEY (`ID_Scaffalatura`) REFERENCES `scaffalature` (`ID_Scaffalatura`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manutenzionescaffalature`
--

LOCK TABLES `manutenzionescaffalature` WRITE;
/*!40000 ALTER TABLE `manutenzionescaffalature` DISABLE KEYS */;
/*!40000 ALTER TABLE `manutenzionescaffalature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manutenzioneveicoli`
--

DROP TABLE IF EXISTS `manutenzioneveicoli`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manutenzioneveicoli` (
  `ID_Manutenzione` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Veicolo` int(11) NOT NULL,
  `DataManutenzione` date NOT NULL,
  `Tipo` varchar(255) NOT NULL,
  `Stato` enum('Programmata','Completata','Annullata') DEFAULT 'Programmata',
  `Note` text DEFAULT NULL,
  PRIMARY KEY (`ID_Manutenzione`),
  KEY `ID_Veicolo` (`ID_Veicolo`),
  CONSTRAINT `manutenzioneveicoli_ibfk_1` FOREIGN KEY (`ID_Veicolo`) REFERENCES `veicoli` (`ID_Veicolo`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manutenzioneveicoli`
--

LOCK TABLES `manutenzioneveicoli` WRITE;
/*!40000 ALTER TABLE `manutenzioneveicoli` DISABLE KEYS */;
/*!40000 ALTER TABLE `manutenzioneveicoli` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manutenzionezone`
--

DROP TABLE IF EXISTS `manutenzionezone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manutenzionezone` (
  `ID_Manutenzione` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Zona` int(11) NOT NULL,
  `DataManutenzione` date NOT NULL,
  `Tipo` varchar(255) NOT NULL,
  `Stato` enum('Programmata','Completata','Annullata') DEFAULT 'Programmata',
  `Note` text DEFAULT NULL,
  PRIMARY KEY (`ID_Manutenzione`),
  KEY `ID_Zona` (`ID_Zona`),
  CONSTRAINT `manutenzionezone_ibfk_1` FOREIGN KEY (`ID_Zona`) REFERENCES `zone` (`ID_Zona`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manutenzionezone`
--

LOCK TABLES `manutenzionezone` WRITE;
/*!40000 ALTER TABLE `manutenzionezone` DISABLE KEYS */;
/*!40000 ALTER TABLE `manutenzionezone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordini`
--

DROP TABLE IF EXISTS `ordini`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordini` (
  `ID_Ordine` int(11) NOT NULL AUTO_INCREMENT,
  `DataOrdine` timestamp NULL DEFAULT current_timestamp(),
  `Tipo` enum('Entrata','Uscita') NOT NULL,
  `ID_Fornitore` int(11) DEFAULT NULL,
  `ID_Cliente` int(11) DEFAULT NULL,
  `Stato` enum('In elaborazione','Spedito','Concluso') DEFAULT 'In elaborazione',
  PRIMARY KEY (`ID_Ordine`),
  KEY `ID_Fornitore` (`ID_Fornitore`),
  KEY `ID_Cliente` (`ID_Cliente`),
  CONSTRAINT `ordini_ibfk_1` FOREIGN KEY (`ID_Fornitore`) REFERENCES `fornitori` (`ID_Fornitore`) ON DELETE SET NULL,
  CONSTRAINT `ordini_ibfk_2` FOREIGN KEY (`ID_Cliente`) REFERENCES `clienti` (`ID_Cliente`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordini`
--

LOCK TABLES `ordini` WRITE;
/*!40000 ALTER TABLE `ordini` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordini` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prodotti`
--

DROP TABLE IF EXISTS `prodotti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prodotti` (
  `ID_Prodotto` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Fornitore` int(11) DEFAULT NULL,
  `Nome` varchar(255) NOT NULL,
  `Produttore` varchar(255) DEFAULT NULL,
  `Tipo` enum('Alimentare','Farmaceutico') NOT NULL,
  `UnitaMisura` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_Prodotto`),
  UNIQUE KEY `Nome` (`Nome`,`Produttore`),
  KEY `ID_Fornitore` (`ID_Fornitore`),
  CONSTRAINT `prodotti_ibfk_1` FOREIGN KEY (`ID_Fornitore`) REFERENCES `fornitori` (`ID_Fornitore`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prodotti`
--

LOCK TABLES `prodotti` WRITE;
/*!40000 ALTER TABLE `prodotti` DISABLE KEYS */;
/*!40000 ALTER TABLE `prodotti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `richiestemovimento`
--

DROP TABLE IF EXISTS `richiestemovimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `richiestemovimento` (
  `ID_Richiesta` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Lotto` int(11) NOT NULL,
  `ID_Zona_Destinazione` int(11) NOT NULL,
  `ID_Scaffalatura_Destinazione` int(11) NOT NULL,
  `Priorita` int(11) DEFAULT 1,
  `Stato` enum('In attesa','Assegnata','Completata','Annullata') DEFAULT 'In attesa',
  `ID_Robot` int(11) DEFAULT NULL,
  `DataRichiesta` timestamp NULL DEFAULT current_timestamp(),
  `DataCompletamento` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`ID_Richiesta`),
  KEY `ID_Lotto` (`ID_Lotto`),
  KEY `ID_Robot` (`ID_Robot`),
  KEY `ID_Zona_Destinazione` (`ID_Zona_Destinazione`),
  KEY `ID_Scaffalatura_Destinazione` (`ID_Scaffalatura_Destinazione`),
  CONSTRAINT `richiestemovimento_ibfk_1` FOREIGN KEY (`ID_Lotto`) REFERENCES `lotti` (`ID_Lotto`) ON DELETE CASCADE,
  CONSTRAINT `richiestemovimento_ibfk_2` FOREIGN KEY (`ID_Robot`) REFERENCES `robot` (`ID_Robot`) ON DELETE SET NULL,
  CONSTRAINT `richiestemovimento_ibfk_3` FOREIGN KEY (`ID_Zona_Destinazione`) REFERENCES `zone` (`ID_Zona`) ON DELETE CASCADE,
  CONSTRAINT `richiestemovimento_ibfk_4` FOREIGN KEY (`ID_Scaffalatura_Destinazione`) REFERENCES `scaffalature` (`ID_Scaffalatura`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `richiestemovimento`
--

LOCK TABLES `richiestemovimento` WRITE;
/*!40000 ALTER TABLE `richiestemovimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `richiestemovimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `robot`
--

DROP TABLE IF EXISTS `robot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `robot` (
  `ID_Robot` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Sensore` int(11) NOT NULL,
  `ID_Zona` int(11) NOT NULL,
  `Nome` varchar(255) NOT NULL,
  `Stato` enum('Disponibile','Occupato','Manutenzione') DEFAULT 'Disponibile',
  `PosizioneAttuale` varchar(255) DEFAULT NULL,
  `Capacita` int(11) DEFAULT NULL,
  `ID_Ricarica` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_Robot`),
  KEY `ID_Sensore` (`ID_Sensore`),
  KEY `ID_Zona` (`ID_Zona`),
  KEY `ID_Ricarica` (`ID_Ricarica`),
  CONSTRAINT `robot_ibfk_1` FOREIGN KEY (`ID_Sensore`) REFERENCES `sensori` (`ID_Sensore`) ON DELETE CASCADE,
  CONSTRAINT `robot_ibfk_2` FOREIGN KEY (`ID_Zona`) REFERENCES `zone` (`ID_Zona`) ON DELETE CASCADE,
  CONSTRAINT `robot_ibfk_3` FOREIGN KEY (`ID_Ricarica`) REFERENCES `stazionericarica` (`ID_Ricarica`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `robot`
--

LOCK TABLES `robot` WRITE;
/*!40000 ALTER TABLE `robot` DISABLE KEYS */;
/*!40000 ALTER TABLE `robot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scaffalature`
--

DROP TABLE IF EXISTS `scaffalature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scaffalature` (
  `ID_Scaffalatura` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Zona` int(11) NOT NULL,
  `Nome` varchar(255) NOT NULL,
  `Capacita` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_Scaffalatura`),
  KEY `ID_Zona` (`ID_Zona`),
  CONSTRAINT `scaffalature_ibfk_1` FOREIGN KEY (`ID_Zona`) REFERENCES `zone` (`ID_Zona`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scaffalature`
--

LOCK TABLES `scaffalature` WRITE;
/*!40000 ALTER TABLE `scaffalature` DISABLE KEYS */;
/*!40000 ALTER TABLE `scaffalature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensori`
--

DROP TABLE IF EXISTS `sensori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensori` (
  `ID_Sensore` int(11) NOT NULL AUTO_INCREMENT,
  `Tipo` enum('Presenza','Temperatura','Umidità') NOT NULL,
  `ID_Zona` int(11) DEFAULT NULL,
  `Valore` float DEFAULT NULL,
  `DataLettura` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`ID_Sensore`),
  KEY `ID_Zona` (`ID_Zona`),
  CONSTRAINT `sensori_ibfk_1` FOREIGN KEY (`ID_Zona`) REFERENCES `zone` (`ID_Zona`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensori`
--

LOCK TABLES `sensori` WRITE;
/*!40000 ALTER TABLE `sensori` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stazionericarica`
--

DROP TABLE IF EXISTS `stazionericarica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stazionericarica` (
  `ID_Ricarica` int(11) NOT NULL AUTO_INCREMENT,
  `ZonaID` int(11) NOT NULL,
  `Nome` varchar(255) NOT NULL,
  `Stato` enum('Libera','Occupata','Manutenzione') DEFAULT 'Libera',
  PRIMARY KEY (`ID_Ricarica`),
  UNIQUE KEY `ZonaID` (`ZonaID`,`Nome`),
  CONSTRAINT `stazionericarica_ibfk_1` FOREIGN KEY (`ZonaID`) REFERENCES `zone` (`ID_Zona`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stazionericarica`
--

LOCK TABLES `stazionericarica` WRITE;
/*!40000 ALTER TABLE `stazionericarica` DISABLE KEYS */;
/*!40000 ALTER TABLE `stazionericarica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storicomovimentimagazzino`
--

DROP TABLE IF EXISTS `storicomovimentimagazzino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storicomovimentimagazzino` (
  `ID_Movimento` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Lotto` int(11) NOT NULL,
  `DataMovimento` timestamp NULL DEFAULT current_timestamp(),
  `TipoMovimento` enum('Entrata','Uscita','Spostamento') NOT NULL,
  `Quantita` int(11) DEFAULT NULL,
  `ID_Zona_Partenza` int(11) DEFAULT NULL,
  `ID_Zona_Arrivo` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_Movimento`),
  KEY `ID_Lotto` (`ID_Lotto`),
  KEY `ID_Zona_Partenza` (`ID_Zona_Partenza`),
  KEY `ID_Zona_Arrivo` (`ID_Zona_Arrivo`),
  CONSTRAINT `storicomovimentimagazzino_ibfk_1` FOREIGN KEY (`ID_Lotto`) REFERENCES `lotti` (`ID_Lotto`) ON DELETE CASCADE,
  CONSTRAINT `storicomovimentimagazzino_ibfk_2` FOREIGN KEY (`ID_Zona_Partenza`) REFERENCES `zone` (`ID_Zona`) ON DELETE SET NULL,
  CONSTRAINT `storicomovimentimagazzino_ibfk_3` FOREIGN KEY (`ID_Zona_Arrivo`) REFERENCES `zone` (`ID_Zona`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storicomovimentimagazzino`
--

LOCK TABLES `storicomovimentimagazzino` WRITE;
/*!40000 ALTER TABLE `storicomovimentimagazzino` DISABLE KEYS */;
/*!40000 ALTER TABLE `storicomovimentimagazzino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turnidipendenti`
--

DROP TABLE IF EXISTS `turnidipendenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turnidipendenti` (
  `ID_Turno` int(11) NOT NULL AUTO_INCREMENT,
  `ID_Dipendente` int(11) NOT NULL,
  `DataInizio` timestamp NOT NULL,
  `DataFine` timestamp NOT NULL,
  `Mansione` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_Turno`),
  KEY `ID_Dipendente` (`ID_Dipendente`),
  CONSTRAINT `turnidipendenti_ibfk_1` FOREIGN KEY (`ID_Dipendente`) REFERENCES `dipendenti` (`ID_Dipendente`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turnidipendenti`
--

LOCK TABLES `turnidipendenti` WRITE;
/*!40000 ALTER TABLE `turnidipendenti` DISABLE KEYS */;
/*!40000 ALTER TABLE `turnidipendenti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veicoli`
--

DROP TABLE IF EXISTS `veicoli`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veicoli` (
  `ID_Veicolo` int(11) NOT NULL AUTO_INCREMENT,
  `Tipo` enum('Bilico','Furgone','Carrello_Elevatore') NOT NULL,
  `Capacita` int(11) NOT NULL,
  `Stato` enum('Disponibile','In uso','Manutenzione') DEFAULT 'Disponibile',
  `Targa` varchar(20) NOT NULL,
  PRIMARY KEY (`ID_Veicolo`),
  UNIQUE KEY `Targa` (`Targa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veicoli`
--

LOCK TABLES `veicoli` WRITE;
/*!40000 ALTER TABLE `veicoli` DISABLE KEYS */;
/*!40000 ALTER TABLE `veicoli` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zone`
--

DROP TABLE IF EXISTS `zone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zone` (
  `ID_Zona` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) NOT NULL,
  `Tipo` enum('Stoccaggio_Alimentari','Stoccaggio_Farmaceutici','Carico','Scarico') NOT NULL,
  `Descrizione` text DEFAULT NULL,
  PRIMARY KEY (`ID_Zona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zone`
--

LOCK TABLES `zone` WRITE;
/*!40000 ALTER TABLE `zone` DISABLE KEYS */;
/*!40000 ALTER TABLE `zone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'magazzino'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-28 17:33:40
