import pymysql as db

conn = db.connect(host='192.168.44.46',
                  user='lth',
                  password='1234',
                  db='lth',
                  charset='utf8')

cur = conn.cursor()
cur.execute("SELECT * FROM `USER1`")

for row in cur.fetchall():
    print('------------------')
    print('아이디 :', row[0])
    print('이 름 :', row[1])
    print('휴대폰 :', row[2])
    print('나이 :', row[3])
    print('------------------')

conn.close()