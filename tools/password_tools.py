# function: Check password strength and to Generate Secure Passwords

import re
import secrets
import string
import tkinter as tk

class PasswordTools:

    def check_strength(self, password):
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
            tips.append("Too short - the National Institute of Standards and Technology recommends at least 15 characters")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            tips.append("Add at least one uppercase letter")

        if re.search(r"[0-9]", password):
            score += 1
        else:
            tips.append("Add at least one number")

        levels = {0: "Very Weak", 1: "Very Weak", 2: "Weak",
                  3: "Moderate", 4: "Strong", 5: "Very Strong"}

        result = f"Strength: {levels.get(score, 'Very Strong')} ({length} characters)\n"
        result += "Reminder: Aim for 15+ characters\n"
        if tips:
            result += "\nSuggestions:\n"
            for tip in tips:
                result += f"  - {tip}\n"
        return result

    def generate(self, length=15):
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(secrets.choice(chars) for _ in range(length))
        return password

    def open_window(self, root):
        win = tk.Toplevel(root)
        win.title("Password Tools")
        win.resizable(False, False)

        tk.Label(win, text="Password Tools",
                 font=("Helvetica", 16, "bold"), pady=10).pack()

        # --- Check Strength ---
        tk.Label(win, text="Check Password Strength",
                 font=("Helvetica", 12, "bold")).pack(pady=(10, 0))

        tk.Label(win, text="Enter password:").pack()
        #password_entry = tk.Entry(win, width=40, show="*") (hides password)
        password_entry = tk.Entry(win, width=40)
        password_entry.pack(pady=5)

        output = tk.Text(win, height=8, width=50, state="disabled")
        output.pack(pady=10)

        def check():
            password = password_entry.get()
            if not password:
                return
            result = self.check_strength(password)
            output.config(state="normal")
            output.delete("1.0", tk.END)
            output.insert(tk.END, result)
            output.config(state="disabled")

        tk.Button(win, text="Check Strength", width=20,
                  command=check).pack(pady=5)

        # --- Generate Password ---
        tk.Label(win, text="Generate Password",
                 font=("Helvetica", 12, "bold")).pack(pady=(20, 0))

        tk.Label(win, text="Length (min 15):").pack()
        length_entry = tk.Entry(win, width=10)
        length_entry.insert(0, "15")
        length_entry.pack(pady=5)

        generated_var = tk.StringVar()
        tk.Label(win, textvariable=generated_var,
                 font=("Helvetica", 11), fg="green").pack(pady=5)
        
        def generate():
            try:
                length = max(15, int(length_entry.get()))
            except ValueError:
                length = 15

            password = self.generate(length)
            generated_var.set(f"Generated: {password}")
            copy_btn.config(state="normal")

        tk.Button(win, text="Generate", width=20,
                  command=generate).pack(pady=5)

        def copy():
            password = generated_var.get().replace("Generated: ", "")
            win.clipboard_clear()
            win.clipboard_append(password)
            copy_btn.config(text="Password has been copied.")
            win.after(2000, lambda: copy_btn.config(text="Copy to Clipboard"))

        copy_btn = tk.Button(win, text="Copy to Clipboard", width=20,
                             state="disabled", command=copy)
        copy_btn.pack(pady=5)

