import sqlite3

def get_user_by_id(id):
    query = 'SELECT * FROM Utenti WHERE id = ?'

    connection = sqlite3.connect('db/raccolte_fondi.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(query, (id,))

    result = cursor.fetchone()
    
    cursor.close()
    connection.close()

    return result

def get_user_by_email(email):

    query = 'SELECT * FROM utenti WHERE email = ?'

    connection = sqlite3.connect('db/raccolte_fondi.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(query, (email,))

    result = cursor.fetchone()
    
    cursor.close()
    connection.close()

    return result


def creare_utente(nuovo_utente):
    query = 'INSERT INTO utenti(username,email,password) VALUES (?,?,?)'

    connection = sqlite3.connect('db/raccolte_fondi.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    success = False

    try:
        cursor.execute(query, (nuovo_utente['username'],nuovo_utente['email'],nuovo_utente['password']))
        connection.commit()
        success = True
    except Exception as e:
        print('Error', str(e))
        connection.rollback()

    cursor.close()
    connection.close()

    return success