This is a Cybersecurity Toolkit Python GUI program. Inspired by topics I learned in my Security & Information Assurance Class in college.

<p align="center">
  <img src="https://i.imgur.com/eQEZtVq.png" alt="Picture of the program" width="200"/>
</p>

**Password Tools**

Checks password strength based on National Institute of Standards and Technology (NIST) 2026 guidelines (https://cyberunit.com/insights/nist-password-guidelines-2026-update/).
Also allows the user to generate a password with true randomness using the Secrets module in Python.

<table>
  <tr>
    <td><img src="https://i.imgur.com/oKM9GbW.png" alt="Password Check" width="200"/></td>
    <td><img src="https://i.imgur.com/PV5tB0M.png" alt="Generated Password" width="200"/></td>
  </tr>
</table>

**Breach Checker**

Check if a password has appeared in known data breaches using the Have I Been Pwned API. Your password is never sent directly — it uses a k-anonymity model for privacy.

<p align="center">
  <img src="https://i.imgur.com/cns7tJL.png" alt="Breach Checker" width="300"/>
</p>

**File Integrity Monitor**

Open a folder and generate a SHA-256 hash for each file. If a hash changes between scans, the file was tampered with.

<p align="center">
  <img src="https://i.imgur.com/5oGMc2K.png" alt="File Integrity Monitor" width="300"/>
</p>

**Cipher Tools**

Showcases two encryption ciphers plus a brute force cracker for the Caesar Cipher:
- Caesar Cipher: shifts every letter by a number you choose
- Vigenere Cipher: uses a keyword for stronger encryption
- Brute Force Cracker: tries all 25 Caesar shifts automatically to decode an unknown message

<p align="center">
  <img src="https://i.imgur.com/mLhoLRh.png" alt="Cipher Tools" width="300"/>
</p>

## Requirements

- Python 3.10+
- Tkinter (included with Python)

## How to Install & Run

### Step 1 — Make sure Python is installed
You can download it here: https://www.python.org/downloads/

### Step 2 — Download the project
- Click the green **Code** button at the top of this page
- Click **Download ZIP**
- Extract the folder

### Step 3 — Run the app
- **Windows & Mac**: Double-click `main.py`
- After the main.py opens, run the program: the GUI should appear. Enjoy!
