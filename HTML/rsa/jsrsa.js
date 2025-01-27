const MAX_VALUE = 65535;
const E_VALUE = 3;

let publicKey = { n: null, e: E_VALUE };
let privateKey = { n: null, d: null, p: null, q: null };

function modpow(base, power, mod) {
    let result = 1;
    for (let i = 0; i < power; i++) {
        result = (result * base) % mod;
    }
    return result;
}

function inverse(a, mod) {
    let aprev = mod, iprev = mod, i = 1, atemp, itemp;

    while (a !== 1) {
        atemp = a;
        itemp = i;
        a = aprev - Math.floor(aprev / atemp) * a;
        i = iprev - Math.floor(aprev / atemp) * i;
        aprev = atemp;
        iprev = itemp;
        while (i < 0) i += mod;
    }

    return i;
}

function ifprime(n) {
    for (let i = 2; i <= Math.floor(n / 2); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

function gcd(num1, num2) {
    let temp;
    if (num1 > num2) {
        temp = num1;
        num1 = num2;
        num2 = temp;
    }
    for (let i = num1; i > 0; i--) {
        if (num1 % i === 0 && num2 % i === 0) {
            return i;
        }
    }
    return 1;
}

function getprime() {
    let n;
    do {
        n = Math.floor(Math.random() * MAX_VALUE) + 5;
    } while (!ifprime(n));
    return n;
}

function findD(e, phi) {
    let eprev = phi, dprev = phi, d = 1, etemp, dtemp;

    while (e !== 1) {
        etemp = e;
        dtemp = d;
        e = eprev - Math.floor(eprev / etemp) * e;
        d = dprev - Math.floor(eprev / etemp) * d;
        eprev = etemp;
        dprev = dtemp;
        while (d < 0) d += phi;
    }

    return d;
}

function setprimes(e) {
    let p, q, n, phi;
    do {
        p = getprime();
        do {
            q = getprime();
        } while (p === q);

        n = p * q;
        phi = (p - 1) * (q - 1);
    } while (gcd(e, phi) !== 1);

    return { p, q, n, phi };
}

function generateKeys() {
    const e = E_VALUE;
    const { p, q, n, phi } = setprimes(e);
    const d = findD(e, phi);

    publicKey = { n, e };
    privateKey = { n, d, p, q };

    console.log('Chiave Pubblica:', publicKey);
    console.log('Chiave Privata:', privateKey);

    document.getElementById('publicKey').innerText = `Chiave Pubblica: (n, e) = (${n}, ${e})`;
    document.getElementById('privateKey').innerText = `Chiave Privata: (n, d) = (${n}, ${d})`;
}

function encryptText() {
    const plaintext = document.getElementById('plaintext').value;
    const n = publicKey.n;
    const e = publicKey.e;

    let ciphertext = '';

    for (let i = 0; i < plaintext.length; i++) {
        const c = modpow(plaintext.charCodeAt(i), e, n);
        ciphertext += c + ' ';
    }

    console.log('Testo in chiaro:', plaintext);
    console.log('Testo cifrato:', ciphertext.trim());

    document.getElementById('ciphertext').innerText = `Testo cifrato: ${ciphertext.trim()}`;
}

function decryptText() {
    const ciphertextInput = document.getElementById('ciphertextInput').value;
    const ciphertextArray = ciphertextInput.split(' ').map(Number);
    const n = privateKey.n;
    const d = privateKey.d;
    const p = privateKey.p;
    const q = privateKey.q;

    let decryptedText = '';

    ciphertextArray.forEach(c => {
        const dP = d % (p - 1);
        const dQ = d % (q - 1);
        const qInv = inverse(q, p);
        const m1 = modpow(c, dP, p);
        const m2 = modpow(c, dQ, q);
        let m1m2 = m1 - m2;
        if (m1m2 < 0) m1m2 += p;
        const h = (qInv * m1m2) % p;
        const m = m2 + h * q;
        decryptedText += String.fromCharCode(m);
    });

    console.log('Testo da decriptare:', ciphertextArray);
    console.log('Testo decriptato:', decryptedText);

    document.getElementById('decryptedText').innerText = `Testo decriptato: ${decryptedText}`;
}