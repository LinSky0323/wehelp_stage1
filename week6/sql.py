# 將所有會跟資料庫的連動定義成獨立的function，統一放在這個py檔中
# 在main.py中，就單純使用函數
import mysql.connector

USER="root"
PASSWORD="y4hwong6"
HOST="localhost"
DATABASE="website"

def get_member_data():
    con=mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE,
    )
    cursor=con.cursor(dictionary=True)
    cursor.execute("select * from member")
    data=cursor.fetchall()
    con.close()

    return data

def get_all_data():
    con=mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE,
    )
    cursor=con.cursor(dictionary=True)
    cursor.execute("select message.*,member.name,member.username from message inner join member on message.member_id=member.id order by message.id desc;")
    data=cursor.fetchall()
    con.close()

    return data

def update_member_data(name,username,password):
    con=mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE,
    )
    cursor=con.cursor(dictionary=True)
    cursor.execute("insert into member(name,username,password) values(%s,%s,%s)",(name,username,password))
    con.commit()
    con.close()

def update_message(member_id,content):
    con=mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE,
    )
    cursor=con.cursor(dictionary=True)
    cursor.execute("insert into message(member_id,content) values(%s,%s)",(member_id,content))
    con.commit()
    con.close()

def delete_messages(message_id):
    con=mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE,
    )
    cursor=con.cursor(dictionary=True)
    cursor.execute("delete from message where id=%s",(message_id,))
    con.commit()
    con.close()

def check_acount(acount):
    con=mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE,
    )
    cursor=con.cursor(dictionary=True)
    cursor.execute("select username from member where username=%s",(acount,))
    data=cursor.fetchall()
    con.close()
    return data

def check_acount_password(acount,password):
    con=mysql.connector.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DATABASE,
    )
    cursor=con.cursor(dictionary=True)
    cursor.execute("select * from member where username=%s and password=%s",(acount,password))
    data=cursor.fetchone()
    con.close()
    return data

