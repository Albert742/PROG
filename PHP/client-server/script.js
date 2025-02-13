function showSection(sectionId) {
    hideAllSections();
    document.getElementById(sectionId).style.display = 'block';
    if (sectionId === 'viewProducts') {
        viewProducts();
    } else if (sectionId === 'calculateTotal') {
        calculateTotal();
    }
}

function hideAllSections() {
    const sections = document.querySelectorAll('.form-section');
    sections.forEach(section => {
        section.style.display = 'none';
    });
    document.getElementById('productName').style.borderColor = '';
    document.getElementById('error').innerText = '';
    document.getElementById('success').innerText = '';
}

function viewProducts() {
    fetch('server.php?action=view')
        .then(response => response.text())
        .then(data => {
            document.getElementById('viewProductsResult').innerHTML = data;
        });
}

function calculateTotal() {
    fetch('server.php?action=calculate')
        .then(response => response.text())
        .then(data => {
            document.getElementById('calculateTotalResult').innerHTML = data;
        });
}

function insertProduct() {
    const form = document.getElementById('productForm');
    const formData = new FormData(form);
    const productName = document.getElementById('productName').value.trim();
    const quantity = document.getElementById('quantity').value.trim();
    const perishableYes = document.getElementById('perishableYes').checked;
    const perishableNo = document.getElementById('perishableNo').checked;

    if (!productName || !quantity || (!perishableYes && !perishableNo)) {
        document.getElementById('error').innerText = 'Tutti i campi sono obbligatori.';
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

document.getElementById('perishableYes').addEventListener('change', function() {
    document.getElementById('error').innerText = '';
    document.getElementById('success').innerText = '';
});

document.getElementById('perishableNo').addEventListener('change', function() {
    document.getElementById('error').innerText = '';
    document.getElementById('success').innerText = '';
});