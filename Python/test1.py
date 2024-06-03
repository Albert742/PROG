import random

class Scatola:
    def __init__(self, numero, premio):
        self.numero = numero
        self.premio = premio
        self.aperta = False

    def apri(self):
        self.aperta = True
        return self.premio

# Creazione delle scatole con premi in ordine casuale
premi = list(range(1000, 11000, 1000))
random.shuffle(premi)
scatole = [Scatola(i, premio) for i, premio in enumerate(premi)]

while len([s for s in scatole if not s.aperta]) > 1:
    print("Scatole rimanenti:", [s.numero for s in scatole if not s.aperta])
    scelta = int(input("Scegli una scatola da aprire: "))
    premio = scatole[scelta].apri()
    print(f"Hai aperto la scatola {scelta} e hai perso il premio di {premio} euro!")

# L'ultimo pacco rimasto è la vincita
vincita = [s.premio for s in scatole if not s.aperta][0]
print(f"Hai terminato il gioco! La tua vincita è: {vincita} euro!")
