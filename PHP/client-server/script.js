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
    .then(response => response.text())
    .then(data => {
        if (data.startsWith('Errore:')) {
            document.getElementById('error').innerText = data;
            if (data.includes('Nome prodotto già esistente.')) {
                document.getElementById('productName').style.borderColor = 'red';
            }
        } else {
            document.getElementById('success').innerText = data;
            form.reset();
        }
    });
}

function rimuoviProdotto() {
    const form = document.getElementById('removeProductForm');
    const formData = new FormData(form);
    const removeProductName = document.getElementById('removeProductName').value.trim();

    if (!removeProductName) {
        document.getElementById('removeError').innerText = 'Il nome del prodotto deve essere riempito.';
        return;
    }

    fetch('server.php?action=remove', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        if (data.startsWith('Errore:')) {
            document.getElementById('removeError').innerText = data;
        } else {
            document.getElementById('removeSuccess').innerText = data;
            form.reset();
        }
    });
}

document.getElementById('removeProductName').addEventListener('input', function() {
    document.getElementById('removeError').innerText = '';
    document.getElementById('removeSuccess').innerText = '';
});

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