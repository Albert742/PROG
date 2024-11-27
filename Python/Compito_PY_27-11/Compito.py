#Parte a
def conta_duplicati(dizionario):
    valori = dizionario.values()
    return len(valori) != len(set(valori))

D1 = {'a':18, 'b':18, 'c':24}
print(conta_duplicati(D1))
D2 = {'a':18, 'b':11, 'c':24}
print(conta_duplicati(D2))


#Parte b
def conta_caratteri_non_in_S(s, S):
    return sum(1 for carattere in s if carattere not in S)

s = "problema"
S = {'c', 'z'}
print(conta_caratteri_non_in_S(s, S))

#Parte c 
def conta_parole_con_caratteri(nome_file, caratteri):
    file = open(nome_file, 'r')
    testo = file.read()
    file.close()
    
    parole = testo.split()
    parole_con_caratteri = 0
    parole_senza_caratteri = 0
    
    for parola in parole:
        contiene_carattere = False
        for carattere in parola:
            if carattere in caratteri:
                contiene_carattere = True
                break
        if contiene_carattere:
            parole_con_caratteri += 1
        else:
            parole_senza_caratteri += 1
    return ('numero parole con caratteri in S', parole_con_caratteri, 'numero parole senza caratteri in S', parole_senza_caratteri)

nome_file = "costituzione_articolo_10.txt"
caratteri = {'a', 'b'}
risultato = conta_parole_con_caratteri(nome_file, caratteri)
print(risultato)

#Parte d
def conta_caratteri(nome_file, caratteri):
    file = open(nome_file, 'r')
    testo = file.read()
    file.close()
    
    parole = testo.split()
    risultati = []
    
    for parola in parole:
        conteggio = sum(1 for carattere in parola if carattere not in caratteri)
        risultati.append(parola + ": " + str(conteggio))
    
    file_counted = open(nome_file.replace('.txt', '_counted.txt'), 'w')
    file_counted.write(', '.join(risultati))
    file_counted.close()

nome_file = "costituzione_articolo_10.txt"
caratteri = {'a', 'e'}
conta_caratteri(nome_file, caratteri)

file_counted = open(nome_file.replace('.txt', '_counted.txt'), 'r')
print(file_counted.read())
file_counted.close()
