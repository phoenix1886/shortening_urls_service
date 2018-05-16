import sqlite3
from configmodule import Config

print(Config.DATABASE_URI)

def create_table():
    with sqlite3.connect(Config.DATABASE_URI) as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS url_table(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT
            )
            '''
        )
        cursor.close()
        connection.commit()


def insert_url_and_get_id(url):
    with sqlite3.connect(Config.DATABASE_URI) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO url_table (url) VALUES ( ? )', (url,))
        id = cursor.lastrowid
        cursor.close()
        connection.commit()
    return id


def get_url_by_id(id):
    with sqlite3.connect(Config.DATABASE_URI) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT url FROM url_table WHERE id = ?', (id,))
        url = cursor.fetchone()
        cursor.close()
    return url[0] if url else None


def find_url_in_database(url):
    with sqlite3.connect(Config.DATABASE_URI) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT id FROM url_table WHERE url = ?', (url,))
        url = cursor.fetchone()
        cursor.close()
    return url[0] if url else None


if __name__ == '__main__':
    create_table()
    if not find_url_in_database('google.com'):
        id = insert_url_and_get_id('google.com')
    else:
        id = find_url_in_database('google.com')
