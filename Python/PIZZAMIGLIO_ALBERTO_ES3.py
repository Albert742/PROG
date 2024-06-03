"""
Esercizio 3 (Dizionari)
Scrivere una funzione che data una lista L di numeri interi (senza duplicati) restituisce un
dizionario D tale che gli elementi di L sono le sue chiavi e il corrispondente valore è una 2-tupla di
booleani (b1,b2) tale che b1 è True se e solo se la chiave è pari e b2 è True se e solo se la chiave è
un multiplo di 3
Esempio: S=[12, 7, 21, 14, 0], → D={12:(True,True), 7:(False,False), 21:(False, True),
14:(True,False), 0:(True, True)}
"""
# Funzione
def crea_dizionario(l):
    D = {}
    for numero in l:
        b1 = numero % 2 == 0
        b2 = numero % 3 == 0
        D[numero] = (b1, b2)
    return D

# Utilizzo
L = [12, 7, 21, 14, 0]
risultato = crea_dizionario(L)
print(risultato) 