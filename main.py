import tkinter as tk
from database import Database
from gui_elements import GUIElements


class ArtworkGUI:
    def __init__(self, db_name: str):
        self.root = tk.Tk()
        self.db = Database(db_name)
        self.gui_elements = GUIElements(self.root, self.db)

    def run(self) -> None:
        self.root.title("Artwork Database")
        self.root.geometry("800x600")
        self.root.mainloop()


if __name__ == "__main__":
    app = ArtworkGUI("artwork.db")
    app.run()
