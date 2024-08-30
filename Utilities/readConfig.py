import configparser
config = configparser.RawConfigParser()
config.read('Configurations/config.ini')

class ReadConfigData:
    @staticmethod
    def read_url_from_config():
        url = config.get('Common Login Information','url')
        return url

    @staticmethod
    def read_username_from_config():
        username = config.get('Common Login Information','username')
        return username

    @staticmethod
    def read_password_from_config():
        password = config.get('Common Login Information','password')
        return password

