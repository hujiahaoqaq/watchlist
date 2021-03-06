from flask import Flask,render_template
from flask import url_for
app = Flask(__name__)

name = 'hujiahao'
movies = [ {'title': 'My Neighbor Totoro', 'year': '1988'},
           {'title': 'Dead Poets Society', 'year': '1989'},
           {'title': 'A Perfect World', 'year': '1993'},
           {'title': 'Leon', 'year': '1994'},
           {'title': 'Mahjong', 'year': '1996'},
           {'title': 'Swallowtail Butterfly', 'year': '1996'},
           {'title': 'King of Comedy', 'year': '1999'},
           {'title': 'Devils on the Doorstep', 'year': '1999'},
           {'title': 'WALL-E', 'year': '2008'},
           {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')

# def hello():
#     return u'欢迎来到我的 Watchlist!'
def index():
    return  render_template('index.html',name=name,movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s'% name

@app.route('/test')
def test_url_for():
    #下面是一些调用示例
    print(url_for('hello'))#输出：/
    #注意下面两个调用是如何生成包含url变量的url的
    print(url_for('user_page',name='hujiahao'))#输出:/user/hujiahao
    print(url_for('user_page',name='peter'))
    print(url_for('test_url_for'))#输出:/test
    #下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到url后面
    print(url_for('test_url_for',num=2))#输出:/test?num=2
    return 'Test page'