import psycopg2

#patrika parole
dsn = "dbname=postgres user=postgres password=patriks2020 host=localhost"  

#krisa parole
# dsn = "dbname=skolotajumajaslapaDB user=postgres password=Kriss2006 host=localhost"

def drop_all_tables(cur):
    # Drop in order due to foreign key constraints
    cur.execute("DROP TABLE IF EXISTS tagi_saites CASCADE;")
    cur.execute("DROP TABLE IF EXISTS tagi CASCADE;")
    cur.execute("DROP TABLE IF EXISTS saites CASCADE;")
    cur.execute("DROP TABLE IF EXISTS kategorijas CASCADE;")
    cur.execute("DROP TABLE IF EXISTS lietotaji CASCADE;")

def create_all_tables():
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    drop_all_tables(cur)

    # Re-create tables
    cur.execute("""
        CREATE TABLE IF NOT EXISTS lietotaji (
            id SERIAL PRIMARY KEY,
            lietotaj_vards VARCHAR(100) UNIQUE NOT NULL,
            parole_hash TEXT NOT NULL,
            loma VARCHAR(10) NOT NULL DEFAULT 'user'
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS saites (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL,
            nosaukums TEXT,
            atsauksme TEXT,
            autors TEXT
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tagi (
            tag_id SERIAL PRIMARY KEY,
            tag_name VARCHAR(100) NOT NULL,
            kategorija VARCHAR(100),
            seciba INTEGER DEFAULT 0
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tagi_saites (
            saraksta_id SERIAL PRIMARY KEY,
            tag_id INTEGER NOT NULL REFERENCES tagi(tag_id) ON DELETE CASCADE,
            saite_id INTEGER NOT NULL REFERENCES saites(id) ON DELETE CASCADE
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS kategorijas (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        );
    """)

    # Optional indexes
    cur.execute("CREATE INDEX IF NOT EXISTS idx_saites_url ON saites(url);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_tagi_saites_tag_id ON tagi_saites(tag_id);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_tagi_saites_saite_id ON tagi_saites(saite_id);")

    conn.commit()
    cur.close()
    conn.close()
    print("All tables dropped and recreated successfully.")

if __name__ == "__main__":
    create_all_tables()