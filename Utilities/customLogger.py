import logging

class Log_Generate:
    @staticmethod
    def generate_log():
        logging.basicConfig(filename="Logs/OrangeHRM.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt="%d/%m/%Y %I:%M:%S %p",force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



