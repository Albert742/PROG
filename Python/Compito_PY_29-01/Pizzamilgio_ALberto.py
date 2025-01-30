"""
Esercizio 1 – studenti M-Z
Scrivere funzioni necessarie a risolvere il seguente problema:
Dato un file di testo calcolare:
a) la percentuale, sul totale, delle ‘parole’ che terminano con le vocali ‘a’,’e’,’i’,’o’,’u’.
(si intende per ‘parola’ ogni sotto-stringa compresa tra due ‘spazi’ o tra ‘inizio file’ e spazio o tra
‘spazio’ e ‘fine file’).
b) trovare e riportare in una 5-tupla le cinque ‘parole’ di lunghezza massima che terminano in
‘a’,’e’,’i’,’o’,’u’. A parità di lunghezza riportare la ‘parola’ che occorre per prima.
c) scrivere sul disco un file ottenuto da quello di ingresso che riporta in formato csv le seguenti
informazioni pe rogni riga di testo nel file di ingresso:
numero di caratteri, numero di vocali.
"""
import os

#a

def percentuale_vocali(file):
    f = open(file, 'r')
    testo = f.read()
    f.close()
    parole = testo.split()
    vocali = ['a', 'e', 'i', 'o', 'u']
    vocali_parole = 0
    for parola in parole:
        if parola[-1] in vocali:
            vocali_parole += 1
    percentuale = vocali_parole / len(parole) * 100
    return percentuale

print(percentuale_vocali('dante.txt'))

#b

def cinque_parole(file):
    f = open(file, 'r', encoding='utf-8')
    testo = f.read()
    f.close()
    
    parole = testo.split()
    vocali = ['a', 'e', 'i', 'o', 'u']
    parole_vocali = []
    
    for parola in parole:
        if parola[-1].lower() in vocali:
            parole_vocali.append(parola)
    
    for i in range(len(parole_vocali)):
        for j in range(i + 1, len(parole_vocali)):
            if len(parole_vocali[i]) < len(parole_vocali[j]):
                parole_vocali[i], parole_vocali[j] = parole_vocali[j], parole_vocali[i]
                
    return tuple(parole_vocali[:5])

print(cinque_parole('dante.txt'))

#c

def file_csv(file_path):
    f = open(file_path, 'r')
    righe = f.readlines()
    f.close()

    o = open('output.csv', 'w')
    for riga in righe:
        numero_caratteri = len(riga.strip())
        numero_vocali =0
        for carattere in riga:
            if carattere in ['a', 'e', 'i', 'o', 'u']:
                numero_vocali += 1
        o.write(str(numero_caratteri) + "," + str(numero_vocali) + "\n")
    o.close()

file_csv('dante.txt')



"""
Esercizio 2 – studenti M-Z
Si chiede di creare software che usi la programmazione ad oggetti per simulare il seguente gioco.
Il gioco è una sfida di due giocatori contro il computer. Il computer compone una stringa di H
caratteri presi casualmente dall’alfabeto internazionale. La stringa è inizialmente nascosta.
I giocatori a turno ‘chiamano’ un carattere e se questo è presente nella stringa ricevono tanti punti
quante sono le occorrenze del carattere. Se però il carattere non è presente il punteggio del giocatore
si azzera. Il gioco termina quando, a parità di tentativi, sono state ‘scoperte’ almeno il 50% delle
lettere nascoste.
"""
import random
import string

class Gioco:
    def __init__(self, lunghezza):
        self.computer = Computer(lunghezza)
        self.giocatori = [Giocatore("Giocatore 1"), Giocatore("Giocatore 2")]
        self.turni = 0

    def inizia(self):
        for giocatore in self.giocatori:
            giocatore.scelta_nome()
        self.turno()

    def turno(self):
        while self.computer.percentuale_scoperta() < 50:
            for giocatore in self.giocatori:
                print("\nTurno di " + giocatore.nome + " \n")
                char = giocatore.carattere_scelto(self.computer.caratteri_usati)
                punti = self.computer.scopri_caratteri(char)
                if punti > 0:
                    giocatore.punteggio += punti
                    print("Carattere trovato. " + giocatore.nome + " ha guadagnato " + str(punti) + " punti.")
                else:
                    print("Carattere errato. " + giocatore.nome + " ha perso tutti i suoi punti.")
                    giocatore.punteggio = 0
                self.turni += 1
                self.stato_gioco()
                if self.computer.percentuale_scoperta() >= 50:
                    break
        self.risultato()

    def stato_gioco(self):
        print("Stringa scoperta: " + ''.join(self.computer.scoperta) + "\nTurni: " + str(self.turni)+ "\n")
        for giocatore in self.giocatori:
            print(giocatore.nome + ": " + str(giocatore.punteggio) + " punti")

    def risultato(self):
        print("\nGioco Finito, almeno la metà della stringa è stata trovata \n")
        for giocatore in self.giocatori:
            print(giocatore.nome + ": " + str(giocatore.punteggio) + " punti")
        vincitore = self.giocatori[0]
        for giocatore in self.giocatori:
            if giocatore.punteggio > vincitore.punteggio:
                vincitore = giocatore
        print("\nIl vincitore è " + vincitore.nome + " con " + str(vincitore.punteggio) + " punti \n")

class Computer:
    def __init__(self, lunghezza):
        self.stringa_nascosta = self.genera_stringa(lunghezza)
        self.scoperta = ['_'] * lunghezza
        self.caratteri_usati = set()

    def genera_stringa(self, lunghezza):
        Str = ''.join(random.choices(string.ascii_lowercase, k=lunghezza))
        return Str

    def scopri_caratteri(self, char):
        if char in self.stringa_nascosta:
            for i in range(len(self.stringa_nascosta)):
                c = self.stringa_nascosta[i]
                if c == char:
                    self.scoperta[i] = char
            return self.scoperta.count(char)
        else:
            return 0
        
    def caratteri_scoperti(self):
        S = self.scoperta.count('_')
        return S
    
    def percentuale_scoperta(self):
        P = (len(self.scoperta) - self.scoperta.count('_')) / len(self.scoperta) * 100
        return P

class Giocatore:
    def __init__(self, nome):
        self.nome = nome
        self.punteggio = 0
        
    def scelta_nome(self):
        self.nome = input("Ciao Giocatore " + self.nome.split()[-1] + ", inserisci il tuo nome: ")
        return self.nome

    def carattere_scelto(self, caratteri_usati):
        while True:
            CS = input("Giocatore " + self.nome.split()[-1] + " Inserisci il carattere che vuoi scoprire: ")
            if CS in caratteri_usati:
                print("Carattere già usato, scegline un altro. \n")
            else:
                caratteri_usati.add(CS)
                return CS
    
gioco = Gioco(10)
gioco.inizia()