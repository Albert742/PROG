def cont_char(stringa): #creazione funzione
    D = {} #creazione dizionario
    for char in stringa: #ciclo for per contare caratteri ripetuti
        if char in D: #controllo presenza
            D[char] += 1
        else:
            D[char] = 1
    return D
print(cont_char("Ciao!!"))
