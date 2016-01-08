import sqlite3

conn = sqlite3.connect('onion.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE pandoras_box
                 (url text)''')
    conn.commit()

def save_domain(url):
    url = url.replace('http://', '').replace('/', '')
    c.execute('INSERT INTO pandoras_box VALUES ("{0}")'.format(url));
    conn.commit()
