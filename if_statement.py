from flask import Flask,render_template
import config

app = Flask (__name__)
app.config.from_object(config)

@app.route ('/')
def index():
    books=[

        {'name':'西游记',
         'author':'吴承恩',
         'price':120},

        {'name': '石头记',
         'author': '曹雪芹',
         'price': 220},

        {'name': '三国演义',
         'author': '罗贯中',
         'price': 128},

        {'name': '西厢记',
         'author': '不详',
         'price': 119}

    ]

    websites=['google.com','baidu.com','youtube.com']
    user={
        'username':'goulun',
        'age':18
    }

    return render_template('ifIndex.html',books=books)





if __name__ == '__main__':
    app.run (debug=True)
