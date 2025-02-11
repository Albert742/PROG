<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Test Page</title>
</head>
<body>

    <h1>PHP Test</h1>

    <?php
    // Variables
    $name = "John Doe";
    $age = 30;

    // Output with variables
    echo "<p>Hello, my name is " . $name . " and I am " . $age . " years old.</p>";

    // Conditional statement
    if ($age >= 18) {
        echo "<p>I am an adult.</p>";
    } else {
        echo "<p>I am a minor.</p>";
    }

    // Loop
    echo "<ul>";
    for ($i = 1; $i <= 5; $i++) {
        echo "<li>Item " . $i . "</li>";
    }
    echo "</ul>";
    ?>

</body>
</html>