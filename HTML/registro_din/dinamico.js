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
    ["Beneficiario", "FONDAZIONE ISTITUTO TECNICO SUPERIORE PER LE TECNOLOGIE DELL'INFORMAZIONE E DELLA COMUNICAZIONE 'STEVE JOBS'"],
    ["Titolo Progetto", "WEB & CYBER SECURITY"],
    ["CUP", "E24D23001880006"],
    ["Sede del corso", "CORSO N. 27 - CATANIA (CT)"],
    ["Data di inizio", "06/11/2023"],
    ["Data di conclusione", ""],
    ["Numero ore d'aula", "1080"]
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
container.style.backgroundColor = "rgb(255, 255, 255)";

// Modifica la posizione delle immagini nella header
logo1.style.order = 1;
logo2.style.order = 2;

// Cambia le dimensioni dell'immagine 1
logo1.style.width = "300px"; 
logo1.style.height = "auto";

// Cambia le dimensioni dell'immagine 2
logo2.style.width = "150px";
logo2.style.height = "auto";

// Aggiunge un margine all'immagini
logo1.style.margin = "0px"; 
logo2.style.margin = "0px";

 // Aggiunge un bordo all'immagini
logo1.style.border = "0px solid rgba(255, 255, 255, 0)";
logo2.style.border = "0px solid rgba(255, 255, 255, 0))";
logo1.style.borderRadius = "0px";
logo2.style.borderRadius = "0px";

// Aggiunge un'ombra all'immagini
logo1.style.boxShadow = "0px 0px 0px rgba(255, 255, 255, 0)"; 
logo2.style.boxShadow = "0px 0px 0px rgba(255, 255, 255, 0)";

// Modifica la dimensione delle immagini nella subheader
logo3.style.width = "200px"; // Cambia la larghezza dell'immagine
logo3.style.height = "auto"; // Mantiene l'aspetto proporzionale

// Modifica lo stile del paragrafo principale
mainParagraph.style.color = "rgb(0, 0, 0)";
mainParagraph.style.fontSize = "20pt";

// Modifica lo stile della tabella
table.style.backgroundColor = "rgb(255, 255, 255)";

// Modifica lo stile delle celle della tabella
const tableCells = document.querySelectorAll("table th, table td");
tableCells.forEach(cell => {
    cell.style.border = "1px solid rgb(0, 0, 0)"; // Cambia lo spessore del bordo
    cell.style.padding = "15px"; // Cambia il padding delle celle
    cell.style.backgroundColor = "rgb(255, 255, 255)"; // Cambia il colore di sfondo delle celle
    cell.style.color = "rgb(0, 0, 0)"; // Cambia il colore del testo delle celle
});

// Modifica lo stile del footer
footer.style.backgroundColor = "rgb(255, 255, 255)"; // Cambia il colore di sfondo del footer
footer.style.padding = "10px"; // Cambia il padding del footer

info.style.border = "0px solid rgba(255, 255, 255, 0)"; // Aggiunge un bordo alla sezione info
info.style.color = "rgb(0, 0, 0)"; // Cambia il colore del testo della sezione info
info.style.padding = "10px"; // Cambia il padding della sezione info

// Modifica il testo e lo stile dei paragrafi nella sezione footer
const footerParagraphs = document.querySelectorAll(".footer .firma p");
footerParagraphs.forEach(paragraph => {
    paragraph.style.fontStyle = "arial"; // Cambia lo stile del testo in corsivo
    paragraph.style.color = "rgb(0, 0, 0)"; // Cambia il colore del testo
});



// Modifica lo stile delle firme nel footer
const firmaDivs = document.querySelectorAll(".firma div");
firmaDivs.forEach(div => {
    div.style.border = "0px solid rgba(255, 255, 255, 0)"; // Aggiunge un bordo alle sezioni delle firme
    div.style.padding = "0px"; // Cambia il padding delle sezioni delle firme
});