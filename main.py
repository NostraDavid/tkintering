import tkinter as tk
from tkinter import ttk


def add_item():
    name = name_var.get()
    age = age_var.get()
    if name and age:
        tree.insert("", "end", values=(name, age))
        name_var.set("")
        age_var.set("")


root = tk.Tk()
root.title("Treeview and Data Entry GUI")

frame = ttk.Frame(root, padding="3")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tree = ttk.Treeview(frame, columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

form_frame = ttk.Frame(frame, padding="3")
form_frame.grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E, tk.N, tk.S))

name_label = ttk.Label(form_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
name_var = tk.StringVar()
name_entry = ttk.Entry(form_frame, textvariable=name_var)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

age_label = ttk.Label(form_frame, text="Age:")
age_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_var = tk.StringVar()
age_entry = ttk.Entry(form_frame, textvariable=age_var)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

add_button = ttk.Button(form_frame, text="Add", command=add_item)
add_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()
