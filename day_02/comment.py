
from flask import Flask,render_template


app = Flask (__name__)


@app.route ('/')
def index():
    comments=[
        {
            'user':'知了',
            'comment':'世界如此美好'
        },

        {
            'user':'杨煊友',
            'comment':'你却如此暴躁'
        },

        {
            'user': '狗伦',
            'comment': '这样不好，这样不好！'
        }
    ]

    return render_template('index02.html', comments=comments)

if __name__ == '__main__':
    app.run ()
