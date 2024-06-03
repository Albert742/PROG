#!/bin/bash

echo "Inserisci un parametro:"
read -r parametro

if [ -f "$parametro" ]; then 
    echo "Il parametro è un file esistente"
elif [ -d "$parametro" ]; then 
    echo "Il parametro è una directory esistente"
    for file in "$parametro"/*; do
        if [ -f "$file" ]; then 
            echo "File: $file"
        elif [ -d "$file" ]; then 
            echo "Directory: $file"
        fi
    done
else 
    echo "Il parametro non è ne un file ne una directory esistente"

    while true; do
        echo "Come procedere"
        echo "1: Crea file"
        echo "2: Crea directory"
        echo "3: Esci"

        read -r decisione

        if [[ $decisione -eq 1 ]]; then 
            cmd="touch"
            echo "Inserisci il nome del file:"
            read -r nomef
            $cmd "$parametro/$nomef"
        elif [[ $decisione -eq 2 ]]; then 
            cmd="mkdir"
            echo "Inserisci il nome della directory"
            read -r nomed
            $cmd "$parametro/$nomed"
        elif [[ $decisione -eq 3 ]]; then 
            echo "Uscita..."
            break
        else 
            echo "Opzione non valida"
        fi
    done

fi

7
