#es1 basi

def purge_carattere_da_file(P, nome_file):
    # Leggi il contenuto del file originale
    file = open(nome_file, 'r')
    content = file.read()
    file.close()
    
    # Rimuovi i caratteri specificati dalla lista
    for char in P:
        content = content.replace(char, '')
    
    # Crea il nome del nuovo file
    new_file_name = nome_file.replace('.txt', '_purged.txt')
    
    # Salva il contenuto modificato nel nuovo file
    new_file = open(new_file_name, 'w')
    new_file.write(content)
    new_file.close()

# Esempio di utilizzo
purge_carattere_da_file(['a', 'e', 'i', 'o', 'u'], 'prova.txt')

#es2 basi

def carattere_frequenza_da_file(P, nome_file):
    # Leggi il contenuto del file originale
    file = open(nome_file, 'r')
    content = file.read()
    file.close()
    
    # Crea il nome del nuovo file
    new_file_name = nome_file.replace('.txt', '_stats.txt')
    
    # Calcola la frequenza dei caratteri specificati
    frequenze = {}
    for char in P:
        frequenze[char] = content.count(char)
    
    # Salva le frequenze nel nuovo file
    new_file = open(new_file_name, 'w')
    for char, freq in frequenze.items():
        new_file.write(f"{char},{freq}\n")
    new_file.close()

# Esempio di utilizzo
carattere_frequenza_da_file(['a', 'e', 'i', 'o', 'u'], 'prova.txt')

#es1 oggetti

import random

class Scatola:
    def __init__(self, id, premio):
        self.id = id
        self.premio = premio
        self.aperta = False

class Giocatore:
    def __init__(self, nome):
        self.nome = nome
        self.scatola_scelta = None

class Gioco:
    def __init__(self, giocatore):
        self.giocatore = giocatore
        self.scatole = self.crea_scatole()
        self.turno = 0

    def crea_scatole(self):
        premi = [0, 5, 10, 100, 250, 500, 1000, 10000, 100000, 300000]
        random.shuffle(premi)
        scatole = [Scatola(i, premi[i]) for i in range(10)]
        return scatole

    def scegli_scatola(self, id_scatola):
        self.giocatore.scatola_scelta = self.scatole[id_scatola]

    def calcola_offerta(self):
        scatole_non_aperte = [scatola for scatola in self.scatole if not scatola.aperta and scatola != self.giocatore.scatola_scelta]
        valore_medio = sum(scatola.premio for scatola in scatole_non_aperte) / len(scatole_non_aperte)
        offerta = valore_medio / 2 * (1 + 0.5 * random.random())
        return offerta

    def scarta_scatola(self, id_scatola):
        self.scatole[id_scatola].aperta = True

    def scambia_scatola(self, id_scatola):
        self.giocatore.scatola_scelta, self.scatole[id_scatola] = self.scatole[id_scatola], self.giocatore.scatola_scelta

    def termina_gioco(self):
        premio = self.giocatore.scatola_scelta.premio
        return premio

    def gioca_turno(self):
        self.turno += 1
        offerta = self.calcola_offerta()
        print(f"Turno {self.turno}: Offerta = {offerta}")
        scelta = input("Scegli: 1) Continua a giocare scartando una scatola, 2) Continua a giocare scambiando la scatola, 3) Termina il gioco: ")
        if scelta == '1':
            id_scatola = int(input("Inserisci l'ID della scatola da scartare: "))
            self.scarta_scatola(id_scatola)
        elif scelta == '2':
            id_scatola = int(input("Inserisci l'ID della scatola con cui scambiare: "))
            self.scambia_scatola(id_scatola)
        elif scelta == '3':
            premio = self.termina_gioco()
            print(f"Hai terminato il gioco. Il tuo premio è: {premio}")
            return False
        return True

    def inizia_gioco(self):
        id_scatola = int(input("Scegli una scatola iniziale (ID 0-9): "))
        self.scegli_scatola(id_scatola)
        while True:
            if not self.gioca_turno():
                break

# Esempio di utilizzo
giocatore = Giocatore("Mario")
gioco = Gioco(giocatore)
gioco.inizia_gioco()

#es2 oggetti

import random

class Casella:
    def __init__(self, tipo, valore=0):
        self.tipo = tipo
        self.valore = valore

class GiocatoreOca:
    def __init__(self, nome):
        self.nome = nome
        self.posizione = 0
        self.premi = 0
        self.fermo = False

class GiocoDellOca:
    def __init__(self, giocatore1o, giocatore2o):
        self.giocatore1o = giocatore1o
        self.giocatore2o = giocatore2o
        self.circuito = self.crea_circuito()
        self.turno = 0

    def crea_circuito(self):
        circuito = []
        for i in range(100):
            tipo = random.choice(['ordinaria', 'premio', 'fermo', 'indietro'])
            if tipo == 'premio':
                valore = random.randint(-10, 10)
            elif tipo == 'indietro':
                valore = random.randint(1, 3)
            else:
                valore = 0
            circuito.append(Casella(tipo, valore))
        return circuito

    def lancia_dado(self):
        input("Premi invio per lanciare il dado...")
        return random.randint(1, 6)

    def muovi_giocatore(self, giocatore):
        if giocatore.fermo:
            giocatore.fermo = False
            return
        dado = self.lancia_dado()
        print(f"{giocatore.nome} ha lanciato il dado e ha ottenuto: {dado}")
        giocatore.posizione += dado
        if giocatore.posizione >= 100:
            giocatore.posizione = 99
        casella = self.circuito[giocatore.posizione]
        print(f"{giocatore.nome} è arrivato sulla casella {giocatore.posizione} ({casella.tipo})")
        if casella.tipo == 'premio':
            giocatore.premi += casella.valore
            print(f"{giocatore.nome} ha ricevuto un premio di {casella.valore}. Premi totali: {giocatore.premi}")
        elif casella.tipo == 'fermo':
            giocatore.fermo = True
            print(f"{giocatore.nome} deve fermarsi un turno.")
        elif casella.tipo == 'indietro':
            giocatore.posizione -= casella.valore
            if giocatore.posizione < 0:
                giocatore.posizione = 0
            print(f"{giocatore.nome} deve tornare indietro di {casella.valore} caselle. Nuova posizione: {giocatore.posizione}")

    def gioca_turno(self):
        self.turno += 1
        if self.turno % 2 == 1:
            print(f"Turno di {self.giocatore1o.nome}")
            self.muovi_giocatore(self.giocatore1o)
        else:
            print(f"Turno di {self.giocatore2o.nome}")
            self.muovi_giocatore(self.giocatore2o)

    def verifica_vittoria(self):
        if self.giocatore1o.posizione >= 99 and self.giocatore2o.posizione >= 99:
            if self.giocatore1o.premi > self.giocatore2o.premi:
                return self.giocatore1o
            else:
                return self.giocatore2o
        elif self.giocatore1o.posizione >= 99:
            return self.giocatore1o
        elif self.giocatore2o.posizione >= 99:
            return self.giocatore2o
        return None

    def inizia_gioco(self):
        while True:
            self.gioca_turno()
            vincitore = self.verifica_vittoria()
            if vincitore:
                print(f"{vincitore.nome} ha vinto il gioco!")
                break

# Esempio di utilizzo
giocatore1o = GiocatoreOca("Giocatore 1")
giocatore2o = GiocatoreOca("Giocatore 2")
gioco = GiocoDellOca(giocatore1o, giocatore2o)
gioco.inizia_gioco()