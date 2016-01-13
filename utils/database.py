import config
import sqlite3

engine = config.get_db_engine()

def initialize():
    if 'sqlite' in engine:
        table_name = config.get_db_table_name()
        db_name = str(config.get_db_directory()) + '/' +  str(config.get_db_filename()) + '.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute('''CREATE TABLE {0}
                     (url text, time_found text, time_last_checked text)'''.format(table_name))
        conn.commit()

def save_domain(url):
    if 'sqlite' in engine:
        table_name = config.get_db_table_name()
        db_name = str(config.get_db_directory()) + '/' +  str(config.get_db_filename()) + '.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        url = url.replace('http://', '').replace('/', '')
        c.execute('INSERT INTO {0} VALUES ("{1}", datetime(), datetime())'.format(table_name, url));
        conn.commit()

def check_domain_in_db(url):
    if 'sqlite' in engine:
        table_name = config.get_db_table_name()
        db_name = str(config.get_db_directory()) + '/' +  str(config.get_db_filename()) + '.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        query = 'SELECT count(*) FROM {0} WHERE url = "{1}"'.format(table_name, url)
        test = c.execute(query)

        if test == 0:
            return True

        return False


