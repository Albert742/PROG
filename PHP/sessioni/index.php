<!DOCTYPE html>
<html>
<head>
    <title>Registrazione e Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Registrazione</h1>
        <form action="server.php" method="POST">
            <input type="hidden" name="azione" value="registra">
            Nome: <input type="text" name="nome" required><br>
            Cognome: <input type="text" name="cognome" required><br>
            Email: <input type="email" name="email" required><br>
            Telefono: <input type="text" name="telefono" required><br>
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <button type="submit">Registrati</button>
        </form>

        <h1>Login</h1>
        <form action="server.php" method="POST">
            <input type="hidden" name="azione" value="login">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <button type="submit">Login</button>
        </form>
        <?php if (isset($_GET['errore'])) echo "<p>Username o password errati</p>"; ?>
    </div>
</body>
</html>