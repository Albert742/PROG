def estrai_char(s, k):
    return [s[i] for i in range(0, len(s), k)]
def estrai_char_alt(s, k):
    risultato = []
    for i in range(0, len(s), k):
        risultato.append(s[i])
    return risultato

# Test della funzione
s = "Ciao, come stai?"
k = 3
print(estrai_char_alt(s, k))  

s = "Ciao! Palle!!?"
k = 2
print(estrai_char(s, k))  
