import sqlite3

def tutte():

    #visto che di default l'ordine è decrescente
    query = '''SELECT * FROM RaccolteFondi
                ORDER BY data_chiusura ASC;'''
    connection = sqlite3.connect('db/raccolte_fondi.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result