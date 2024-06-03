"""
Esercizio 1 (Stringhe)
Scrivere una funzione che data una stringa alfabetica s restituisce una nuova stringa p ottenuta da s
scambiando di posto i caratteri successivi a due a due in s. Se i caratteri in s sono dispari l'ultimo
carattere non viene cambiato.
Esempio: s=”aprile”→ “pairel”, o anche “marzo” → ”amzro”
"""
# Funzione
def scambio_caratteri_stringa (s):
    stringa_scambiata = ""
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            stringa_scambiata += s[i+1] + s[i]
    else:
        for i in range(0, len(s)-1, 2):
            stringa_scambiata += s[i+1] + s[i]
        stringa_scambiata += s[-1]
    return stringa_scambiata

# Utilizzo
s = "marzo"
p = scambio_caratteri_stringa(s)
print(p)