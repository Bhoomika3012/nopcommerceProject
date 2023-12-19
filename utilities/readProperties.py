import configparser

config=configparser.RawConfigParser()
config.read("D:\\Users\\bsuresh\\PycharmProjects\\pythonProject\\nopcommersseApp\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('commonInfo','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('commonInfo','password')
        return password