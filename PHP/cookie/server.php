<?php
session_start();

$filename = 'users.txt';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $action = $_GET['action'];
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($action == 'register') {
        $name = $_POST['name'];
        $surname = $_POST['surname'];
        $email = $_POST['email'];
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        // Salvataggio delle informazioni dell'utente nel file
        $user_data = [
            'username' => $username,
            'name' => $name,
            'surname' => $surname,
            'email' => $email,
            'password' => $hashed_password
        ];

        $users = leggiUtentiDaFile($filename);
        $users[$username] = $user_data;
        scriviUtentiSuFile($filename, $users);

        // Salvataggio delle informazioni dell'utente nella sessione
        $_SESSION['username'] = $username;
        $_SESSION['name'] = $name;
        $_SESSION['surname'] = $surname;
        $_SESSION['email'] = $email;

        // Creazione del cookie
        $expire = time() + 120;
        setcookie("user", $username, $expire);
        setcookie("user_expire", $expire, $expire);

        // Redirezione alla pagina info.php
        header("Location: Info.php");
        exit();
    } elseif ($action == 'login') {
        $users = leggiUtentiDaFile($filename);

        // Verifica se l'utente esiste nel file
        if (isset($users[$username]) && password_verify($password, $users[$username]['password'])) {
            // Salvataggio delle informazioni dell'utente nella sessione
            $_SESSION['username'] = $username;
            $_SESSION['name'] = $users[$username]['name'];
            $_SESSION['surname'] = $users[$username]['surname'];
            $_SESSION['email'] = $users[$username]['email'];

            // Creazione del cookie
            $expire = time() + 120;
            setcookie("user", $username, $expire);
            setcookie("user_expire", $expire, $expire);

            // Redirezione alla pagina info.php
            header("Location: Info.php");
            exit();
        } else {
            echo "Nome utente o password errati!";
        }
    }
} elseif (isset($_GET['action']) && $_GET['action'] == 'logout') {
    // Gestione del logout
    session_unset();
    session_destroy();

    // Cancellazione del cookie
    setcookie("user", "", time() - 3600);
    setcookie("user_expire", "", time() - 3600);

    // Redirezione alla pagina di login
    header("Location: index.html");
    exit();
}

function leggiUtentiDaFile($filename) {
    $users = [];
    if (file_exists($filename)) {
        $file = fopen($filename, 'r');
        while (($line = fgets($file)) !== false) {
            $user = json_decode($line, true);
            $users[$user['username']] = $user;
        }
        fclose($file);
    }
    return $users;
}

function scriviUtentiSuFile($filename, $users) {
    $file = fopen($filename, 'w');
    foreach ($users as $user) {
        fwrite($file, json_encode($user) . PHP_EOL);
    }
    fclose($file);
}
?>