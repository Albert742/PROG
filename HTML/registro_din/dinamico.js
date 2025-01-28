// Modifica il titolo della pagina
document.title = "Registro Aula Dinamico";

// Modifica il numero dell'aula
document.querySelector("p b").textContent = "3";

// Modifica il beneficiario
document.querySelectorAll("table th")[0].textContent = "ISTITUTO TECNICO SUPERIORE NUOVO BENEFICIARIO";

// Modifica il titolo del progetto
document.querySelectorAll("table th")[1].textContent = "NUOVO PROGETTO";

// Modifica il CUP
document.querySelectorAll("table th")[2].textContent = "E24D23001880007";

// Modifica la sede del corso
document.querySelectorAll("table th")[3].textContent = "NUOVA SEDE - ROMA (RM)";

// Modifica la data di inizio
document.querySelectorAll("table th")[4].textContent = "01/01/2024";

// Modifica la data di conclusione
document.querySelectorAll("table th")[5].textContent = "31/12/2024";

// Modifica il numero di ore d'aula
document.querySelectorAll("table th")[6].textContent = "1200";

// Modifica il numero di pagine del registro
document.querySelector(".info p b").textContent = "80";
document.querySelectorAll(".info p b")[1].textContent = "1";
document.querySelectorAll(".info p b")[2].textContent = "80";

// Modifica la data nel footer
document.querySelector(".firma div p b").textContent = "12/12/2024";

// Modifica la posizione delle immagini nella header
const headerImages = document.querySelectorAll(".header img");
headerImages[0].style.order = 2; // Sposta la prima immagine a destra
headerImages[1].style.order = 1; // Sposta la seconda immagine a sinistra

// Modifica la dimensione delle immagini nella subheader
const subheaderImage = document.querySelector(".subheader img");
subheaderImage.style.width = "200px"; // Cambia la larghezza dell'immagine
subheaderImage.style.height = "auto"; // Mantiene l'aspetto proporzionale

// Modifica lo stile del paragrafo principale
const mainParagraph = document.querySelector("p");
mainParagraph.style.color = "blue"; // Cambia il colore del testo
mainParagraph.style.fontSize = "20pt"; // Cambia la dimensione del testo

// Modifica lo stile della tabella
const table = document.querySelector("table");
table.style.backgroundColor = "#f0f0f0"; // Cambia il colore di sfondo della tabella

// Modifica lo stile delle celle della tabella
const tableCells = document.querySelectorAll("table th, table td");
tableCells.forEach(cell => {
    cell.style.border = "2px solid #000"; // Cambia lo spessore del bordo
    cell.style.padding = "15px"; // Cambia il padding delle celle
});

// Modifica lo stile del footer
const footer = document.querySelector(".footer");
footer.style.backgroundColor = "#e0e0e0"; // Cambia il colore di sfondo del footer
footer.style.padding = "20px"; // Cambia il padding del footer

// Modifica lo stile delle firme nel footer
const firmaDivs = document.querySelectorAll(".firma div");
firmaDivs.forEach(div => {
    div.style.border = "1px solid #000"; // Aggiunge un bordo alle sezioni delle firme
    div.style.padding = "10px"; // Cambia il padding delle sezioni delle firme
});