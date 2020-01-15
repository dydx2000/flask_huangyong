from flask import Flask,render_template
# import config

app = Flask (__name__)
# app.config.from_object(config)

@app.route ('/')
def index():
    dic1={
        'username':'goulun',
        'gender':'male',
        'age':18
    }
    return render_template('index.html', **dic1)


if __name__ == '__main__':
    app.run (debug=True)
 