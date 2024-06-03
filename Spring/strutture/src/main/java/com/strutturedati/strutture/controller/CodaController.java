package com.strutturedati.strutture.controller;

import java.util.LinkedList;
import java.util.Queue;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/coda")
public class CodaController {
    private final Queue<String> coda = new LinkedList<>();

    @GetMapping("/aggiungi")
    public String aggiungiAllaCoda(String elemento) {
        try {
            coda.add(elemento);
            return "Elemento aggiunto alla coda: " + elemento;
        } catch (IllegalStateException ex) {
            return "Errore: La coda è piena";
        }
    }

    @GetMapping("/rimuovi")
    public String rimuoviDallaCoda() {
        if (coda.isEmpty()) {
            return "La coda è vuota";
        }
        String elemento = coda.poll();
        return "Elemento rimosso dalla coda: " + elemento;
    }

    @GetMapping("/vizualizza")
    public String visualizzaProssimoElemento() {
        if (coda.isEmpty()) {
            return "La coda è vuota";
        }
        String elemento = coda.peek();
        return "Elemento successivo nella coda: " + elemento;
    }

    @GetMapping("/dimensione")
    public int ottieniDimensioneCoda() {
        return coda.size();
    }
}