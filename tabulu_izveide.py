import psycopg2

dsn = "dbname=postgres user=postgres password=patriks2020 host=localhost"

def create_all_tables():
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    # Tabula: lietotaji
    cur.execute("""
        CREATE TABLE IF NOT EXISTS lietotaji (
            id SERIAL PRIMARY KEY,
            lietotaj_vards VARCHAR(100) UNIQUE NOT NULL,
            parole_hash TEXT NOT NULL,
            role VARCHAR(10) NOT NULL DEFAULT 'user'
        );
    """)

    # Tabula: saites
    cur.execute("""
        CREATE TABLE IF NOT EXISTS saites (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL,
            nosaukums TEXT,
            atsauksme TEXT,
            autors TEXT
        );
    """)

    # Tabula: tagi
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tagi (
            tag_id SERIAL PRIMARY KEY,
            tag_name VARCHAR(100) NOT NULL,
            kategorija VARCHAR(100),
            seciba INTEGER DEFAULT 0
        );
    """)

    # Tabula: tagi_saites
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tagi_saites (
            saraksta_id SERIAL PRIMARY KEY,
            tag_id INTEGER NOT NULL REFERENCES tagi(tag_id) ON DELETE CASCADE,
            saite_id INTEGER NOT NULL REFERENCES saites(id) ON DELETE CASCADE
        );
    """)

    # Tabula: kategorijas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS kategorijas (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        );
    """)

    cur.execute("CREATE INDEX IF NOT EXISTS idx_saites_url ON saites(url);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_tagi_saites_tag_id ON tagi_saites(tag_id);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_tagi_saites_saite_id ON tagi_saites(saite_id);")

    conn.commit()
    cur.close()
    conn.close()
    print("All tables created successfully.")

if __name__ == "__main__":
    create_all_tables()
