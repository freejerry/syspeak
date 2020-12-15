# 從flask引入Flask python功能
from flask import Flask #Flask 網頁的架構


app = Flask(__name__) #用Flask跑app

from . import index #.當前目錄引入index這個函式
app.register_blueprint(index.bp, url_prefix='/') #叫index這個函式出來 url_prefix為子目錄

if __name__ == '__main__':
    app.run(debug=False)