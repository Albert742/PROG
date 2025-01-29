#es1

def purge_carattere_da_file(P, nome_file):
    # Leggi il contenuto del file originale
    file = open(nome_file, 'r')
    content = file.read()
    file.close()
    
    # Rimuovi i caratteri specificati dalla lista
    for char in P:
        content = content.replace(char, '')
    
    # Crea il nome del nuovo file
    new_file_name = nome_file.replace('.txt', '_purged.txt')
    
    # Salva il contenuto modificato nel nuovo file
    new_file = open(new_file_name, 'w')
    new_file.write(content)
    new_file.close()

# Esempio di utilizzo
purge_carattere_da_file(['a', 'e', 'i', 'o', 'u'], 'prova.txt')