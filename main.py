import tkinter as tk
from tools.password_tools import PasswordTools
from tools.file_integrity import FileIntegrityMonitor
from tools.cipher_tools import CipherTools
from tools.breach_checker import BreachChecker
from tools.help_about import HelpAbout

def main():
    root = tk.Tk()
    root.title("Cybersecurity Toolkit") # window name
    root.resizable(False, False)

    tk.Label(
        root,
        text="Cybersecurity Toolkit",
        font=("Arial", 18, "bold"),
        pady=10
    ).pack()

    tk.Label(
        root,
        text="Select a tool to get started",
        font=("Arial", 11),
        fg="gray"
    ).pack(pady=(0, 20))

    tools = [
        ("Password Tools",        PasswordTools),
        ("Password Breach Checker",        BreachChecker),
        ("File Integrity Monitor", FileIntegrityMonitor),
        ("Cipher Tools",          CipherTools),
        ("Help / About",          HelpAbout),
        # TBA
        # TBA
    ]

    for label, ToolClass in tools:
        tk.Button(
            root,
            text=label,
            width=30,
            pady=8,
            command=lambda cls=ToolClass: cls().open_window(root)
        ).pack(pady=5)

    tk.Button(
        root,
        text="Exit",
        width=30,
        pady=8,
        fg="red",
        command=root.quit
    ).pack(pady=(5, 20))

    root.mainloop()

if __name__ == "__main__":
    main()