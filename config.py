import configparser
import os
def read_config():
    "Reads config"
    check_config()
    config = configparser.ConfigParser()
    config.read('settings/config.ini')
    return config
def check_config():
    PATH = "settings/"
    if not os.path.exists(PATH):
        os.makedirs(PATH)
        with open("settings/config.ini","w") as f:
            f.close()
        print("Path Created")