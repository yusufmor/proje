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
def isim_ekle_kontrol():
    #İsim ve parolayı kontrol edip onu döndürür
    while True:
        ad=input("Yeni kullanıcı adinizi giriniz..:")
        parola=input("Yeni kullanıcı parolasını giriniz..:")
        imlec.execute("SELECT * FROM kullanıcılar")
        db=imlec.fetchall()
        DB=[]
        for i in db:
            for a in i:
                DB.append(a) 
        if ad in DB:         #Ad içindemi diye kontrol edyor
            imlec.execute("SELECT kullanıcı_parolası FROM kullanıcılar WHERE kullanıcı_adı = ?",[ad])
            parola_db=imlec.fetchall()
            parola_DB=[]
            for i in parola_db:
                for a in i:
                    parola_DB.append(a)
            
            if parola != parola_DB[0]: #Ad içindeyse kullanıcıdan alına parola ile Bu ad veya adların içinde aynı parola var mı diye bakıyor
                print("hesabınız eklendi") #yoksa dögüyü bitiriyor
                break
            else:
                print("Böyle bir parola var")#varsa en başa dönüyor
                continue
        else:                #Ad içinde değilse döngüyü bitiriyor
            break
    return ad,parola #ensonda ad ve soyadı dödürüyor
def kayıt_ekle():
    #Bu fonksiyon adı parolayı ve yönetici parolasını veri tabınına ekler
    ad,parola = isim_ekle_kontrol()
    girilecek_deger="INSERT INTO kullanıcılar(kullanıcı_adı,kullanıcı_parolası,yönetici_parolası) VALUES (?,?,?)"
    yönetici_parolası=yönetici_parolası_ekle()
    data=[ad,parola,yönetici_parolası]
    imlec.execute(girilecek_deger,data)
    vt.commit()
