import hashlib

def create_employee_id(codice_fiscale, nome, cognome, ruolo, data_assunzione):
    """
    Crea un ID dipendente unico dato il codice fiscale, nome, cognome, ruolo e data di assunzione.
    """
    concatenated_string = f"{codice_fiscale}{nome}{cognome}{ruolo}{data_assunzione}"
    hashed_string = hashlib.sha256(concatenated_string.encode()).hexdigest()
    employee_id = hashed_string[:10]
    return employee_id

id = create_employee_id("VRDGLI90D43C351B", "Giulia", "Verdi", "Amministratore", "2015-01-20")
print(id)
"""
("RSSMRA80A01C351O", "Mario", "Rossi", "Operatore", "2020-05-15"),
("BNCLSU98E54C351X", "Luisa", "Bianchi", "Tecnico", "2020-03-10"),
("VRDGLI90D43C351B", "Giulia", "Verdi", "Amministratore", "2015-01-20")
"""