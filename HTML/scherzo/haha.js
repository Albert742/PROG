function getrolled() {
    setTimeout(function() {
        window.location.href = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';
    }, 5000);
};

document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('bottone');
    const fireworkSounds = [
        document.getElementById('fireworkSound1'),
        document.getElementById('fireworkSound2'),
        document.getElementById('fireworkSound3'),
        document.getElementById('fireworkSound4')
    ];
    const alertSound = document.getElementById('alertSound');
    let tries = 0;
    const maxTries = 20;

    button.addEventListener('click', function() {
        if (tries >= maxTries) {
            alertSound.play();
            alert("Va bene, hai vinto!!! (\u256F\u00B0\u25A1\u00B0)\u256F\uFE35 \u253B\u2501\u253B");
            setTimeout(function() {
                window.location.href = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';
            }, 800);
        } else {
            getrolled();
        }
    });

    document.addEventListener('mousemove', function(event) {
        if (tries >= maxTries) return;

        const rect = button.getBoundingClientRect();
        const distanceX = Math.abs(event.clientX - (rect.left + rect.width / 2));
        const distanceY = Math.abs(event.clientY - (rect.top + rect.height / 2));

        if (distanceX < 150 && distanceY < 150) {
            let x = Math.random() * (window.innerWidth - button.clientWidth);
            let y = Math.random() * (window.innerHeight - button.clientHeight);
            button.style.position = 'absolute';
            button.style.left = x + 'px';
            button.style.top = y + 'px';
            tries++;
        }
        const soundIndex = Math.floor(Math.random() * fireworkSounds.length);
        fireworkSounds[soundIndex].play();
        console.log('Tentativi', tries )
    });
});