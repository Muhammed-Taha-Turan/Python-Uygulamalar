import time
class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding = "utf-8") as dosya:
            self.dosya_icerigi=dosya.read()
            kelimeler=self.dosya_icerigi.split()
            self.sade_kelimeler=list()
            for i in kelimeler:
                i=i.strip("\n")
                i=i.strip(",")
                i=i.strip(".")
                i=i.strip(" ")
                self.sade_kelimeler.append(i)
    def tum_kelimeler(self):
        kelimeler=set()
        for i in self.sade_kelimeler:
            kelimeler.add(i)
        print("****Tüm Kelimeler****")
        for i in kelimeler:
             print(i)
             print("--------")
    def kelime_frekansi(self):
        frekans=set()
        for i in self.sade_kelimeler:
            adet=self.sade_kelimeler.count(i)
            frekans.add("{} kelimesi {} adet geçmiştir".format(i,adet))
        for i in frekans:
            print(i)
            print("-------")
    def kelime_ara(self,kelime):
        if (kelime in self.sade_kelimeler):
            adet = self.sade_kelimeler.count(kelime)
            print("{} Kelimesi {} Adet geçmiştir...".format(kelime, adet))
        else:
            print("'{}' Kelimesi Metin İçinde Yok!!".format(kelime))

print("""
**********Dosya İşlemleri**********
-----------------------------------
1-)Dosyayı Yazdır
2-)Dosya içinde Geçen Kelimeler
3-)Metinde Geçen Kelimelerin Sayısı
4-)Kelime Ara
5-)Çıkış
------------------------------------
************************************
""")
dosya=Dosya()
while True:
    try:
        islem = int(input("Yapmak İstediğiniz İşlem: "))
        if (islem==1):
            print("Dosya İçeriği Bastırılıyor....")
            time.sleep(1)
            print(dosya.dosya_icerigi)
        elif (islem==2):
            print("Geçen Kelimeler Sıralanıyor...")
            time.sleep(1)
            print(dosya.sade_kelimeler)
        elif (islem==3):
            print("Kelime Sayıları Hesaplanıyor...")
            time.sleep(1)
            dosya.kelime_frekansi()
        elif (islem==4):
            kelime=input("Aramak İstediğiniz Kelime: ")
            print("{} Kelimesi Aranıyor...".format(kelime))
            time.sleep(1)
            dosya.kelime_ara(kelime)
        elif (islem==5):
            print("Çıkış Yapılıyor...")
            time.sleep(1)
            print("Çıkıs Yapıldı Yine Bekleriz...")
            break
        else:
            print("5 Adet Seçenek var sadece...")
    except:
        print("Geçerli Bir İşlem Giriniz!!!")