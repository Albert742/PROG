<?php
session_start();

if (!isset($_SESSION['products'])) {
    $_SESSION['products'] = [];
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if ($_GET['action'] === 'view') {
        viewProducts();
    } elseif ($_GET['action'] === 'calculate') {
        calculateTotal();
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST' && $_GET['action'] === 'insert') {
    insertProduct();
}

function viewProducts() {
    $products = $_SESSION['products'];
    foreach ($products as $product) {
        list($id, $name, $quantity, $perishable) = $product;
        echo "Nome: $name, Quantità: $quantity, Deteriorabile: $perishable<br>";
    }
}

function calculateTotal() {
    $products = $_SESSION['products'];
    $total = 0;
    foreach ($products as $product) {
        list($id, $name, $quantity, $perishable) = $product;
        $total += (int)$quantity;
    }
    echo "Quantità totale in magazzino: $total";
}

function insertProduct() {
    $id = uniqid();
    $name = $_POST['productName'];
    $quantity = $_POST['quantity'];
    $perishable = $_POST['perishable'];

    $products = $_SESSION['products'];
    foreach ($products as $product) {
        list($existingId, $existingName) = $product;
        if ($existingId === $id || $existingName === $name) {
            echo json_encode(['error' => 'duplicate', 'field' => $existingId === $id ? 'id' : 'name']);
            return;
        }
    }

    $newProduct = [$id, $name, $quantity, $perishable];
    $_SESSION['products'][] = $newProduct;
    echo json_encode(['success' => true]);
}
?>