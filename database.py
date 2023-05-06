import sqlite3
from typing import List, Tuple, Any, Optional


class Database:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS artwork (
            id INTEGER PRIMARY KEY,
            title TEXT,
            medium TEXT,
            dimension TEXT,
            category TEXT,
            year INTEGER,
            price REAL
        )
        """
        )
        self.conn.commit()

    def insert(self, data: Tuple[Any, ...]) -> None:
        self.cursor.execute(
            """
        INSERT INTO artwork (title, medium, dimension, category, year, price)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
            data,
        )
        self.conn.commit()

    def get_all(self) -> List[Tuple[Any, ...]]:
        self.cursor.execute("SELECT * FROM artwork")
        return self.cursor.fetchall()

    def update(self, data: Tuple[Any, ...]) -> None:
        self.cursor.execute(
            """
        UPDATE artwork
        SET title = ?, medium = ?, dimension = ?, category = ?, year = ?, price = ?
        WHERE id = ?
        """,
            data,
        )
        self.conn.commit()

    def delete(self, id: int) -> None:
        self.cursor.execute("DELETE FROM artwork WHERE id = ?", (id,))
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
