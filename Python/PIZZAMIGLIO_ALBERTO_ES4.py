"""
Esercizio 4 (Oggetti)
Parte 1. Scrivere una classe “Spiaggia” che rappresenti una spiaggia caratterizzata dal tipo di
spiaggia tra “sabbia” e “ciottoli” e dalla lunghezza in metri.
La classe deve provvedere:
- metodo per la costruzione una istanza dell’oggetto Spiaggia
- metodo per stampare informazioni sulla istanza di un oggetto Spiaggia
- metodi per comparare due Spiagge in base alla loro lunghezza
Parte 2. scrivere una classe “Litorale” che rappresenti una collezione di Spiagge.
La classe deve provvedere:
- metodo per la costruzione una istanza dell’oggetto Litorale
- metodo per stampare informazioni sulla istanza di un oggetto Litorale
- metodo per fornire il numero totale di metri di tutte le spiagge “sabbia” del Litorale
- metodo per fornire il numero totale di metri di tutte le spiagge “ciottoli” del Litorale
Parte 3. Scrivere codice per “collaudare” le classi create.
"""

# Parte 1
class Spiaggia:
    def __init__(self, tipo, lunghezza):
        self.tipo = tipo
        self.lunghezza = lunghezza

    def stampa_info(self):
        print(f"Spiaggia di tipo {self.tipo} di {self.lunghezza} metri in lunghezza ")
        print("-------------------")    
        
    def confronta_lunghezza(self, altra_spiaggia):
        prima_è_più_lunga = self.lunghezza > altra_spiaggia.lunghezza
        seconda_è_più_lunga = self.lunghezza < altra_spiaggia.lunghezza
        sono_uguali = self.lunghezza == altra_spiaggia.lunghezza
        return prima_è_più_lunga, seconda_è_più_lunga, sono_uguali

# Parte 2
class Litorale:
    def __init__(self):
        self.spiagge = []

    def aggiungi_spiaggia(self, spiaggia):
        self.spiagge.append(spiaggia)

    def stampa_info(self):
        print(f"N° spiagge nel litorale: {len(self.spiagge)}")
        print(f"Di cui spiagge di tipo 'sabbia': {sum(1 for s in self.spiagge if s.tipo == 'sabbia')}")
        print(f"Di cui spiagge di tipo 'ciottoli': {sum(1 for s in self.spiagge if s.tipo == 'ciottoli')}")
        print("\n")
        for spiaggia in self.spiagge:
            spiaggia.stampa_info()
        print("\n")
    def totale_lunghezza_tipo_sabbia(self):
        totale = 0
        for spiaggia in self.spiagge:
            if spiaggia.tipo == "sabbia":
                totale += spiaggia.lunghezza
        return totale

    def totale_lunghezza_tipo_ciottoli(self):
        totale = 0
        for spiaggia in self.spiagge:
            if spiaggia.tipo == "ciottoli":
                totale += spiaggia.lunghezza
        return totale

# Parte 3

# Collaudo parte 1
spiaggia1 = Spiaggia("sabbia", 100)
spiaggia2 = Spiaggia("ciottoli", 225)
spiaggia3 = Spiaggia("sabbia", 230)
spiaggia4 = Spiaggia("ciottoli", 100)

print("\n")
spiaggia1.stampa_info()
spiaggia2.stampa_info()
spiaggia3.stampa_info()
spiaggia4.stampa_info()

print("\n")
risultato = spiaggia1.confronta_lunghezza(spiaggia2)
print(f"La spiaggia è più lunga dell'altra Spiaggia : {risultato[0]}")
print(f"La spiaggia è più corta dell'altra Spiaggia : {risultato[1]}")
print(f"Le lunghezze delle Spiagge sono uguali: {risultato[2]}")
print("\n")
risultato = spiaggia3.confronta_lunghezza(spiaggia1)
print(f"La spiaggia è più lunga dell'altra Spiaggia : {risultato[0]}")
print(f"La spiaggia è più corta dell'altra Spiaggia : {risultato[1]}")
print(f"Le lunghezze delle Spiagge sono uguali: {risultato[2]}")
print("\n")
risultato = spiaggia1.confronta_lunghezza(spiaggia4)
print(f"La spiaggia è più lunga dell'altra Spiaggia : {risultato[0]}")
print(f"La spiaggia è più corta dell'altra Spiaggia : {risultato[1]}")
print(f"Le lunghezze delle Spiagge sono uguali: {risultato[2]}")
print("\n")

# Collaudo parte 2
litorale = Litorale()
litorale2 = Litorale()

spiaggia5 = Spiaggia("ciottoli", 150)
spiaggia6 = Spiaggia("sabbia", 235)
spiaggia7 = Spiaggia("ciottoli", 255)

litorale.aggiungi_spiaggia(spiaggia1)
litorale.aggiungi_spiaggia(spiaggia3)
litorale.aggiungi_spiaggia(spiaggia5)
litorale.aggiungi_spiaggia(spiaggia7)

litorale2.aggiungi_spiaggia(spiaggia2)
litorale2.aggiungi_spiaggia(spiaggia4)
litorale2.aggiungi_spiaggia(spiaggia6)

litorale.stampa_info()
litorale2.stampa_info()

print(f"Totale lunghezza spiagge sabbia: {litorale.totale_lunghezza_tipo_sabbia()} metri")
print(f"Totale lunghezza spiagge ciottoli: {litorale.totale_lunghezza_tipo_ciottoli()} metri")
print("\n")
print(f"Totale lunghezza spiagge sabbia: {litorale2.totale_lunghezza_tipo_sabbia()} metri")
print(f"Totale lunghezza spiagge ciottoli: {litorale2.totale_lunghezza_tipo_ciottoli()} metri")
