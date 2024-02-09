import sqlite3
from datetime import datetime

# Connessione al database (crea il database se non esiste)
conn = sqlite3.connect('raccolte_fondi.db')
c = conn.cursor()

# Creazione delle tabelle
c.execute('''
    CREATE TABLE IF NOT EXISTS Utenti (
        id INTEGER  PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL CHECK(email LIKE '%_@__%.__%'),
        password TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS RaccolteFondi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    descrizione TEXT NOT NULL,
    immagine TEXT,
    obiettivo REAL NOT NULL CHECK(obiettivo > 0),
    tipo TEXT NOT NULL CHECK(tipo IN ('lampo', 'normale')),
    data_creazione TEXT NOT NULL,
    data_chiusura TEXT,
    donazione_min REAL NOT NULL CHECK(donazione_min > 0),
    donazione_max REAL NOT NULL CHECK(donazione_max > 0),
    stato TEXT NOT NULL CHECK(stato IN ('aperta', 'chiusa')),
    utente_id INTEGER NOT NULL,
    FOREIGN KEY(utente_id) REFERENCES Utenti(id)
    )
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Donazioni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raccolta_id INTEGER NOT NULL,
    nome_donatore TEXT NOT NULL,
    cognome_donatore TEXT NOT NULL,
    importo_donato REAL NOT NULL CHECK(importo_donato > 0),
    data_donazione TEXT NOT NULL,
    anonimo INTEGER NOT NULL CHECK(anonimo IN (0, 1)),
    carta_di_credito TEXT NOT NULL CHECK(length(carta_di_credito) >= 16 AND length(carta_di_credito) <= 20),
    FOREIGN KEY(raccolta_id) REFERENCES RaccolteFondi(id)
);
''')

# Inserimento dei valori nelle tabelle
# Inserimento di un utente
c.execute("INSERT INTO Utenti (username, email, password) VALUES (?, ?, ?)", ('utente1', 'utente1@example.com', 'password1'))
conn.commit()

# Inserimento di una raccolta fondi
c.execute("INSERT INTO RaccolteFondi (titolo, descrizione, immagine, obiettivo, tipo, data_creazione, data_chiusura, donazione_min, donazione_max, stato, utente_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
          ('Raccolta1', 'Descrizione della Raccolta 1', 'immagine1.jpg', 1000.0, 'lampo', datetime.now(), datetime.now(), 5.0, 500.0, 'aperta', 1))
conn.commit()

# Inserimento di una donazione
c.execute("INSERT INTO Donazioni (raccolta_id,nome_donatore, cognome_donatore, importo_donato, data_donazione, anonimo, carta_di_credito) VALUES (?,?, ?, ?, ?, ?, ?)",
          (1,'Mario', 'Rossi', 50.0, datetime.now(), 0, '1234-5678-9012-3456'))
conn.commit()

# Chiusura della connessione al database
conn.close()