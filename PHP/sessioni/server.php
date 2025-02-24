<?php
session_start();

function registra($username, $password, $nome, $cognome, $email, $telefono) {
    $dati_utente = "$username,$password,$nome,$cognome,$email,$telefono\n";
    file_put_contents('users.txt', $dati_utente, FILE_APPEND);
}

function autentica($username, $password) {
    $utenti = file('users.txt', FILE_IGNORE_NEW_LINES);
    foreach ($utenti as $utente) {
        list($username_mem, $password_mem, $nome, $cognome, $email, $telefono) = explode(',', $utente);
        if ($username == $username_mem && $password == $password_mem) {
            $_SESSION['username'] = $username;
            $_SESSION['nome'] = $nome;
            $_SESSION['cognome'] = $cognome;
            $_SESSION['email'] = $email;
            $_SESSION['telefono'] = $telefono;
            return true;
        }
    }
    return false;
}

function aggiorna_profilo($email, $telefono) {
    $utenti = file('users.txt', FILE_IGNORE_NEW_LINES);
    $utenti_aggiornati = [];
    foreach ($utenti as $utente) {
        list($username, $password, $nome, $cognome, $email_mem, $telefono_mem) = explode(',', $utente);
        if ($username == $_SESSION['username']) {
            $utente = "$username,$password,$nome,$cognome,$email,$telefono";
            $_SESSION['email'] = $email;
            $_SESSION['telefono'] = $telefono;
        }
        $utenti_aggiornati[] = $utente;
    }
    file_put_contents('users.txt', implode("\n", $utenti_aggiornati) . "\n");
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['azione'])) {
        if ($_POST['azione'] == 'registra') {
            registra($_POST['username'], $_POST['password'], $_POST['nome'], $_POST['cognome'], $_POST['email'], $_POST['telefono']);
            header("Location: index.php");
            exit();
        } elseif ($_POST['azione'] == 'login') {
            if (autentica($_POST['username'], $_POST['password'])) {
                header("Location: profilo.php");
                exit();
            } else {
                header("Location: index.php?errore=1");
                exit();
            }
        } elseif ($_POST['azione'] == 'aggiorna') {
            aggiorna_profilo($_POST['email'], $_POST['telefono']);
            header("Location: profilo.php?successo=1");
            exit();
        }
    }
} elseif ($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['azione']) && $_GET['azione'] == 'logout') {
    session_destroy();
    header("Location: index.php");
    exit();
}
?>