import os.path
from configparser import ConfigParser


CONFIG_FILE = './config.ini'

class Config():

    def __init__(self) -> None:
        self.config = ConfigParser()

        self.token = ''

        self.enable_logging = False
        self.logging_chat = 0

        self.enable_filter = False
        self.allowed_chats = []

        self.telegram_bot_api_server = ''
        self.use_webhook = True
        self.ip = ''
        self.port = 0


    def read(self):
        true_answ = ['t', 'yes', 'true']
        if not os.path.exists(CONFIG_FILE):
            print(f"Config file: {CONFIG_FILE} not found!")
            exit(1)
        
        self.config.read(CONFIG_FILE)

        self.token = self.config['Bot']['token']

        self.enable_logging = self.config['Logging']['enable'].lower() in true_answ
        self.logging_chat = self.config['Logging']['chat']

        self.enable_filter = self.config['Filter']['enable'].lower() in true_answ
        self.allowed_chats = self.config['Filter']['chats'].replace(" ", "").split(",")

        self.telegram_bot_api_server = self.config['Server']['bot_api']
        self.use_webhook = self.config['Server']['use_webhook'].lower() in true_answ
        self.ip = self.config['Server']['ip']
        self.port = self.config['Server']['port']

