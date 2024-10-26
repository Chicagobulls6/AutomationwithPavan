import configparser

#read data from .ini file
config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')  # provide relative path

class ReadConfig:
    @staticmethod # access method using class name
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password



