import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import List, Dict, Tuple, Any
from database import Database


class GUIElements:
    def __init__(self, parent: tk.Tk, db: Database):
        self.parent = parent
        self.db = db
        self.selected_item: Tuple[Any, ...] = None

        self.create_gui_elements()

    def create_gui_elements(self) -> None:
        # Frame voor de inputvelden en labels
        input_frame = tk.Frame(self.parent)
        input_frame.grid(row=0, column=0, sticky="nsew")

        # Maak labels en inputvelden
        labels = ["Titel", "Medium", "Afmeting", "Categorie", "Jaar", "Prijs"]
        self.entries: Dict[str, tk.Entry] = {}
        for index, label in enumerate(labels):
            tk.Label(input_frame, text=label).grid(row=index, column=0)
            entry = tk.Entry(input_frame, width=20)
            entry.grid(row=index, column=1)
            self.entries[label.lower()] = entry

        # Database tabel
        self.tree = ttk.Treeview(self.parent, columns=labels, show="headings")
        for label in labels:
            self.tree.heading(label, text=label)
        self.tree.grid(row=1, column=0, columnspan=2)

        # Bind event handler om geselecteerd item bij te werken
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Laad gegevens in de tabel
        self.load_data()

        # Knoppen
        button_frame = tk.Frame(self.parent)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # Knoppen en bijbehorende functies
        buttons = [
            ("Toevoegen", self.on_add),
            ("Bijwerken", self.on_update),
            ("Verwijderen", self.on_delete),
            ("Filteren", self.on_filter),
        ]
        for index, (text, command) in enumerate(buttons):
            tk.Button(button_frame, text=text, command=command).grid(
                row=0, column=index, padx=(0, 10)
            )

    def load_data(self) -> None:
        # Verwijder alle items uit de tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Voeg items uit de database toe aan de tabel
        for item in self.db.get_all():
            self.tree.insert("", "end", values=item)

    def on_tree_select(self, event: tk.Event) -> None:
        item = self.tree.selection()[0]
        self.selected_item = self.tree.item(item)["values"]

        # Vul de invoervelden met de gegevens van het geselecteerde item
        for index, key in enumerate(self.entries):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, str(self.selected_item[index]))

    def on_add(self) -> None:
        # Haal de gegevens op uit de inputvelden en voeg ze toe aan de database
        data = tuple(entry.get() for entry in self.entries.values())
        self.db.insert(data)
        self.load_data()

    def on_update(self) -> None:
        # Werk het geselecteerde item bij met de gegevens uit de inputvelden
        if self.selected_item:
            updated_data = tuple(entry.get() for entry in self.entries.values()) + (
                self.selected_item[0],
            )
            self.db.update(updated_data)
            self.load_data()

    def on_delete(self) -> None:
        # Verwijder het geselecteerde item uit de database en de tabel
        if self.selected_item:
            confirm = messagebox.askyesno(
                "Bevestig verwijderen", "Weet u zeker dat u dit item wilt verwijderen?"
            )
            if confirm:
                self.db.delete(self.selected_item[0])
                self.load_data()
                self.selected_item = None
                for entry in self.entries.values():
                    entry.delete(0, tk.END)

    def on_filter(self) -> None:
        # Filter de tabel op basis van de gegevens in de inputvelden
        filter_values = tuple(entry.get() for entry in self.entries.values())

        # Verwijder alle items uit de tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Voeg gefilterde items uit de database toe aan de tabel
        for item in self.db.get_all():
            match = True
            for index, value in enumerate(filter_values):
                if value and str(item[index]) != value:
                    match = False
                    break
            if match:
                self.tree.insert("", "end", values=item)
