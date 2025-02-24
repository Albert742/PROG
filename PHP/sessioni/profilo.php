<?php
session_start();
if (!isset($_SESSION['username'])) {
    header("Location: index.php");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Profilo</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Profilo</h1>
        <h2>Modifica dati</h2>
        <form action="server.php" method="POST">
            <input type="hidden" name="azione" value="aggiorna">
            Email: <input type="email" name="email" value="<?php echo $_SESSION['email']; ?>" required><br>
            Telefono: <input type="text" name="telefono" value="<?php echo $_SESSION['telefono']; ?>" required><br>
            <button type="submit">Aggiorna</button>
        </form>
        <a href="server.php?azione=logout">Logout</a>
        <?php if (isset($_GET['successo'])) echo "<p>Dati aggiornati con successo</p>"; ?>
    </div>
</body>
</html>