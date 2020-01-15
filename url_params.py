from flask import Flask
import config

app = Flask (__name__)
app.config.from_object(config)

@app.route ('/')
def hello_world():

    return "hello world."

@app.route('/articles/<id>')
def article(id):
    return u'你请求的参是： %s'%id


if __name__ == '__main__':
    app.run ()
