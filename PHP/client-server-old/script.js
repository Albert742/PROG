function mostraSezione(sectionId) {
    nascondiTutteLeSezioni();
    document.getElementById(sectionId).style.display = 'block';
    if (sectionId === 'visualizzaProdotti') {
        visualizzaProdotti();
    } else if (sectionId === 'calcolaTotale') {
        calcolaTotale();
    }
}

function nascondiTutteLeSezioni() {
    const sections = document.querySelectorAll('.form-section');
    sections.forEach(section => {
        section.style.display = 'none';
    });
    document.getElementById('productName').style.borderColor = '';
    document.getElementById('error').innerText = '';
    document.getElementById('success').innerText = '';
}

function visualizzaProdotti() {
    fetch('server.php?action=view')
        .then(response => response.text())
        .then(data => {
            document.getElementById('visualizzaProdottiResult').innerHTML = data;
        });
}

function calcolaTotale() {
    fetch('server.php?action=calculate')
        .then(response => response.text())
        .then(data => {
            document.getElementById('calcolaTotaleResult').innerHTML = data;
        });
}

function inserisciProdotto() {
    const form = document.getElementById('productForm');
    const formData = new FormData(form);
    const productName = document.getElementById('productName').value.trim();
    const quantity = document.getElementById('quantity').value.trim();
    const deperibileSi = document.getElementById('deperibileSi').checked;
    const deperibileNo = document.getElementById('deperibileNo').checked;

    if (!productName || !quantity || (!deperibileSi && !deperibileNo)) {
        document.getElementById('error').innerText = 'Tutti i campi deve essere riempiti.';
        return;
    }

    fetch('server.php?action=insert', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            const errorMessage = data.field === 'name' ? 'Nome prodotto già esistente.' : 'ID prodotto già esistente.';
            document.getElementById('error').innerText = errorMessage;
            if (data.field === 'name') {
                document.getElementById('productName').style.borderColor = 'red';
            }
        } else {
            document.getElementById('success').innerText = 'Prodotto inserito con successo.';
            form.reset();
        }
    });
}

document.getElementById('productName').addEventListener('input', function() {
    document.getElementById('productName').style.borderColor = '';
    document.getElementById('error').innerText = '';
    document.getElementById('success').innerText = '';
});

document.getElementById('quantity').addEventListener('input', function() {
    document.getElementById('error').innerText = '';
    document.getElementById('success').innerText = '';
});

document.getElementById('deperibileSi').addEventListener('change', function() {
    document.getElementById('error').innerText = '';
    document.getElementById('success').innerText = '';
});

document.getElementById('deperibileNo').addEventListener('change', function() {
    document.getElementById('error').innerText = '';
    document.getElementById('success').innerText = '';
});