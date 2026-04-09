import tkinter as tk

class HelpAbout:

    def open_window(self, root):
        win = tk.Toplevel(root)
        win.title("Help / About")
        win.resizable(False, False)

        tk.Label(win, text="Help / About",
                 font=("Helvetica", 16, "bold"), pady=10).pack()

        tools = [
            ("Password Tools",
             "Check password strength based on National Institute of Standards and Technology 2026 guidelines.\n"
             "This is done via the Secrets module in Python"),

            ("Breach Checker",
             "Checks if a password has appeared in known data breaches."),

            ("File Integrity Monitor",
             "Open a folder and generate a SHA-256 hash for each file.\n"
             "If a hash changes between the scans, the file was tampered with."),

            ("Cipher Tools",
             "Showcases Caesar and Vigenere Ciphers"
             "Caesar cipher — shifts every letter by a number you choose.\n"
             "Vigenere cipher — uses a keyword for stronger encryption.\n"
             "Brute force cracker — tries all 25 Caesar shifts automatically."),
        ]

        for title, description in tools:
            frame = tk.Frame(win, bd=1, relief="groove")
            frame.pack(fill="x", padx=20, pady=5)

            tk.Label(frame, text=title,
                     font=("Helvetica", 12, "bold"),
                     anchor="w").pack(fill="x", padx=10, pady=(8, 2))

            tk.Label(frame, text=description,
                     font=("Helvetica", 10),
                     fg="gray", anchor="w", justify="left",
                     wraplength=400).pack(fill="x", padx=10, pady=(0, 8))

        tk.Button(win, text="Close", width=20,
                  command=win.destroy).pack(pady=(5, 20))
        