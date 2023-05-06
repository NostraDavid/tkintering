import tkinter as tk
from tkinter import ttk
from gui_elements import GUIElements
from database import Database

def main():
    root = tk.Tk()
    root.title("GUI Scherm")
    
    # Configureer de root window
    root.geometry("800x600")
    root.resizable(False, False)
    
    # Initialiseer de database
    db = Database()
    
    # Initialiseer de GUI-elementen
    gui = GUIElements(root, db)
    
    root.mainloop()

if __name__ == "__main__":
    main()
