<!-- filepath: /c:/Users/alber/Desktop/PROG/PHP/cookie/Info.php -->
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informazioni Utente</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: rgb(0, 0, 0);
        }
        p {
            font-size: 18px;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #f44336;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        a:hover {
            background-color: #d32f2f;
        }
        .cookie-section {
            margin-top: 40px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        .cookie-section h2 {
            color: #4CAF50;
        }
    </style>
    <script>
        function checkCookieExpiration() {
            var expire = <?php echo isset($_COOKIE['user_expire']) ? $_COOKIE['user_expire'] : 0; ?>;
            var currentTime = Math.floor(Date.now() / 1000);
            if (currentTime > expire) {
                alert("Sessione scaduta. Verrai reindirizzato alla pagina di login.");
                window.location.href = "index.html";
            }
        }

        setInterval(checkCookieExpiration, 5000);
    </script>
</head>
<body>
    <div>
        <h1>Informazioni Utente</h1>
    </div>
    <?php
    session_start();
    if (isset($_COOKIE['user']) && isset($_SESSION['username'])) {
        $expire = isset($_COOKIE['user_expire']) ? $_COOKIE['user_expire'] : 0;
        if (time() > $expire) {
            echo "<p>Sessione scaduta. Verrai reindirizzato alla pagina di login.</p>";
            header("Refresh: 3; url=index.html");
            exit();
        }

        echo "<p>Nome: " . $_SESSION['name'] . "</p>";
        echo "<p>Cognome: " . $_SESSION['surname'] . "</p>";
        echo "<p>Username: " . $_SESSION['username'] . "</p>";
        echo "<p>Email: " . $_SESSION['email'] . "</p>";
        echo '<a href="server.php?action=logout">Logout</a>';

        echo '<div class="cookie-section">';
        echo '<h2>Dati del Cookie</h2>';
        $cookie_keys = ['user', 'user_expire', 'PHPSESSID', 'token'];
        foreach ($cookie_keys as $key) {
            if (isset($_COOKIE[$key])) {
                echo "<p>$key: " . htmlspecialchars($_COOKIE[$key]) . "</p>";
            }
        }
        $expire = isset($_COOKIE['user_expire']) ? date('Y-m-d H:i:s', $_COOKIE['user_expire']) : 'N/A';
        echo "<p>Expire: $expire</p>";
        echo "<p>Domain: " . $_SERVER['HTTP_HOST'] . "</p>";
        echo "<p>Secure: " . (isset($_SERVER['HTTPS']) ? 'Yes' : 'No') . "</p>";
        echo '</div>';
    } else {
        echo "<p>Accesso non autorizzato. Effettua il login.</p>";
        header("Refresh: 3; url=index.html");
    }
    ?>
</body>
</html>