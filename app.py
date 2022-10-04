from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/index')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/movie')
def movie():
    datelist=[]
    conn=sqlite3.connect('movie.db')
    c=conn.cursor()
    sql='select * from movie250'
    rs=c.execute(sql)
    for item in rs:
        datelist.append(item)
    c.close()
    conn.close()
    return render_template('movie.html', movies=datelist)

@app.route('/score')
def score():
    score=[]
    num=[]
    conn = sqlite3.connect('movie.db')
    c = conn.cursor()
    sql1 = 'select score,count(score) from movie250 group by score'
    rs = c.execute(sql1)
    for item in rs:
        score.append(item[0])
        num.append(item[1])
    c.close()
    conn.close()
    return render_template('score.html', score=score, num=num)

@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/pic')
def pic():
    datelist = []
    conn = sqlite3.connect('movie.db')
    c = conn.cursor()
    sql = 'select cname from movie250'
    rs = c.execute(sql)
    for item in rs:
        datelist.append(item)
    c.close()
    conn.close()
    return render_template('pic.html', pics=datelist)
if __name__ == '__main__':
    app.run()
