<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $interests = isset($_POST["interests"]) ? $_POST["interests"] : [];

    echo "<h2>Dati del Form:</h2>";
    echo "<p>Nome: " . htmlspecialchars($name) . "</p>";

    if (!empty($interests)) {
        echo "<p>Interessi:</p>";
        echo "<ul>";
        foreach ($interests as $interest) {
            echo "<li>" . htmlspecialchars($interest) . "</li>";
        }
        echo "</ul>";
    } else {
        echo "<p>Nessun interesse selezionato.</p>";
    }
} else {
    echo "<p>Nessun dato ricevuto.</p>";
}
?>