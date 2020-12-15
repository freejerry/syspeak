from os import environ

class Config:
    SECRET_KEY = 'tkjga3732'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://syspeak:@UdiHNAQMoyMG1ZOy@192.168.50.76:3307/syspeak"
    SQLALCHEMY_TRACK_MODIFICATIONS = True