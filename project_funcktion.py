import projea as p
import sqlite3 as sql
vt=sql.connect("proje.db")
imlec=vt.cursor()

def yönetici_parolası_ekle():
    #Yönetici parolsiı ekler
    while True:
        yönetici_parolası=r.randint(0,1000000)
        imlec.execute("SELECT * FROM kullanıcılar")
        db=imlec.fetchall()
        DB=[]
        for i in db:
            DB.append(i)#DB değişkenine database'deki kullanıcıların her bir kullanıcı için bir liste olmak üzere ekleme yapar
        if yönetici_parolası in DB:
             continue
        else:
             break
    return yönetici_parolası #Yönetici parolasını döndürür