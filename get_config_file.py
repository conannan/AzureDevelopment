import configparser


class GetConfig():
    CONFIG = configparser.ConfigParser()
    CONFIG.read("config.ini")


if __name__ == '__main__':
    print(GetConfig.CONFIG["GlobalVariables"]["SUBSCRIPTION_ID"])
