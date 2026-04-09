import tkinter as tk

class CipherTools:

    def caesar_encrypt(self, m: str, k: int) -> str:
        result = ""
        for ch in m:
            if ch == ' ':
                result += ' '
            else:
                a = ord("A") if ch.isupper() else ord("a")
                result += chr((ord(ch) - a + k) % 26 + a)
        return result

    def caesar_decrypt(self, m: str, k: int) -> str:
        return self.caesar_encrypt(m, -k)

    def brute_force(self, m: str) -> str:
        result = "Brute Force Results:\n\n"
        for k in range(1, 26):
            result += f"  Shift {k:2}: {self.caesar_decrypt(m, k)}\n"
        return result

    def vigenere_encrypt(self, m: str, k: str) -> str:
        result, count = "", 0
        k = k.lower()
        for ch in m:
            if ch == ' ':
                result += ' '
            else:
                shift = ord(k[count % len(k)]) - ord("a")
                result += self.caesar_encrypt(ch, shift)
                count += 1
        return result

    def vigenere_decrypt(self, m: str, k: str) -> str:
        result, count = "", 0
        k = k.lower()
        for ch in m:
            if ch == ' ':
                result += ' '
            else:
                shift = ord(k[count % len(k)]) - ord("a")
                result += self.caesar_decrypt(ch, shift)
                count += 1
        return result

    def open_window(self, root):
        win = tk.Toplevel(root)
        win.title("Cipher Tools")
        win.resizable(False, False)

        tk.Label(win, text="Cipher Tools",
                 font=("Helvetica", 16, "bold"), pady=10).pack()

        # --- Message input ---
        tk.Label(win, text="Message:").pack()
        message_entry = tk.Entry(win, width=50)
        message_entry.pack(pady=5)

        # --- Key input ---
        key_frame = tk.Frame(win)
        key_frame.pack(pady=5)

        tk.Label(key_frame, text="Caesar shift key:").grid(row=0, column=0, padx=5)
        caesar_key = tk.Entry(key_frame, width=5)
        caesar_key.insert(0, "3")
        caesar_key.grid(row=0, column=1, padx=5)

        tk.Label(key_frame, text="Vigenere keyword:").grid(row=0, column=2, padx=5)
        vigenere_key = tk.Entry(key_frame, width=15)
        vigenere_key.insert(0, "SECRET")
        vigenere_key.grid(row=0, column=3, padx=5)

        # --- Output ---
        output = tk.Text(win, height=15, width=60, state="disabled")
        output.pack(pady=10, padx=10)

        def show(result):
            output.config(state="normal")
            output.delete("1.0", tk.END)
            output.insert(tk.END, result)
            output.config(state="disabled")

        def get_message():
            return message_entry.get()

        def get_caesar_key():
            try:
                return int(caesar_key.get())
            except ValueError:
                show("Invalid shift key — must be a number.")
                return None

        def get_vigenere_key():
            k = vigenere_key.get()
            if not k.isalpha():
                show("Invalid keyword — must be letters only.")
                return None
            return k

        # --- Buttons ---
        btn_frame = tk.Frame(win)
        btn_frame.pack(pady=5)

        def caesar_enc():
            m, k = get_message(), get_caesar_key()
            if m and k is not None:
                show(f"Encrypted:\n{self.caesar_encrypt(m, k)}")

        def caesar_dec():
            m, k = get_message(), get_caesar_key()
            if m and k is not None:
                show(f"Decrypted:\n{self.caesar_decrypt(m, k)}")

        def brute():
            m = get_message()
            if m:
                show(self.brute_force(m))

        def vig_enc():
            m, k = get_message(), get_vigenere_key()
            if m and k:
                show(f"Encrypted:\n{self.vigenere_encrypt(m, k)}")

        def vig_dec():
            m, k = get_message(), get_vigenere_key()
            if m and k:
                show(f"Decrypted:\n{self.vigenere_decrypt(m, k)}")

        buttons = [
            ("Caesar Encrypt",       caesar_enc),
            ("Caesar Decrypt",       caesar_dec),
            ("Caesar Brute Force",   brute),
            ("Vigenere Encrypt",     vig_enc),
            ("Vigenere Decrypt",     vig_dec),
        ]

        for i, (label, cmd) in enumerate(buttons):
            tk.Button(btn_frame, text=label, width=20,
                      command=cmd).grid(row=i//3, column=i%3, padx=5, pady=5)

        tk.Button(win, text="Close", width=20,
                  command=win.destroy).pack(pady=(5, 20))