# -*- coding: cp1254 -*-
from Tkinter import *
import time
anapen = Tk()
anapen.title(u"Ceasar Yöntemiyle Şifreleme")
anapen.geometry("480x600+300+100")
anapen.wm_iconbitmap("gray12")
anapen.resizable(False, False)
anapen.wm_attributes("-topmost", 1)
anapen.tk_setPalette("black")

#Menü İşlemleri
menu = Menu(anapen)
anapen.config(menu=menu)
dosya = Menu(menu, tearoff=0)
menu.add_cascade(label=u"Konsol")
menu.add_cascade(label=u"Yapımcı")

#Kullanıcı Giriş
bilgiler = ("MuRe","cyber-warrior")
denemeHakki = 3
zaman = 0

def girisYap():
    global denemeHakki, zaman

    if denemeHakki <= 0:
        if time.time()-zaman >= 5:
            denemeHakki = 3
        else:
            sonuc.config(text = u"5 sn Beklemeniz gerekiyor")
            return False
    
    username = isim.get()
    password = sifre.get()
    if username == bilgiler[0] and password == bilgiler[1]:
        sonuc.config(text = u"Başarıyla giriş yapıldı...")
        ekraniTemizle()

    else:
        denemeHakki -= 1
        if denemeHakki == 0:
            zaman = time.time()
        sonuc.config(text = u"Bilgiler Yanlış! Deneme: %d " %denemeHakki)
        
def ekraniTemizle():
    def geriCevir(x):
        return chr(x)
 
    def yapistir():
        global metin
        metin = giris.get(0.0, END)
        sifre = list(map(f, metin))
        cikis1.delete(0.0,END)
        cikis1.insert(INSERT, str(sifre[:-1])[1:-1])
        sifrelimetin = ''.join(geriCevir(i) for i in sifre)
        cikis2.delete(0.0,END)
        cikis2.insert(INSERT, str(sifrelimetin))
        cozulen = list(map(coz, sifrelimetin))

    def sifreCoz():
        global metin
        metin = giris.get(0.0, END)
     
        sifre = list(map(coz, metin[:-1]))
        cikis1.delete(0.0,END)
        cikis1.insert(INSERT, str(sifre)[1:-1])
        sifrelimetin = ''.join(geriCevir(i) for i in sifre)
        cikis2.delete(0.0,END)
        cikis2.insert(INSERT, str(sifrelimetin))
        cozulen = list(map(coz, sifrelimetin))
     
    def f(x):
        return ord(x)+3
     
    def coz(x):
        return ord(x)-3
     
    #Pencere
    Karsila = Label(anapen)
    Karsila.config(text = u"Ceasar Yöntemiyle Şifreleme ve Şifre Çözme - Başarı İle Giriş Yaptınız")
    Karsila.place(x=1,y=1)
     
    GirisBir = Label(anapen)
    GirisBir.config(text = u"Giriş:")
    GirisBir.place(x=1,y=25)
     
    giris = Text(anapen)
    giris.config(width = 40, height = 8, font = "arial 12")
    giris.place(x=100,y=25)
     
    karsilama1 = Label(anapen)
    karsilama1.config(text = u"ASCII Hali:")
    karsilama1.place(x=1,y=200)
     
    cikis1 = Text(anapen)
    cikis1.config(width = 40, height = 8, font = "arial 12")
    cikis1.place(x=100,y=200)
     
    karsilama2 = Label(anapen)
    karsilama2.config(text = u"Çıkış:")
    karsilama2.place(x=1,y=375)
     
    cikis2 = Text(anapen)
    cikis2.config(width = 40, height = 8, font = "arial 12")
    cikis2.place(x=100,y=375)
     

     
    hesapButon = Button(anapen)
    hesapButon.config(text = u"Hesapla!",command = yapistir)
    hesapButon.place(x=1,y=550)
     
    cozButon = Button(anapen)
    cozButon.config(text = u"Şifre Çöz!",command = sifreCoz)
    cozButon.place(x=410,y=550)

    #Ekran Temizle
    karsilama.destroy()
    isimSor.destroy()
    isim.destroy()
    sifreSor.destroy()
    sifre.destroy()
    buton.destroy()
    ithafen.destroy()
    

karsilama = Label(anapen)
karsilama.config(text = u"Ceasar Crypto Programına Hoş Geldiniz")
karsilama.place(x=1,y=1)

isimSor = Label(anapen)
isimSor.config(text = u"Kullanıcı Adı:")
isimSor.place(x=1,y=25)

isim = Entry(anapen)
isim.place(x=150,y=25)

sifreSor = Label(anapen)
sifreSor.config(text = u"Kullanıcı Şifre:")
sifreSor.place(x=1,y=50)

sifre = Entry(anapen)
sifre.place(x=150,y=50)

buton = Button(anapen)
buton.config(text = u"Gönder ", command = girisYap)
buton.place(x=300,y=45)

sonuc = Label(anapen)
sonuc.config(text = u"Henüz işlem yapılmadı ")
sonuc.place(x=300,y=20)

ithafen = Label(anapen)
ithafen.config(text = u"Kardeşim eSckral'a ithafen - Kara Ayaz")
ithafen.place(x=1,y=75)


mainloop()
