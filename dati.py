
import os
import psycopg2
import json
import csv
import time

dsn = "dbname=mydb user=myuser password=mypass host=localhost"

def test_connection():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
   
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    cur.close()
    conn.close()
    return result

def ierakstit1(parametri):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql="""INSERT INTO saites (url,nosaukums,atsauksme,autors) 
        VALUES ({}) RETURNING id;""" 
    cur.execute(sql.format(parametri))
    jaunais_id=cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jaunais_id

def ierakstit2(tags,saite):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql="""INSERT INTO tagi_saites (tag_id,saite_id) 
        VALUES (%s,%s) RETURNING saraksta_id;""" 
    cur.execute(sql,(tags,saite))
    conn.commit()
    cur.close()
    conn.close()
    return test_connection()


def nolasit(parametri = 0):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    if parametri==0: #Šeit nolasās pilnīgi visi dati
        kverijs='''SELECT id, url, nosaukums, atsauksme, autors, tag_name, tagi.tag_id, seciba, kategorija FROM saites LEFT JOIN tagi_saites ON saites.id=tagi_saites.saite_id LEFT JOIN tagi ON tagi_saites.tag_id=tagi.tag_id ORDER BY id DESC, kategorija ASC, tagi.tag_id ASC '''
        cur.execute(kverijs)
        r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    elif parametri == 1:
        kverijs='''SELECT name FROM kategorijas '''
        cur.execute(kverijs)
        r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    elif parametri == 2:
        kverijs='''SELECT * FROM tagi ORDER BY kategorija ASC, seciba ASC'''        
        cur.execute(kverijs)
        r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    else:           #Šeit būs atlasītie dati
        cur.execute(parametri)
        r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    return r


def tekstapstrade(teksts, ietvars, saraksts):
    print(teksts,ietvars,saraksts)
    if len(saraksts) == 0:
        jaunaiskverijsvidus = ""
    else:
        jaunaiskverijsvidus = """WHERE EXISTS (SELECT 1 FROM tagi_saites WHERE (tagi_saites.tag_id = {} AND tagi_saites.saite_id=id)
            """.format(saraksts[0])
        for tags in saraksts[1:]:
            jaunaiskverijsvidus +="""
                AND EXISTS (SELECT 1 FROM tagi_saites WHERE tagi_saites.tag_id = {} AND tagi_saites.saite_id=id)
                """.format(tags)
        jaunaiskverijsvidus += " ) "

    if teksts == "":
        if len(saraksts) == 0:
            jaunaiskverijs = 0
        else:
            jaunaiskverijssakums = """
            SELECT id, url, nosaukums, atsauksme, autors, tag_name, tagi.seciba, tagi.tag_id, kategorija 
            FROM 
                (SELECT * FROM saites """
            jaunaiskverijsbeigas = """
                ) AS a 
                LEFT JOIN tagi_saites ON a.id=tagi_saites.saite_id LEFT JOIN tagi ON tagi_saites.tag_id = tagi.tag_id
            ORDER BY id DESC, kategorija ASC, tagi.seciba ASC
            """

            jaunaiskverijs = jaunaiskverijssakums + jaunaiskverijsvidus + jaunaiskverijsbeigas
            print(jaunaiskverijs)
    else:
        jaunaiskverijssakums = """
        SELECT * FROM (
            SELECT id, url, nosaukums, atsauksme, autors, tag_name, tagi.tag_id, tagi.seciba, kategorija 
            FROM 
                (SELECT * FROM saites """
        jaunaiskverijsbeigas = """
                ) AS a
                LEFT JOIN tagi_saites ON a.id=tagi_saites.saite_id LEFT JOIN tagi ON tagi_saites.tag_id = tagi.tag_id
            ORDER BY id DESC, kategorija ASC, tagi.seciba ASC) AS tabula WHERE
            """
        if ietvars == '1':
            jaunaiskverijsbeigas += """tabula.nosaukums LIKE '%{}%' """.format(teksts)
        elif ietvars == '2':
            jaunaiskverijsbeigas += """tabula.atsauksme LIKE '%{}%' """.format(teksts)
        else:
            jaunaiskverijsbeigas += """tabula.autors LIKE '%{}%' """.format(teksts)
        jaunaiskverijs = jaunaiskverijssakums + jaunaiskverijsvidus + jaunaiskverijsbeigas
    return jaunaiskverijs


def dzest(id):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM tagi_saites WHERE saite_id = %s", (id,))
        cur.execute("DELETE FROM saites WHERE id = %s", (id,))
        conn.commit()
    finally:
        cur.close()
        conn.close()
    return f"Deleted entry with id {id}"

    
def saisuSaraksts():
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    kverijs = """SELECT url FROM saites"""
    cur.execute(kverijs)
    saraksts=[r[0] for r in cur.fetchall()]
    conn.commit()
    cur.close()
    conn.close()
    return saraksts
