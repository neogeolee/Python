from flask import Blueprint, render_template, request, redirect
import pymysql as db

delete_blueprint = Blueprint('delete', __name__)

@delete_blueprint.route('/delete', methods=['POST'])
def delete():
    # 파라미터 수신
    uid = request.form['uid']
    name = request.form['name']
    hp = request.form['hp']
    age = request.form['age']

    # 데이터베이스 접속
    conn = db.connect(host='192.168.44.46',
                      user='lth',
                      password='1234',
                      db='lth',
                      charset='utf8')

    # 쿼리문 실행 객체 생성
    cur = conn.cursor()
    # 쿼리문 실행
    sql = "DELETE FROM `USER1` WHERE ('%s', '%s', '%s', '%s')"
    cur.execute(sql % (uid, name, hp, age))
    conn.commit()

    # 데이터베이스 종료
    conn.close()

    return redirect('/list')