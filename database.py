import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                title TEXT,
                medium TEXT,
                dimension TEXT,
                category TEXT,
                year INTEGER,
                price REAL
            )
        """)
        self.conn.commit()
    
    def insert(self, data):
        self.cursor.execute("""
            INSERT INTO items (title, medium, dimension, category, year, price) VALUES (?, ?, ?, ?, ?, ?)
        """, data)
        self.conn.commit()
    
    def update(self, data):
        self.cursor.execute("""
            UPDATE items SET title=?, medium=?, dimension=?, category=?, year=?, price=? WHERE id=?
        """, data)
        self.conn.commit()
    
    def delete(self, item_id):
        self.cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
        self.conn.commit()
    
    def get_all(self):
        self.cursor.execute("SELECT * FROM items")
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
