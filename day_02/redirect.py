from flask import Flask,url_for,redirect

import config

app = Flask (__name__)
app.config.from_object(config)

@app.route ('/')
def index():
    return redirect(url_for('login'))
    return "这是首页"

@app.route("/login/")
def login():
    return "这是登录页"

@app.route("/question/<is_login>")
def question(is_login):
    if is_login=='1':
        return "欢迎访问问答页面。"
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run (debug=True)
