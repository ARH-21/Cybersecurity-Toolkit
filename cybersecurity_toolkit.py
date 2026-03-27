import os
import re
import hashlib
import secrets
import string
import requests # To be used for later function


# ================================
# 1. PASSWORD TOOLS
# ================================

# Common Passwords (To be updated with more)
COMMON_PASSWORDS = [
    "password"]

def check_password_strength(password):
    score = 0
    tips = []
    length = len(password)

    if length >= 20:
        score += 3
    elif length >= 15:
        score += 2
    elif length >= 8:
        score += 1
    else:
        tips.append("Too short - NIST recommends at least 15 characters")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        tips.append("This is a commonly breached password - never use it")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add at least one uppercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        tips.append("Add at least one number")

    levels = {
        0: "Very Weak",
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    rating = levels.get(score, "Very Strong")
    print(f"\n  Strength: {rating} ({length} characters)")
    print(f"Reminder: Aim for 15+ characters")
    if tips:
        print("  Suggestions:")
        for tip in tips:
            print(f"    - {tip}")

def generate_password():
    try:
        user_input = input("\n  Choose password length (press Enter for default 15): ").strip()
        if user_input == "":
            length = 15
        else:
            length = int(user_input)
            if length < 15:
                print("  Too short, adjusted to minimum 15 characters.")
                length = 15
    except ValueError:
        print("  Invalid input. Using default of 15 characters.")
        length = 15

    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(secrets.choice(chars) for _ in range(length))
    print(f"\n  Generated Password: {password}")
    print(f"  Length: {length} characters")

def password_tools():
    while True:
        print("\n=== Password Tools ===")
        print("  1. Check password strength")
        print("  2. Generate a secure password")
        print("  0. Back to menu")
        choice = input("\n  Choose (1-2, 0 to go back): ")

        if choice == "0":
            break
        elif choice == "1":
            while True:
                password = input("\n  Enter password to check (or 0 to go back): ")
                if password == "0":
                    break
                check_password_strength(password)
        elif choice == "2":
            while True:
                generate_password()
                again = input("\n  Generate another? (y/n): ")
                if again.lower() != "y":
                    break
        else:
            print("  Invalid choice.")


# ================================
# 2. FILE INTEGRITY MONITOR
# ================================
def file_integrity_monitor():
    while True:
        print("\n=== File Integrity Monitor ===")
        print("  0. Back to menu")
        folder = input("\n  Enter folder path to monitor (or press Enter for current folder): ").strip()

        if folder == "0":
            break
        if folder == "":
            folder = "."

        if not os.path.exists(folder):
            print("  Folder not found! Try again.")
            continue

        print(f"\n  Scanning '{folder}'...\n")
        hashes = {}

        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                with open(filepath, "rb") as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                hashes[filename] = file_hash
                print(f"  {filename}")
                print(f"    SHA-256: {file_hash}\n")

        print(f"  Total files scanned: {len(hashes)}")
        print("  Complete. If any hash changes, the file was tampered with.")

        again = input("\n  Scan another folder? (y/n): ")
        if again.lower() != "y":
            break


# ================================
# 3. CIPHER TOOLS (Caesar + Vigenere)
# ================================
def c_encrypt(m: str, k: int) -> str:
    """Encrypts a message using Caesar Cipher. Note: M = Plaintext, K = Key, C = Ciphertext."""
    c = ""
    for ch in m:
        if ch == ' ':
            c += ' '
        else:
            if ch.isupper():
                a_start = ord("A")
            else:
                a_start = ord("a")
            n = (ord(ch) - a_start + k) % 26
            c += chr(n + a_start)
    return c

def c_decrypt(m: str, k: int) -> str:
    """Decrypts a Caesar Cipher message."""
    c = ""
    for ch in m:
        if ch == ' ':
            c += ' '
        else:
            if ch.isupper():
                a_start = ord("A")
            else:
                a_start = ord("a")
            n = (ord(ch) - a_start - k) % 26
            c += chr(n + a_start)
    return c

def c_brute_force(m: str):
    """Attempts all 25 Caesar shifts to crack the message."""
    print("\n  Brute forcing all shifts...\n")
    for k in range(1, 26):
        print(f"  Shift {k:2}: {c_decrypt(m, k)}")

def v_encrypt(m: str, k: str) -> str:
    """Encrypts a message using Vigenere Cipher. M = Plaintext, K = Keyword."""
    c = ""
    a_start = ord("a")
    count = 0
    k = k.lower()
    k_length = len(k)
    for ch in m:
        if ch == ' ':
            c += ' '
        else:
            n = ord(k[count % k_length]) - a_start
            c += c_encrypt(ch, n)
            count += 1
    return c

def v_decrypt(m: str, k: str) -> str:
    """Decrypts a Vigenere Cipher message. M = Ciphertext, K = Keyword."""
    c = ""
    a_start = ord("a")
    count = 0
    k = k.lower()
    k_length = len(k)
    for ch in m:
        if ch == ' ':
            c += ' '
        else:
            n = ord(k[count % k_length]) - a_start
            c += c_decrypt(ch, n)
            count += 1
    return c

def cipher_tools():
    while True:
        print("\n=== Cipher Tools ===")
        print("  1. Caesar (Encrypt)")
        print("  2. Caesar (Decrypt)")
        print("  3. Caesar  (Brute Force Crack)")
        print("  4. Vigenere (Encrypt)")
        print("  5. Vigenere (Decrypt)")
        print("  0. Back to menu")
        choice = input("\n  Choose (1-5, 0 to go back): ")

        if choice == "0":
            break
        elif choice == "1":
            m = input("  Enter message: ")
            k = int(input("  Enter shift key (number): "))
            print(f"\n  Encrypted: {c_encrypt(m, k)}")
        elif choice == "2":
            m = input("  Enter message: ")
            k = int(input("  Enter shift key (number): "))
            print(f"\n  Decrypted: {c_decrypt(m, k)}")
        elif choice == "3":
            m = input("  Enter message: ")
            c_brute_force(m)
        elif choice == "4":
            m = input("  Enter message: ")
            k = input("  Enter keyword (ex: MYSECRET): ")
            print(f"\n  Encrypted: {v_encrypt(m, k)}")
        elif choice == "5":
            m = input("  Enter message: ")
            k = input("  Enter keyword (ex:. MYSECRET): ")
            print(f"\n  Decrypted: {v_decrypt(m, k)}")
        else:
            print("Invalid choice.")


# ================================
# 4. HELP / ABOUT
# ================================
def help_about():
    print("""
=============================
     Help / About
=============================

This is a Cybersecurity Toolkit.
The tool has 3 functions:

1. PASSWORD TOOLS
   Check how strong your password is based on NIST (National Institute of Standards and Technology) 2026 guidelines. 
   Additional option to generate a secure password (using the secrets module)

2. FILE INTEGRITY MONITOR
   This will scan a folder and generates a SHA-256 hash for
   each file. If a hash changes, the file was tampered
   with.

3. CIPHER TOOLS
   Ciphers are ways to scramble a message so only
   someone with the key can read it. This is the
   foundation of modern encryption.

   CAESAR CIPHER:
   Shifts every letter by a number you choose (the key).
   Example: "hello" with shift 3 becomes "khoor"
   Simple but easy to crack since there are
   only 25 possible keys.

   VIGENERE CIPHER:
   Like Caesar but uses a whole keyword instead of
   one number. Each letter in your message gets
   shifted by a different amount based on the keyword.
   Example: "attack" with keyword "KEY" is much harder
   to crack than a basic Caesar shift.
   Stronger than Caesar but still breakable.

   BRUTE FORCE CRACKER:
   If someone sends you a Caesar encrypted message
   and you don't know the key, this option tries all 25
   possible shifts automatically.
          
4. HELP / ABOUT
   (You are here)

5. EXIT
   Closes the program.


=============================
    """)
    input("\n  Press Enter to return to menu...")


# ================================
# MAIN MENU
# ================================
def main():
    while True:
        print("\n=============================")
        print("    Cybersecurity Toolkit    ")
        print("=============================")
        print("  1. Password Tools")
        print("  2. File Integrity Monitor")
        print("  3. Cipher Tools")
        print("  4. Help / About")
        print("  5. Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            password_tools()
        elif choice == "2":
            file_integrity_monitor()
        elif choice == "3":
            cipher_tools()
        elif choice == "4":
            help_about()
        elif choice == "5":
            print("\nGoodbye (program is closed)")
            break
        else:
            print("Invalid choice, try again.")

main()
