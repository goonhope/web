# -*- coding: utf-8 -*-
'''
@FileName	 :   url.py 
@Created     :   2020/05/04 12:45 
@Updated     :   2020/05/04 12:45 
@Author		 :   goonhope@gmail.com
@Function	 :   flask 
'''

from flask import Flask
app = Flask(__name__)


@app.route('/')
def mainpage():
    return '''<head><title>Teddy的共享</title></head>
    <h1>Index of Teddy</h1>
    <h2>
    <a href="/google">1.google搜索</a>
    <br><br>
    <a href="/book">2.文献论文下载</a>
    </h2>'''


def page(du):
    return '''<head><title>''' + du[0] + '''中转</title></head><script language="JavaScript">
    function autoResize(id){ var newheight;  var newwidth;
    if(document.getElementById){
        newheight=document.getElementById(id).contentWindow.document.body.scrollHeight;
        newwidth=document.getElementById(id).contentWindow.document.body.scrollWidth;}
    document.getElementById(id).height= (newheight) + "px";
    document.getElementById(id).width= (newwidth) + "px";}</script>
    <iframe src="''' + du[1] + '''" width="100%" height="100%" id="iframe" marginheight="0" frameborder="0"
     onLoad="autoResize('iframe');"></iframe>'''


def pag(du):
    return '''<head><title>''' + du[0] + '''中转</title></head><script language="JavaScript">
    var autoResize = (strg) =>$(strg).attr("scrolling": "no").load(function() {
    $(this).css({"height": $(this).contents().height() + "px","width": $(this).contents().width() + "px"})}); </script>
    <iframe src="''' + du[1] + '''" width="100%" height="100%" id="iframe" marginheight="0" frameborder="0"
     onLoad="autoResize('iframe');"></iframe>'''


def made01(du):
    disc, url = du
    @app.route(f'/{disc}')
    def page01(du=du):
        return pag(du)

    
def made02(du):
    disc, url = du
    @app.route(f'/{disc}')
    def page02(du=du):
        return page(du)


if __name__ == "__main__":
    google = ("google", "http://www.google.com.hk/")
    book = ("book","http://www.key007.com/e/action/ListInfo/?classid=61")
    made01(google)
    made02(book)
    app.run(host='0.0.0.0', port=8080,debug=True)
