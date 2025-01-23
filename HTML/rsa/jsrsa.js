const MAX_VALUE = 65535;
const E_VALUE = 3;

let publicKey = { n: null, e: E_VALUE };
let privateKey = { n: null, d: null };

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

function ifprime(n) {
    for (let i = 2; i <= Math.floor(n / 2); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

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

function gcd(a, b) {
    if (b === 0) return a;
    return gcd(b, a % b);
}

function getprime() {
    let n;
    do {
        n = Math.floor(Math.random() * MAX_VALUE) + 5;
    } while (!ifprime(n));
    return n;
}

function setprimes(e) {
    let p, q, n, phi;
    do {
        p = getprime();
        do {
            q = getprime();
        } while (p === q);

        n = p * q;
        phi = n - p - q + 1;
    } while (gcd(e, phi) !== 1);

    return { p, q, n, phi };
}

function generateKeys() {
    const e = E_VALUE;
    const { p, q, n, phi } = setprimes(e);
    const d = findD(e, phi);

    publicKey = { n, e };
    privateKey = { n, d };

    console.log(`p: ${p}, q: ${q}, n: ${n}, phi: ${phi}`);
    console.log(`d: ${d}`);
    console.log(`Public Key: (n, e) = (${n}, ${e})`);
    console.log(`Private Key: (n, d) = (${n}, ${d})`);

    document.getElementById('publicKey').innerText = `Chiave Pubblica: (n, e) = (${n}, ${e})`;
    document.getElementById('privateKey').innerText = `Chiave Privata: (n, d) = (${n}, ${d})`;
}

function encryptText() {
    const plaintext = document.getElementById('plaintext').value;
    const { n, e } = publicKey;
    let ciphertext = '';

    for (let i = 0; i < plaintext.length; i++) {
        const c = modpow(plaintext.charCodeAt(i), e, n);
        ciphertext += c + ' ';
    }

    document.getElementById('ciphertext').innerText = 'Testo crittografato: ' + ciphertext.trim();
}

function decryptText() {
    const ciphertext = document.getElementById('ciphertextInput').value.split(' ');
    const { n, d } = privateKey;
    let decryptedText = '';

    for (let i = 0; i < ciphertext.length; i++) {
        const m = modpow(parseInt(ciphertext[i]), d, n);
        decryptedText += String.fromCharCode(m);
    }

    document.getElementById('decryptedText').innerText = 'Testo decrittografato: ' + decryptedText;
}