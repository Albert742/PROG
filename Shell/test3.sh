#!/bin/bash
# Definizione di una funzione che restituisce il quadrato di un numero
quadrato() {
    echo $(($1 * $1))
}

# Definizione di un array di numeri
numero_array=("uno" "due" "tre" "quattro" "cinque")

# Stampa del valore di ogni elemento dell'array
echo "Elementi dell'array:"
for elemento in "${numero_array[@]}"; do
    echo "$elemento"
done

# Chiamata della funzione quadrato con il primo elemento dell'array come argomento
echo "Il quadrato del primo elemento dell'array è:"
# shellcheck disable=SC2005
# shellcheck disable=SC2046
echo $(quadrato "${numero_array[0]}")