import tkinter as tk
from tkinter import ttk
from deprem_verisi import fetch_afad_data

class ModernApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🌍 AFAD Son Depremler")
        self.geometry("850x550")
        self.configure(bg="#2e2e2e")
        self.setup_ui()

    def setup_ui(self):
        title = tk.Label(self, text="AFAD Son Depremler", font=("Segoe UI", 20, "bold"),
                         bg="#2e2e2e", fg="#c0392b")
        title.pack(pady=15)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#3b3b3b",
                        foreground="white",
                        rowheight=30,
                        fieldbackground="#3b3b3b",
                        font=('Segoe UI', 11))
        style.configure("Treeview.Heading",
                        background="#444",
                        foreground="#c0392b",
                        font=('Segoe UI', 12, 'bold'))
        style.map("Treeview", background=[("selected", "#922b21")])

        frame = tk.Frame(self, bg="#2e2e2e")
        frame.pack(fill=tk.BOTH, expand=True, padx=20)

        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(frame, columns=("Tarih", "Yer", "Büyüklük", "Derinlik"),
                                 show="headings", yscrollcommand=scrollbar.set)

        self.tree.heading("Tarih", text="Tarih")
        self.tree.heading("Yer", text="Yer")
        self.tree.heading("Büyüklük", text="Büyüklük")
        self.tree.heading("Derinlik", text="Derinlik (km)")

        self.tree.column("Tarih", anchor="center", width=150)
        self.tree.column("Yer", anchor="w", width=350)
        self.tree.column("Büyüklük", anchor="center", width=100)
        self.tree.column("Derinlik", anchor="center", width=120)

        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)

        self.button = tk.Button(self, text="🔄 Verileri Yenile", font=("Segoe UI", 11, "bold"),
                                bg="#c0392b", fg="white", activebackground="#a93226",
                                padx=20, pady=8, bd=0, relief=tk.FLAT, command=self.load_data)
        self.button.pack(pady=15)
        self.button.bind("<Enter>", lambda e: self.button.config(bg="#a93226"))
        self.button.bind("<Leave>", lambda e: self.button.config(bg="#c0392b"))

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        data = fetch_afad_data()
        for item in data:
            self.tree.insert("", "end", values=item)
