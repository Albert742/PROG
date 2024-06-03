#!/bin/bash
#funzionee per creare array di numeri

function creaArray(){
    local arr=()
    for i in $@; do
        arr+=($i)
    done
    echo "${arr[@]}"
}

creaArray 1 2 8

#visualizza il valore di ogni elemento dell'array
function visualizzaArray(){
    for i in $@; do
        echo "$i"
    done
}

visualizzaArray 1 2 8

#calcola la somma di tutti i valori dell'array
function somma(){
    local somma=0
    for i in $@; do
        somma=$((somma+i))
    done
    echo "$somma"
}

somma 1 2 8


