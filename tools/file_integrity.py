import os
import hashlib
import tkinter as tk
from tkinter import filedialog

class FileIntegrityMonitor:

    def scan(self, folder):
        hashes = {}
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                with open(filepath, "rb") as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                hashes[filename] = file_hash
        return hashes

    def open_window(self, root):
        win = tk.Toplevel(root)
        win.title("File Integrity Monitor")
        win.resizable(False, False)

        tk.Label(win, text="File Integrity Monitor",
                 font=("Helvetica", 16, "bold"), pady=10).pack()

        tk.Label(win, text="Select a folder to scan its SHA-256 hashes.",
                 font=("Helvetica", 11), fg="gray").pack(pady=(0, 10))

        folder_var = tk.StringVar()
        folder_var.set("No folder selected")

        tk.Label(win, textvariable=folder_var,
                 font=("Helvetica", 10), fg="blue").pack(pady=5)

        output = tk.Text(win, height=20, width=60, state="disabled")
        output.pack(pady=10, padx=10)

        def select_and_scan():
            folder_root = tk.Tk()
            folder_root.withdraw()
            folder_root.lift()
            folder_root.attributes('-topmost', True)
            folder = filedialog.askdirectory(title="Select folder to scan")
            folder_root.destroy()

            if not folder:
                return

            folder_var.set(f"Scanning: {folder}")
            hashes = self.scan(folder)

            output.config(state="normal")
            output.delete("1.0", tk.END)

            if not hashes:
                output.insert(tk.END, "No files found in this folder.\n")
            else:
                for filename, file_hash in hashes.items():
                    output.insert(tk.END, f"{filename}\n")
                    output.insert(tk.END, f"  SHA-256: {file_hash}\n\n")
                output.insert(tk.END, f"Total files scanned: {len(hashes)}\n")
                output.insert(tk.END, "Complete. If any hash was changed, the file was tampered with.")

            output.config(state="disabled")
            folder_var.set(f"Scanned: {folder}")

        tk.Button(win, text="Select Folder & Scan", width=25,
                  command=select_and_scan).pack(pady=5)

        tk.Button(win, text="Close", width=25,
                  command=win.destroy).pack(pady=(5, 20))