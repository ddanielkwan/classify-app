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
def write_config(settingChange):
    value = settingChange.get()
    config = read_config()
    config['DEFAULT']['bg'] = value
    with open('settings/config.ini', 'w') as configfile:
       config.write(configfile)
       configfile.close()
    print(value)
def write_default():
    config = read_config()
    config['DEFAULT'] = {'bg':'black'}