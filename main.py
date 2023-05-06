import tkinter as tk
from typing import Tuple
from database import Database
from gui_elements import GUIElements

import random
from database import Database


class ArtworkGUI:
    def __init__(self, db_name: str):
        self.root = tk.Tk()
        self.db = Database(db_name)
        self.gui_elements = GUIElements(self.root, self.db)
        # insert_random_data(self.db, 100)

    def run(self) -> None:
        self.root.title("Artwork Database")
        self.root.geometry("800x600")
        self.root.mainloop()


def generate_random_data() -> Tuple[str, str, str, str, int, float]:
    title = f"Artwork {random.randint(1, 1000)}"
    medium = random.choice(["Olieverf", "Aquarel", "Acryl", "Potlood", "Houtskool"])
    dimension = f"{random.randint(10, 200)}x{random.randint(10, 200)}"
    category = random.choice(
        ["Abstract", "Impressionisme", "Realisme", "Surrealisme", "Portret"]
    )
    year = random.randint(1900, 2022)
    price = round(random.uniform(100, 10000), 2)
    return (title, medium, dimension, category, year, price)


def insert_random_data(db: Database, n: int) -> None:
    for _ in range(n):
        random_data = generate_random_data()
        db.insert(random_data)


if __name__ == "__main__":
    app = ArtworkGUI("artwork.db")
    app.run()
