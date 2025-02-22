<?php
session_start();

$filename = 'prodotti.txt';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if ($_GET['action'] === 'view') {
        visualizzaProdotti();
    } elseif ($_GET['action'] === 'calculate') {
        calcolaTotale();
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST' && $_GET['action'] === 'insert') {
    inserisciProdotto();
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST' && $_GET['action'] === 'remove') {
    rimuoviProdotto();
}
function visualizzaProdotti() {
    global $filename;
    $products = leggiProdottiDaFile($filename);
    foreach ($products as $product) {
        if (count($product) === 4) {
            list($id, $name, $quantity, $deperibile) = $product;
            echo "Nome: $name , Quantità: $quantity , Deperibile: $deperibile<br>";
        }
    }
}

function calcolaTotale() {
    global $filename;
    $products = leggiProdottiDaFile($filename);
    $total = 0;
    foreach ($products as $product) {
        if (count($product) === 4) {
            list($id, $name, $quantity, $deperibile) = $product;
            $total += (int)$quantity;
        }
    }
    echo "Quantità totale in magazzino: $total";
}

function inserisciProdotto() {
    global $filename;
    $id = uniqid();
    $name = $_POST['productName'];
    $quantity = $_POST['quantity'];
    $deperibile = $_POST['deperibile'];

    $products = leggiProdottiDaFile($filename);
    foreach ($products as $product) {
        list($existingId, $existingName) = $product;
        if ($existingId === $id || $existingName === $name) {
            echo "Errore: " . ($existingId === $id ? "ID prodotto già esistente." : "Nome prodotto già esistente.");
            return;
        }
    }

    $newProduct = [$id, $name, $quantity, $deperibile];
    $products[] = $newProduct;
    scriviProdottiSuFile($filename, $products);
    echo "Prodotto inserito con successo.";
}

function leggiProdottiDaFile($filename) {
    $products = [];
    if (file_exists($filename)) {
        $file = fopen($filename, 'r');
        while (($line = fgets($file)) !== false) {
            $products[] = explode(':', trim($line));
        }
        fclose($file);
    }
    return $products;
}

function scriviProdottiSuFile($filename, $products) {
    $file = fopen($filename, 'w');
    foreach ($products as $product) {
        $linea = implode(':', $product) . PHP_EOL;
        fwrite($file, $linea);
    }
    fclose($file);
}

function rimuoviProdotto() {
    global $filename;
    $name = $_POST['removeProductName'];

    $products = leggiProdottiDaFile($filename);
    $productFound = false;
    foreach ($products as $index => $product) {
        if ($product[1] === $name) {
            $productFound = true;
            unset($products[$index]);
            break;
        }
    }

    if ($productFound) {
        scriviProdottiSuFile($filename, $products);
        echo "Prodotto rimosso con successo.";
    } else {
        echo "Errore: Nome prodotto non trovato.";
    }
}
?>