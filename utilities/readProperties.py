import configparser # default property of python
import os
import sys
config = configparser.RawConfigParser()
config.read(os.path.dirname(os.path.dirname(__file__)) + "\\configurations\\config.ini")


class readConfig:
    @staticmethod
    def readURL():
        url = config.get('common', 'URL')
        return url

    @staticmethod
    def readUsername():
        username = config.get('common', 'username')
        return username

    @staticmethod
    def readPassword():
        password = config.get('common', 'password')
        return password
