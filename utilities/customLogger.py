import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        os.makedirs('./Logs', exist_ok=True)

        logger = logging.getLogger("nopCommerceLogger")
        logger.setLevel(logging.INFO)

        # Avoid adding handlers multiple times
        if not logger.handlers:
            file_handler = logging.FileHandler('./Logs/automation.log', mode='a')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
