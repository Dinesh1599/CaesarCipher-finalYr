<h2>📖 Overview</h2>
<p>This project is a Python-based desktop application built using <strong>PyQt5</strong> that provides a simple yet robust GUI for text encryption and decryption. It utilizes a multi-layer custom encryption algorithm, combining rotation, substitution, and key-based transformations, making the process highly secure and complex to reverse without the correct key.</p>
<p>The demo file for this project is present in the <strong>Dynamic Caesar Cipher</strong> folder with the file name <strong>Dynamic Caesar Cipher</strong>.</p>

<h2>✨ Features</h2>
<ul>
    <li><strong>Encryption</strong>: Convert any input message into encrypted ciphertext.</li>
    <li><strong>Decryption</strong>: Decode encrypted messages using a stored key.</li>
    <li><strong>Dynamic Key Generation</strong>: Keys based on timestamp, machine IP, and geographical data.</li>
    <li><strong>Key Export</strong>: Save generated keys securely in <code>.ldt</code> files.</li>
    <li><strong>Internet Connectivity Check</strong>: Ensures internet access for geo-location.</li>
    <li><strong>Error Handling & Pop-ups</strong>: User-friendly guidance dialogs.</li>
</ul>

<h2>🔎 How It Works</h2>
<h3>1. Encryption Process</h3>
<p>Verifies internet connectivity, generates keys, applies multiple layers of encryption, and saves key metadata in an <code>.ldt</code> file.</p>

<h3>2. Decryption Process</h3>
<p>Uses the <code>.ldt</code> file and user input ciphertext to reverse the encryption process and display the original message.</p>

<h3>3. Core Logic Components</h3>
<ul>
    <li>Rotation & Reverse Rotation</li>
    <li>Key Generation with modular arithmetic</li>
    <li>File handling and validations</li>
    <li>Intuitive GUI interaction</li>
</ul>

<h2>🛠 Technologies Used</h2>
<ul>
    <li>Python 3.x</li>
    <li>PyQt5</li>
    <li>geocoder</li>
    <li>socket, OS, sys modules</li>
</ul>

<h2>💻 How to Run</h2>
<pre><code>pip install PyQt5 geocoder
python demoModel.py
<h2>🚀 Future Upgrades</h2>
<ul>
    <li>Support for AES/RSA encryption layers</li>
    <li>File encryption/decryption support</li>
    <li>Cross-platform executable builds</li>
    <li>Modern UI enhancements and dark mode</li>
    <li>Multi-language UI support</li>
</ul>


