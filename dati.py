import sqlite3


conn = sqlite3.connect("dati.db", check_same_thread=False)

def kategorijas_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE kategorijas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kategorija TEXT NOT NULL
        )
        """
    )
    conn.commit()

def pievienot_kategoriju(kategorija):
    cur = conn.cursor()
    cur.execute(
    f"""
    INSERT INTO kategorijas(kategorija) VALUES("{kategorija}")
    """
    )
    print(kategorija)