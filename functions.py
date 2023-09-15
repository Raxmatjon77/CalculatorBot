import sqlite3

db=sqlite3.connect('data.db')
c=db.cursor()
c.execute(f"""CREATE TABLE IF NOT EXISTS hisobot(id TEXT,son TEXT,amal TEXT,son1 TEXT,belgi TEXT)""")
db.commit()
db.close()

def adduser(id):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    hisobot=c.execute(f"""SELECT * FROM hisobot """).fetchall()


    c.execute(f"""INSERT INTO hisobot VALUES ("{id}",'0','0','0','0')""")

    db.commit()
    db.close()
def changeamal(id,amal):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    hisobot=c.execute("""SELECT * FROM hisobot """).fetchall()
    for i in hisobot:
        if i[0]==str(id):

            c.execute(F"""UPDATE hisobot SET amal='{amal}' WHERE id='{id}' """)



    db.commit()
    db.close()

def changeson(id, n):
        db = sqlite3.connect('data.db')
        c = db.cursor()
        hisobot = c.execute(F"""SELECT * FROM hisobot """).fetchall()
        for i in hisobot:
            if i[0] == str(id):
                if i[4]=='0':
                    son = int(f"{i[1]}{n}")
                    c.execute(F"""Update hisobot SET son={son} WHERE id='{id}' """)
                else:
                    son = int(f"{i[3]}{n}")
                    c.execute(F"""Update hisobot SET son1={son} WHERE id={id}""")



        db.commit()
        db.close()

def GetRes(id):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    hisobot = c.execute("""SELECT * FROM hisobot """).fetchall()
    for i in hisobot:
        if i[0] == str(id):
            if i[2]=='0':
                db.commit()
                db.close()
                return i[1]

            else:
                c.execute(F"""UPDATE hisobot SET son1='eval(f"{i[1]} {i[2]} {i[3]}")' , amal='0',son1='0',belgi='0' WHERE id ='{id}' """)
                db.commit()
                db.close()
                if i[2]=='*' or i[2]=="/" and i[3]=="0":
                    return eval(f"{i[1]} {i[2]} 1")
                else:
                    return eval(f"{i[1]} {i[2]} {i[3]}")


def getSon(id):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    hisobot = c.execute("""SELECT * FROM hisobot """).fetchall()
    for i in hisobot:
        if i[0] == str(id):
            if i[1]=="0":
                return 0
            elif i[2]=="0":
                return i[1]
            elif i[3]=="0":
                return [i[1],i[2]]
            else:
                return [i[1],i[2],i[3]]

    db.commit()
    db.close()
def changebelgi(id):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    hisobot = c.execute("""SELECT * FROM hisobot """).fetchall()
    for i in hisobot:
        if i[0] == str(id):
            c.execute(F"""UPDATE hisobot SET belgi='1' WHERE id='{id}' """)
    db.commit()
    db.close()
def clear(id):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    hisobot = c.execute("""SELECT * FROM hisobot """).fetchall()
    for i in hisobot:
        if i[0] == str(id):
            c.execute(F"""UPDATE hisobot SET son ='0',belgi='0', amal='0',son1='0' WHERE id ='{id}'""")
    db.commit()
    db.close()
    return "tozalandi,yangi aperatsiyani boshlash mumkin"
