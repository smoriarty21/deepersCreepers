import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config/config.ini")

def get_tor_port():
    return Config.get('tor', 'port')

def get_tor_ip():
    return Config.get('tor', 'ip')

def get_db_engine():
    return Config.get('database',  'engine')

def get_db_filename():
    return Config.get('database', 'filename')

def get_db_directory():
    return Config.get('database', 'directory')

def get_db_host():
    return Config.get('database', 'host')

def get_db_port():
    return Config.get('database', 'port')

def get_db_collection():
    return Config.get('database', 'collection')

def get_db_table_name():
    return Config.get('database', 'tablename')
