# 從flask引入Flask python功能
from flask import Flask #Flask 網頁的架構
from flask_sqlalchemy import SQLAlchemy #引入資料庫連線函式庫
from flask_login import LoginManager #引入登入模組函式庫

app = Flask(__name__) #用Flask跑app
app.config.from_object('config.Config') # 載入設定檔
db = SQLAlchemy() #實體化資料庫連線模組

login_manager = LoginManager() #實體化登入模組
login_manager.login_view = "userpanel.login"

def create_app():
    #初始化資料庫連線
    db.init_app(app)

    login_manager.init_app(app)

    from . import index #.當前目錄引入index這個函式
    app.register_blueprint(index.bp, url_prefix='/') #叫index這個函式出來 url_prefix為子目錄

    from . import userpanel
    app.register_blueprint(userpanel.bp, url_prefix='/userpanel')

    return app

if __name__ == '__main__':
    app.run(debug=False)