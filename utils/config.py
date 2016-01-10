import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config/config.ini")

def get_tor_port():
    return Config.get('tor', 'port')

def get_tor_ip():
    return Config.get('tor', 'ip')


