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
}

function visualizzaProdotti() {
    global $filename;
    $products = leggiProdottiDaFile($filename);
    foreach ($products as $product) {
        list($id, $name, $quantity, $deperibile) = $product;
        echo "Nome: $name, Quantità: $quantity, Deperibile: $deperibile<br>";
    }
}

function calcolaTotale() {
    global $filename;
    $products = leggiProdottiDaFile($filename);
    $total = 0;
    foreach ($products as $product) {
        list($id, $name, $quantity, $deperibile) = $product;
        $total += (int)$quantity;
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
            echo json_encode(['error' => 'duplicate', 'field' => $existingId === $id ? 'id' : 'name']);
            return;
        }
    }

    $newProduct = [$id, $name, $quantity, $deperibile];
    $products[] = $newProduct;
    scriviProdottiSuFile($filename, $products);
    echo json_encode(['success' => true]);
}

function leggiProdottiDaFile($filename) {
    $products = [];
    if (file_exists($filename)) {
        $file = fopen($filename, 'r');
        while (($line = fgets($file)) !== false) {
            $products[] = explode('|', trim($line));
        }
        fclose($file);
    }
    return $products;
}

function scriviProdottiSuFile($filename, $products) {
    $file = fopen($filename, 'w');
    foreach ($products as $product) {
        fputcsv($file, $product, '|');
    }
    fclose($file);
}
?>