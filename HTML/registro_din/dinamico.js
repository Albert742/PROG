// Crea il contenitore principale
const container = document.createElement("div");
container.className = "container";

// Crea la sezione header
const header = document.createElement("div");
header.className = "header";
const logo1 = document.createElement("img");
logo1.src = "logo1.jpg";
logo1.alt = "Logo 1";
const logo2 = document.createElement("img");
logo2.src = "logo2.jpg";
logo2.alt = "Logo 2";
header.appendChild(logo1);
header.appendChild(logo2);

// Crea la sezione subheader
const subheader = document.createElement("div");
subheader.className = "subheader";
const logo3 = document.createElement("img");
logo3.src = "logo3.png";
logo3.alt = "Logo 3";
subheader.appendChild(logo3);

// Crea il paragrafo principale
const mainParagraph = document.createElement("p");
mainParagraph.innerHTML = 'REGISTRO AULA n. <b>2</b>';

// Crea la tabella
const table = document.createElement("table");
const rows = [
    ["Beneficiario", "Ciao"],
    ["Titolo Progetto", ""],
    ["CUP", ""],
    ["Sede del corso", ""],
    ["Data di inizio", ""],
    ["Data di conclusione", ""],
    ["Numero ore d'aula", ""]
];
rows.forEach(rowData => {
    const row = document.createElement("tr");
    const cell1 = document.createElement("td");
    cell1.textContent = rowData[0];
    const cell2 = document.createElement("th");
    cell2.textContent = rowData[1];
    row.appendChild(cell1);
    row.appendChild(cell2);
    table.appendChild(row);
});

// Crea la sezione footer
const footer = document.createElement("div");
footer.className = "footer";

// Crea la sezione info nel footer
const info = document.createElement("div");
info.className = "info";
const infoParagraph = document.createElement("p");
infoParagraph.innerHTML = 'Il presente Registro si compone di <b>70</b> pagine, numerate dalla <b>1</b> alla <b>70</b> e regolarmente vidimate.';
info.appendChild(infoParagraph);

// Crea la sezione firma nel footer
const firma = document.createElement("div");
firma.className = "firma";
const firmaData = document.createElement("div");
const firmaDataParagraph = document.createElement("p");
firmaDataParagraph.innerHTML = 'Data <b>11/08/2024</b>';
firmaData.appendChild(firmaDataParagraph);
const firmaTimbroEnte = document.createElement("div");
const firmaTimbroEnteParagraph = document.createElement("p");
firmaTimbroEnteParagraph.textContent = 'Timbro ENTE';
firmaTimbroEnte.appendChild(firmaTimbroEnteParagraph);
const firmaTimbroFirma = document.createElement("div");
const firmaTimbroFirmaParagraph1 = document.createElement("p");
firmaTimbroFirmaParagraph1.textContent = 'Timbro e Firma';
const firmaTimbroFirmaParagraph2 = document.createElement("p");
firmaTimbroFirmaParagraph2.textContent = '____________________';
firmaTimbroFirma.appendChild(firmaTimbroFirmaParagraph1);
firmaTimbroFirma.appendChild(firmaTimbroFirmaParagraph2);
firma.appendChild(firmaData);
firma.appendChild(firmaTimbroEnte);
firma.appendChild(firmaTimbroFirma);

// Aggiungi tutte le sezioni al container
footer.appendChild(info);
footer.appendChild(firma);
container.appendChild(header);
container.appendChild(subheader);
container.appendChild(mainParagraph);
container.appendChild(table);
container.appendChild(footer);

// Aggiungi il container al root
document.getElementById("root").appendChild(container);

// Modifica dinamicamente lo stile degli elementi

// Modifica il colore di sfondo del container
container.style.backgroundColor = "rgb(243, 10, 10)";

// Modifica la posizione delle immagini nella header
logo1.style.order = 2; // Sposta la prima immagine a destra
logo2.style.order = 1; // Sposta la seconda immagine a sinistra
logo1.style.width = "100px"; // Cambia la larghezza dell'immagine
logo1.style.height = "auto"; // Mantiene l'aspetto proporzionale
logo2.style.width = "100px"; // Cambia la larghezza dell'immagine
logo2.style.height = "auto"; // Mantiene l'aspetto proporzionale
logo1.style.margin = "20px"; // Aggiunge un margine all'immagine di sinistra
logo2.style.margin = "20px"; // Aggiunge un margine all'immagine di destra
logo1.style.border = "2px solid rgb(255, 14, 14)"; // Aggiunge un bordo all'immagine di sinistra
logo2.style.border = "2px solid rgba(0, 255, 213, 0.94)"; // Aggiunge un bordo all'immagine di destra
logo1.style.borderRadius = "10px"; // Aggiunge un bordo arrotondato all'immagine di sinistra
logo2.style.borderRadius = "10px"; // Aggiunge un bordo arrotondato all'immagine di destra
logo1.style.boxShadow = "5px 5px 15px rgb(166, 255, 0)"; // Aggiunge un'ombra all'immagine di sinistra
logo2.style.boxShadow = "5px 5px 15px rgba(0, 174, 255, 0.43)"; // Aggiunge un'ombra all'immagine di destra
logo1.style.transition = "transform 0.3s"; // Aggiunge una transizione all'immagine di sinistra
logo2.style.transition = "transform 0.3s"; // Aggiunge una transizione all'immagine di destra

// Modifica la dimensione delle immagini nella subheader
logo3.style.width = "200px"; // Cambia la larghezza dell'immagine
logo3.style.height = "auto"; // Mantiene l'aspetto proporzionale
logo3.style.opacity = "0.5"; // Imposta l'opacità al 50%

// Modifica lo stile del paragrafo principale
mainParagraph.style.color = "rgba(0, 30, 94, 0.77)"; // Cambia il colore del testo
mainParagraph.style.fontSize = "20pt"; // Cambia la dimensione del testo

// Modifica lo stile della tabella
table.style.backgroundColor = "rgba(37, 139, 255, 0.41)"; // Cambia il colore di sfondo della tabella

// Modifica lo stile delle celle della tabella
const tableCells = document.querySelectorAll("table th, table td");
tableCells.forEach(cell => {
    cell.style.border = "2px solid rgb(86, 211, 149)"; // Cambia lo spessore del bordo
    cell.style.padding = "15px"; // Cambia il padding delle celle
    cell.style.backgroundColor = "rgb(77, 211, 0)"; // Cambia il colore di sfondo delle celle
    cell.style.color = "rgb(255, 53, 131)"; // Cambia il colore del testo delle celle
});

// Modifica lo stile del footer
footer.style.backgroundColor = "rgb(68, 44, 44)"; // Cambia il colore di sfondo del footer
footer.style.padding = "20px"; // Cambia il padding del footer

// Modifica il testo e lo stile dei paragrafi nella sezione footer
const footerParagraphs = document.querySelectorAll(".footer .firma p");
footerParagraphs.forEach(paragraph => {
    paragraph.style.fontStyle = "italic"; // Cambia lo stile del testo in corsivo
    paragraph.style.color = "rgba(0, 255, 170, 0.4)"; // Cambia il colore del testo
});

// Modifica lo stile delle firme nel footer
const firmaDivs = document.querySelectorAll(".firma div");
firmaDivs.forEach(div => {
    div.style.border = "1px solid rgba(207, 155, 255, 0.97)"; // Aggiunge un bordo alle sezioni delle firme
    div.style.padding = "10px"; // Cambia il padding delle sezioni delle firme
});