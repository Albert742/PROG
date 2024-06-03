import random

# Creare una lista di 10 pacchi con cifre crescenti da 0 a 300000
pacchi = sorted(random.sample(range(300001), 10))
print(f"Pacchi originali: {pacchi}")

eliminati = 0
while pacchi:
    # Fare scegliere un elemento della lista ed eliminarlo dalla lista
    scelta = int(input("Scegli un pacco da eliminare (inserisci l'indice): "))
    if scelta < len(pacchi):
        pacco_eliminato = pacchi.pop(scelta)
        print(f"Hai eliminato il pacco con valore {pacco_eliminato}")
        eliminati += 1

        # Ogni 3 elementi eliminati viene proposta la vincita uguale a (media dei pacchi rimanenti)/2
        if eliminati % 3 == 0 and pacchi:
            vincita = sum(pacchi) / (2 * len(pacchi))
            print(f"La tua vincita proposta è: {vincita}")
    else:
        print("Indice non valido. Riprova.")
else:
    print("Tutti i pacchi sono stati eliminati.")
