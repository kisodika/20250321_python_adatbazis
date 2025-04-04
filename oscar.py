import sqlite3

# Kapcsolódás az adatbázishoz
conn = sqlite3.connect('oscar.db')
cursor = conn.cursor()






cursor.execute('''
CREATE TABLE IF NOT EXISTS film (
    id INTEGER PRIMARY KEY,
    ev INTEGER,
    nyert BOOLEAN,
    magyar TEXT,
    cim TEXT UNIQUE,
    bemutato DATE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS kapcsolat (
    filmid INTEGER,
    keszitoid INTEGER,
    PRIMARY KEY (filmid, keszitoid),
    FOREIGN KEY (filmid) REFERENCES film(id),
    FOREIGN KEY (keszitoid) REFERENCES keszito(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS keszito (
    id INTEGER PRIMARY KEY,
    nev TEXT UNIQUE,
    producer BOOLEAN
)
''')
