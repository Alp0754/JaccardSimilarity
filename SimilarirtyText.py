import sqlite3

metin1=input("Birinci metni giriniz:")
metin2=input("İkinci metni giriniz:")


baglan=sqlite3.connect('metinBenzerlik.db')

imlec=baglan.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS metin(Metin TEXT)")

imlec.execute("INSERT INTO metin(Metin) VALUES(?)",(metin1,))
imlec.execute("INSERT INTO metin(Metin) VALUES(?)",(metin2,))
imlec.execute("SELECT * FROM metin")


baglan.commit()

def Benzerlikoranı(text1,text2):
    kume1=set(text1.split())
    kume2=set(text2.split())
    kesisim=len(kume1 & kume2)
    birlesim=len(kume1|kume2)
    benzerlik=kesisim/birlesim
    return benzerlik

benzerlikDurumu=Benzerlikoranı(metin1,metin2)


dosya=open("BenzerlikDurumu.txt","w")
dosya.write(str(benzerlikDurumu))

dosya.close()

imlec.execute("DELETE FROM metin")
baglan.commit()
