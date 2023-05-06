import tkinter as tk
from tkinter import ttk
import sqlite3


def create_table():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER)")
    conn.commit()
    conn.close()


def add_item():
    name = name_var.get()
    age = age_var.get()
    if name and age:
        tree.insert("", "end", values=(name, age))
        insert_data(name, age)
        name_var.set("")
        age_var.set("")


def insert_data(name, age):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO people (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()


def load_data():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM people")
    records = c.fetchall()
    conn.close()
    return records


create_table()

root = tk.Tk()
root.title("Treeview and Data Entry GUI with SQLite")

frame = ttk.Frame(root, padding="3")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tree = ttk.Treeview(frame, columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

for record in load_data():
    tree.insert("", "end", values=(record[0], record[1]))

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
