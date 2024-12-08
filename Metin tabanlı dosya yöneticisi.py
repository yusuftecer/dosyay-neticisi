import os
import shutil
import datetime
print(""""
Dosya Yöneticisine Hoşgeldiniz

1.İşlem: Okumak istediğiniz dosyayı giriniz.
2.İşlem: Dosyaya metin ekleme.
3.İşlem: Silmek istediğiniz dosyayı seciniz.
4.İşlem: Adını değiştirmek istediğiniz dosyayı seçiniz.
5.İşlem: Yeni bir dosya oluşturma.
6.İşlem: Dosya özelliklerini görme.
7.İşlem: Dosya kopyalama.
8.İşlem: Aramak istediğiniz dosyayı giriniz.
9.İşlem: Çıkış


""")



def dosya_okuma():
    dosya = input("Okumak istediğiniz dosyayı giriniz:")
    with open (dosya,"r",encoding="utf-8") as file:
        for i in file :
            print("Dosya içeriği:\n",i,end=" \n")

def dosya_metinekleme():
    x = input("Değişiklik yapmak istediğiniz dosyanın adını giriniz:")
    c = input("Yapmak istediğiniz değişiklik:")
    z = int(input("Nereye ekleme yapmak istiyorsunuz:"))
    with open (x,"r+",encoding="utf-8") as dosya :
        dosya.seek(z)
        kalan_icerik = dosya.read()
        dosya.seek(z)
        dosya.write(c + kalan_icerik)

def dosya_oluşturma():
    dosya = input("Dosya adını giriniz:")
    metin = input("Dosyaya girmek istediğiniz metni giriniz:")
    type(metin)
    with open (dosya,"w",encoding="utf-8") as file :
        file.write(metin)

def dosya_silme():
    x = input("Silemk istediğiniz dosyayı giriniz:")
    os.remove((x))

def isim_degistirmek():
    x = input("İsmini değiştirmek istediğiniz dosya:")
    c = input("Yeni isim:")
    os.rename(x,c)

def dosya_ozellikleri():
    x = input("Özelliklerini görmek istediğiniz dosyayı giriniz:")
    dosyaozellikleri = os.stat(x)
    print(""""
    Dosyanın boyutu = {}
    Dosyanın son erişim zamanı = {}
    Dosyanın son değiştirilme zamanı = {}
    Dosyanın oluşturulma zamanı = {}
    """.format(dosyaozellikleri.st_size,datetime.datetime.fromtimestamp(dosyaozellikleri.st_atime).strftime("%Y-%m-%d %H:%M:%S"),datetime.datetime.fromtimestamp(dosyaozellikleri.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),datetime.datetime.fromtimestamp(dosyaozellikleri.st_ctime).strftime("%Y-%m-%d %H:%M:%S")))

def dosya_kopyalama():
    x = input("Kopyalanacak dosya adı:")
    c = input("Yeni dosyanın adı:")
    shutil.copyfile(x,c)

def dosya_arama():
    x = input("Aranacak dosyayı giriniz:")
    c = input("Arancak dizini giriniz:")
    for kok,dizinler,dosyalar in os.walk(c):
        for dosya in dosyalar:
            if dosya == x:
                tam_yol=os.path.join(kok,dosya)
                print(f"{x} dosyası bulundu: {tam_yol}")


while True:
    islem = int(input("Yapmak istediğiniz işlemi seçiniz:"))
    if islem == 1:
        dosya_okuma()
    elif islem == 2:
        dosya_metinekleme()
    elif islem == 3:
        dosya_silme()
    elif islem == 4:
        isim_degistirmek()
    elif islem == 5:
        dosya_oluşturma()
    elif islem == 6:
        dosya_ozellikleri()
    elif islem == 7:
        dosya_kopyalama()
    elif islem == 8:
      dosya_arama()
    elif islem == 9:
        break