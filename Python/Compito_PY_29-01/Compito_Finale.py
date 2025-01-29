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

print(percentuale_vocali('prova.txt'))

#b

def cinque_parole(file):
    f = open(file, 'r')
    testo = f.read()
    f.close()
    parole = testo.split()
    vocali = ['a', 'e', 'i', 'o', 'u']
    parole_vocali = []
    for parola in parole:
        if parola[-1] in vocali:
            parole_vocali.append(parola)
    for i in range(len(parole_vocali)):
        for j in range(i + 1, len(parole_vocali)):
            if len(parole_vocali[i]) < len(parole_vocali[j]):
                parole_vocali[i], parole_vocali[j] = parole_vocali[j], parole_vocali[i]
    return tuple(parole_vocali[:5])

print(cinque_parole('prova.txt'))

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