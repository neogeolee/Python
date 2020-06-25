"""
날짜 : 2020/06/25
이름 : 이태훈
내용 : 파이썬 웹프로그래밍
"""
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Python Flask!!!</h>'

@app.route('/hello')
def hello():
    return render_template('/hello.html')

if __name__=='__main__':
    app.run()