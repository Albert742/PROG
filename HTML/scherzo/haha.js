document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('bottone');
    const alertSound = document.getElementById('alertSound');
    let tries = 0;
    const maxTries = 20;
    const content = document.querySelector('.content'); // Ottieni il contenitore

    document.addEventListener('mousemove', function(event) {
        if (tries >= maxTries) return;

        const rect = button.getBoundingClientRect();
        const distanceX = Math.abs(event.clientX - (rect.left + rect.width / 2));
        const distanceY = Math.abs(event.clientY - (rect.top + rect.height / 2));

        if (distanceX < 150 && distanceY < 150) {
            // Calcola le nuove posizioni X e Y all'interno del contenitore
            const contentRect = content.getBoundingClientRect();
            let x = Math.random() * (contentRect.width - button.clientWidth);
            let y = Math.random() * (contentRect.height - button.clientHeight);

            // Imposta le nuove posizioni
            button.style.position = 'absolute';
            button.style.left = x + 'px';
            button.style.top = y + 'px';
            tries++;
        }
        console.log('Tentativi', tries )
    });

    button.addEventListener('click', function() {
        if (tries >= maxTries) {
            alertSound.play();
            alertSound.onended = function() {
                alert("Va bene, hai vinto!!! (\u256F\u00B0\u25A1\u00B0)\u256F\uFE35 \u253B\u2501\u253B");
                window.location.href = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';
            };
        } else {
            getrolled();
        }
    });
});