"""
Esercizio 2 (Liste)
Scrivere una funzione che data una lista di stringhe S restituisce una 2-tupla T=(T1,T2) i cui
elementi sono così formati: T1 è la lista di tutti i primi caratteri degli elementi di S e T2 è la lista di
tutti gli ultimi caratteri degli elementi di S.
Esempio: S=[“pippo”, ”pluto”, “paperino”]→ ([“p”, “p”, “p”],[“o”, “o”, “o”])
"""
# Funzione
def estrazione_primo_ultimo_carattere(s):
    T1 = [parola[0] for parola in s]
    T2 = [parola[-1] for parola in s]
    return (T1, T2)

# Utilizzo
S = ["pippo", "pluto", "paperino", "topolino"]
car_estratti = estrazione_primo_ultimo_carattere(S)
print(car_estratti) 