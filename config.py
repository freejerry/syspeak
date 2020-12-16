from os import environ

class Config:
    ENV = 'development' # 伺服器模式，開發中：development、正式發布：production
    DEBUG = True # 除錯模式
    TESTING = False # 測試模式
    SECRET_KEY = 'tkjga3732' # 連線加密密鑰
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://syspeak:@UdiHNAQMoyMG1ZOy@192.168.50.76:3307/syspeak" # 資料庫連線資訊
    SQLALCHEMY_TRACK_MODIFICATIONS = True # 資料庫錯誤追蹤模式，正式發布時設為False，要把它打開不然不知道錯哪