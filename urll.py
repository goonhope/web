# -*- coding: utf-8 -*-
'''
@FileName	 :   urll.py 
@Created     :   2020/05/04
@Updated     :   2020/05/05
@Author		 :   goonhope@gmail.com
@Function	 :   临时中转
'''

from flask import Flask,render_template as tmp
app = Flask(__name__)


@app.route('/')
def mainpage():
    return tmp("page.html",name=None)


def made01(du):
    name, url = du
    @app.route(f'/{name}')
    def page01():
        return tmp("page.html",name=name,url=url)


def made02(du):
    name, url = du
    @app.route(f'/{name}')
    def page02():
        return tmp("page.html",name=name,url=url)


if __name__ == "__main__":
    google = ("google", "http://www.google.com.hk/")
    book = ("book","http://www.key007.com/e/action/ListInfo/?classid=61")
    made01(google)
    made02(book)
    app.run(host='0.0.0.0', port=8080,debug=True)
