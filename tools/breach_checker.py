import hashlib
import requests
import tkinter as tk
import threading

class BreachChecker:

    API_URL = "https://api.pwnedpasswords.com/range/"

    def check(self, password: str) -> int:
        sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        prefix, suffix = sha1[:5], sha1[5:]

        try:
            response = requests.get(self.API_URL + prefix, timeout=5)
            response.raise_for_status()
        except requests.exceptions.ConnectionError:
            return -1
        except requests.exceptions.Timeout:
            return -2
        except requests.exceptions.HTTPError as e:
            return -3

        for line in response.text.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)
        return 0

    def open_window(self, root):
        win = tk.Toplevel(root)
        win.title("Breach Checker")
        win.resizable(False, False)

        tk.Label(win, text="Password Breach Checker",
                 font=("Helvetica", 16, "bold"), pady=10).pack()

        tk.Label(win,
        text='''Note: Your password will not be sent to anyone. The API uses k-anonymity.
    Your password is hashed locally.
    Only the first 5 characters of the hash are sent.
    The API returns a list of matching hashes.
    This program checks locally if your full hash is in that list.''',
                 font=("Helvetica", 10), fg="gray").pack(pady=(0, 10))


        # Input/Output
        tk.Label(win, text="Enter password to check:").pack()
        password_entry = tk.Entry(win, width=40)
        password_entry.pack(pady=5)

        output = tk.Text(win, height=8, width=50, state="disabled")
        output.pack(pady=10, padx=10)

        status_var = tk.StringVar()
        status_var.set("")
        tk.Label(win, textvariable=status_var,
                 font=("Helvetica", 10), fg="gray").pack()

        def show(result, color="black"):
            output.config(state="normal")
            output.delete("1.0", tk.END)
            output.insert(tk.END, result)
            output.config(state="disabled", fg=color)

        def run_check():
            password = password_entry.get()
            if not password:
                show("Please enter a password.", "red")
                return

            status_var.set("Checking Password...")
            check_btn.config(state="disabled")

            def task():
                count = self.check(password)

                if count == -1:
                    result = "Error: Please be connected to the Internet."
                    color = "red"
                elif count == -2:
                    result = "Request timed out. Please try again."
                    color = "red"
                elif count == -3:
                    result = "Error. Please try again."
                    color = "red"
                elif count == 0:
                    result = "Good news! This password has not been\nfound in any known data breaches."
                    color = "green"
                elif count < 100:
                    result = f"Warning: This password has been seen\n{count} times in data breaches.\nConsider changing it."
                    color = "orange"
                else:
                    result = f"DANGER: This password has been seen\n{count:,} times in data breaches.\nDo not use this password!"
                    color = "red"

                win.after(0, lambda: show(result, color))
                win.after(0, lambda: status_var.set(""))
                win.after(0, lambda: check_btn.config(state="normal"))

            # This has been added so this function doesn't run slow
            threading.Thread(target=task, daemon=True).start()

        check_btn = tk.Button(win, text="Check Password", width=20,
                              command=run_check)
        check_btn.pack(pady=5)

        tk.Button(win, text="Close", width=20,
                  command=win.destroy).pack(pady=(10, 20))