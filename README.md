<h1>🖧 Network Classifier</h1>

  <p>A simple desktop application built with Python and <code>tkinter</code> that allows you to:</p>
  <ul>
    <li>Detect the network class (A, B, C, D, E) of your local IP address.</li>
    <li>Classify any external IP address entered manually.</li>
  </ul>

  <h2>📷 Graphical Interface</h2>
  <p>The interface offers two options:</p>
  <ul>
    <li><strong>Find out my network class:</strong> Automatically detects your real local IP and classifies it.</li>
    <li><strong>Classify an external IP:</strong> Prompts you to enter an external IP to determine its network class.</li>
  </ul>

  <h2>🧠 How It Works</h2>
  <p>The app uses the standard IPv4 address class rules:</p>
  <ul>
    <li><strong>Class A:</strong> 1.0.0.0 – 126.255.255.255</li>
    <li><strong>Class B:</strong> 128.0.0.0 – 191.255.255.255</li>
    <li><strong>Class C:</strong> 192.0.0.0 – 223.255.255.255</li>
    <li><strong>Class D:</strong> 224.0.0.0 – 239.255.255.255 (Multicast)</li>
    <li><strong>Class E:</strong> 240.0.0.0 – 254.255.255.255 (Experimental)</li>
  </ul>

  <h2>📦 Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Standard libraries: <code>socket</code>, <code>tkinter</code>, <code>os</code></li>
  </ul>
  <p>No external packages are required.</p>

  <h2>🚀 How to Run</h2>
  <ol>
    <li>Make sure Python is installed.</li>
    <li>Place the <code>logo.png</code> file in the same directory as the script.</li>
    <li>Run the script with:</li>
  </ol>
  <pre><code>python Networks.py</code></pre>

  <h2>🖼️ Custom Icon</h2>
  <p>The app uses a <code>logo.png</code> file as the window icon. Ensure it’s in the same folder as the script.</p>

  <h2>📂 Project Structure</h2>
  <pre><code>NetworkClassifier/
├── Networks.py
└── logo.png
</code></pre>

  <h2>📌 Notes</h2>
  <ul>
    <li>The app retrieves the actual local IP address, not internal loopback addresses like <code>127.0.0.1</code>.</li>
    <li>Only valid IPv4 addresses are supported.</li>
  </ul>

  <h2>🛠️ Author</h2>
  <p>Developed for educational purposes by <strong>Alexey Tenllado</strong>.</p>
