#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Devi inserire almeno un comando:"
    read comando
    if [[ "$comando" == "uscita" ]]; then
        echo "Uscita dallo script..."
        
    fi	
    echo "Vuoi aggiungere argomenti al comando? (s/n)"
    read risposta
    if [[ "$risposta" == "s" ]]; then
        echo "Inserisci il primo argomento: "
        read arg1
        echo "Inserisci il secondo argomento (lascia vuoto se non serve): "
        read arg2
    fi
    if [[ -z "$arg1" ]]; then 
        echo "Esecuzione del comando: $comando"
        $comando
        sleep 5
    elif [[ -n "$arg1" ]]; then
        if [[ -z "$arg2" ]]; then
            echo "Esecuzione del comando: $comando con primo argomento $arg1"
            $comando $arg1
            sleep 5
        else    
            echo "Esecuzione del comando: $comando con primo argomento $arg1 e secondo argomento $arg2"
            $comando $arg1 $arg2
            sleep 5
        fi
    fi
    arg1=""
    arg2=""
elif [[ $# -gt 0 ]]; then
    echo "Esecuzione del comando iniziale: $1 $2 "
    $1 $2 
    sleep 5
fi

while true; do
    echo "Inserisci un nuovo comando o 'uscita' per terminare:"
    read comando
    if [[ "$comando" == "uscita" ]]; then
        echo "Uscita dallo script..."
        break
    fi	
    echo "Vuoi aggiungere argomenti al comando? (s/n)"
    read risposta
    if [[ "$risposta" == "s" ]]; then
        echo "Inserisci il primo argomento: "
        read arg1
        echo "Inserisci il secondo argomento (lascia vuoto se non serve): "
        read arg2
    fi
    if [[ -z "$arg1" ]]; then 
        echo "Esecuzione del comando: $comando"
        $comando
        sleep 5
    elif [[ -n "$arg1" ]]; then
        if [[ -z "$arg2" ]]; then
            echo "Esecuzione del comando: $comando con primo argomento $arg1"
            $comando $arg1
            sleep 5
        else    
            echo "Esecuzione del comando: $comando con primo argomento $arg1 e secondo argomento $arg2"
            $comando $arg1 $arg2
            sleep 5
        fi
    fi
    arg1=""
    arg2=""
done
