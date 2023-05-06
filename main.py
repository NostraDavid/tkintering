import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Global variable to store the image path
image_path = None


def add_entry():
    values = [entries[field].get() for field in entry_labels]
    if all(values) and image_path:
        treeview.insert("", tk.END, values=values)
    else:
        messagebox.showerror("Error", "Please fill in all fields and select an image.")


def remove_entry():
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item)
    else:
        messagebox.showerror("Error", "Please select an item to remove.")


def show_record():
    selected_item = treeview.selection()
    if selected_item:
        record = treeview.item(selected_item)["values"]
        messagebox.showinfo(
            "Record",
            "\n".join(
                [f"{entry_labels[i]}: {value}" for i, value in enumerate(record)]
            ),
        )
    else:
        messagebox.showerror("Error", "Please select an item to show the record.")


def print_report():
    pass


def print_barcode():
    pass


def print_barcode_sticker():
    pass


def go_to_admin_page():
    pass


def browse_file():
    global image_path
    image_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.png;*.jpeg")]
    )
    # You can display the selected image using a library like Pillow or OpenCV.
    pass


# The rest of the code remains the same, just replace the function definitions with the new ones.


# Create the main window
root = tk.Tk()
root.title("TreeView and Data Entry GUI")

# Create the treeview
treeview = ttk.Treeview(
    root,
    columns=("titel", "medium", "afmeting", "categorie", "jaar", "prijs"),
    show="headings",
)
treeview.heading("titel", text="Titel")
treeview.heading("medium", text="Medium")
treeview.heading("afmeting", text="Afmeting")
treeview.heading("categorie", text="Categorie")
treeview.heading("jaar", text="Jaar")
treeview.heading("prijs", text="Prijs")
treeview.pack()

# Create data entry labels and entry fields
entry_labels = ["Titel", "Medium", "Afmeting", "Categorie", "Jaar", "Prijs"]
entries = {}
for i, label in enumerate(entry_labels):
    tk.Label(root, text=label).grid(row=i, column=0)
    entries[label.lower()] = tk.Entry(root)
    entries[label.lower()].grid(row=i, column=1)

# Add a label and button to select a photo
photo_label = tk.Label(root, text="Foto")
photo_label.grid(row=len(entry_labels), column=0)

browse_button = tk.Button(root, text="Bladeren", command=browse_file)
browse_button.grid(row=len(entry_labels), column=1)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack()

toevoegen_button = tk.Button(button_frame, text="Toevoegen", command=add_entry)
toevoegen_button.pack(side=tk.LEFT)

verwijderen_button = tk.Button(button_frame, text="Verwijderen", command=remove_entry)
verwijderen_button.pack(side=tk.LEFT)

toon_record_button = tk.Button(button_frame, text="Toon record", command=show_record)
toon_record_button.pack(side=tk.LEFT)

# Create bottom menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Functionaliteiten", menu=file_menu)
file_menu.add_command(label="Print Rapport", command=print_report)
file_menu.add_command(label="Print Barcode", command=print_barcode)
file_menu.add_command(label="Print Barcode Sticker", command=print_barcode_sticker)
file_menu.add_command(label="Ga naar Admin Pagina", command=go_to_admin_page)

root.mainloop()
