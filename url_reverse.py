from flask import Flask,url_for
import config

app = Flask (__name__)
app.config.from_object(config)

@app.route ('/')
def index():
    print(url_for('my_list'))
    print(url_for('article',id='abc'))
    return "hello world."

@app.route('/list/')
def my_list():
    return 'list'

@app.route('/article/<id>')
def article(id):
    return '你请救的id是： %s'%id

if __name__ == '__main__':
    app.run (debug=True)
