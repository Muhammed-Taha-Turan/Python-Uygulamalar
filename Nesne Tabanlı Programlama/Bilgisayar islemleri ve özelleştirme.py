import math
import time
class Bilgisayar():
    def __init__(self,marka="Bilgi Yok",hard_disk=0,ram=0,anakart="Bilgi Yok",islemci="Bilgi Yok",uygulamalar=["Hesap Makinesi"],durum="Kapalı",acik_uygulama="Yok"):
        self.marka=marka
        self.hard_dik=hard_disk
        self.ram=ram
        self.anakart=anakart
        self.islemci=islemci
        self.uygulamalar=uygulamalar
        self.durum=durum
        self.acik_uygulama=acik_uygulama
    def acma(self):
        if self.durum=="Kapalı":
            print("Bilgisayar Açılıyor...")
            time.sleep(1)
            print("Bilgisayar Açıldı!")
            self.durum="Açık"
        else:
            time.sleep(0.5)
            print("Bilgisayar Zaten Açık!")
    def kapatma(self):
        if self.durum=="Açık":
            print("Bilgisayar Kapanıyor...")
            time.sleep(1)
            print("Bilgisayar Kapandı!")
            self.durum="Kapalı"
        else:
            time.sleep(0.5)
            print("Bilgisayar Zaten Kapalı!")
    def uygulama_ekle(self):
        while True:
            uygulama=input("Eklemek İstediğiniz Uygulama (Çıkış İçin 1 e basınız): ")
            if uygulama!="1":
                print("{} Uygulaması Ekleniyor...".format(uygulama))
                time.sleep(1)
                print("{} Uygulaması Eklendi!".format(uygulama))
                self.uygulamalar.append(uygulama)
            else:
                print("Çıkış Yapılıyor...")
                time.sleep(0.5)
                print("Çıkış Yapıldı!")
                break
    def uygulama_ac(self):
        sayac=1
        for i in self.uygulamalar:
            print("{} = {}".format(sayac,i))
            sayac+=1
        try:
            islem=int(input("Açmak İstediğiniz Uygulama: "))
            if islem==1:
                print("""
                *********** HESAP MAKİNESİ ***********
                İŞLEMLER:
                1-TOPLAMA   5-ÜST ALMA      9-KOMBİNASYON
                2-ÇIKARMA   6-KÖK ALMA      10-MOD ALMA
                3-ÇARPMA    7-FAKTÖRİYEL    11-EBOB
                4-BÖLME     8-PERMUTASYON   12-EKOK
                *****************************************
                ÇIKIMAK İÇİN Q YA BASINIZ....
                *****************************************
                """)
                while True:
                    try:
                        islem = input("Yapmak İstediğiniz işlem: ")
                        if islem == "q" or islem == "Q":
                            print("Hesap Makinesinden çıkılıyor.....")
                            time.sleep(1)
                            print("Hesap Makinesinden Çıkış Yapıldı!")
                            break
                        else:
                            islem = int(islem)
                            if islem == 1:
                                toplama_adet = int(input("Kaç Adet Sayı Toplucaksınız : "))
                                toplam = 0
                                i = 1
                                adet = 1
                                while i <= toplama_adet:
                                    sayi = int(input("{}.Sayı: ".format(adet)))
                                    toplam += sayi
                                    adet += 1
                                    i += 1
                                print("Toplama İşlemi Yapılıyor...")
                                time.sleep(1)
                                print("Sayıların Toplamı {}".format(toplam))
                            elif islem == 2:
                                sayi1 = int(input("SAYI1: "))
                                sayi2 = int(input("SAYI2: "))
                                sonuc = sayi1 - sayi2
                                print("Çıkarma İşleminiz Yapılıyor....")
                                time.sleep(1)
                                print("{}-{}={}".format(sayi1, sayi2, sonuc))
                            elif islem == 3:
                                carpma_adet = int(input("Kaç Adet Sayı Çarpıcaksınız : "))
                                carpim = 1
                                i = 1
                                adet = 1
                                while i <= carpma_adet:
                                    sayi = int(input("{}.Sayı: ".format(adet)))
                                    carpim *= sayi
                                    adet += 1
                                    i += 1
                                print("Çarpma İşlemi Yapılıyor...")
                                time.sleep(1)
                                print("Sayıların Çarpımı {}".format(carpim))
                            elif islem == 4:
                                sayi1 = int(input("SAYI1: "))
                                sayi2 = int(input("SAYI2: "))
                                sonuc = sayi1 / sayi2
                                print("Bölme İşleminiz Yapılıyor....")
                                time.sleep(1)
                                print("{}/{}={}".format(sayi1, sayi2, sonuc))
                            elif islem == 5:
                                taban = int(input("Taban: "))
                                us = int(input("Üst: "))
                                sonuc = math.pow(taban, us)
                                print("İşleminiz Yapıluyor...")
                                time.sleep(1)
                                print("{} üstü {} = {}".format(taban, us, sonuc))
                            elif islem == 6:
                                sayi = int(input("Sayı: "))
                                kok = math.sqrt(sayi)
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("{} Sayısının karekökü = {}".format(sayi, kok))
                            elif islem == 7:
                                sayi = int(input("Sayı: "))
                                faktoriyel = math.factorial(sayi)
                                print("İşleminiz Yaplıyor...")
                                time.sleep(1)
                                print("{}! = {}".format(sayi, faktoriyel))
                            elif islem == 8:
                                sayi1 = int(input("Sayı1: "))
                                sayi2 = int(input("Sayı2: "))
                                permutasyon = math.perm(sayi1, sayi2)
                                print("İşleminiz Yapılıyor....")
                                time.sleep(1)
                                print("per({},{}) = {}".format(sayi1, sayi2, permutasyon))
                            elif islem == 9:
                                sayi1 = int(input("Sayı1: "))
                                sayi2 = int(input("Sayı2: "))
                                kombinasyon = math.comb(sayi1, sayi2)
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("comb({},{})={}".format(sayi1, sayi2, kombinasyon))
                            elif islem == 10:
                                sayi1 = int(input("Sayı1: "))
                                sayi2 = int(input("Sayı2: "))
                                mod = sayi1 % sayi2
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("{} ın {} e bölümünden kalan = {}".format(sayi1, sayi2, mod))
                            elif islem == 11:
                                sayi1 = int(input("Sayı1: "))
                                sayi2 = int(input("Sayı2: "))
                                ebob = math.gcd(sayi1, sayi2)
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("EBOB({},{})={}".format(sayi1, sayi2, ebob))
                            elif islem == 12:
                                sayi1 = int(input("Sayı1: "))
                                sayi2 = int(input("Sayı2: "))
                                ekok = math.lcm(sayi1, sayi2)
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("EKOK({},{})={}".format(sayi1, sayi2, ekok))
                    except ValueError:
                        print("Geçerli bir işlem giriniz")
            else:
                for i in range(1, len(self.uygulamalar) + 1):
                    if islem == i:
                        self.acik_uygulama = self.uygulamalar[i - 1]
                        print("{} Uygulaması Açılıyor...".format(self.uygulamalar[i - 1]))
                        time.sleep(1)
                        print("{} Uygulaması Açıldı!".format(self.acik_uygulama))
        except ValueError:
            print("Geçerli Bir İşlem Giriniz!!")
    def yukseltme(self):
        print("""
        1-) Hard Disk Yükseltme
        2-) Ram Yükseltme 
        3-) Anakart Yükseltme
        4-) İşlemci Yükseltme
        5-) Çıkış
        """)
        toplam=0
        while True:
            try:
                islem = int(input("Yapmak İstediğiniz İşlem: "))
                if islem == 1:
                    print("""
                    1-) 500 Gb = 500 Tl
                    2-) 1 Tb = 1000 Tl
                    3-) 2 Tb = 2000 Tl
                    4-) 4 Tb = 3500 Tl
                    5-) Çıkış
                    """)
                    while True:
                        try:
                            hdd_islem = int(input("Hangisine Yükseltmek İstersiniz: "))
                            if hdd_islem == 1:
                                self.hard_dik = 500
                                toplam += 500
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("İşlem Başarılı HDD: {} GB Tutar: 500 TL".format(self.hard_dik))
                                break
                            elif hdd_islem == 2:
                                self.hard_dik = 1000
                                toplam += 1000
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("İşlem Başarılı HDD: {} GB Tutar: 1000 TL".format(self.hard_dik))
                                break
                            elif hdd_islem == 3:
                                self.hard_dik = 2000
                                toplam += 2000
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("İşlem Başarılı HDD: {} GB Tutar: 2000 TL".format(self.hard_dik))
                                break
                            elif hdd_islem == 4:
                                self.hard_dik = 4000
                                toplam += 3500
                                print("İşleminiz Yapılıyor...")
                                time.sleep(1)
                                print("İşlem Başarılı HDD: {} GB Tutar: 3500 TL".format(self.hard_dik))
                                break
                            elif hdd_islem == 5:
                                print("Yükseltme İşlemi Yapılmadı Çıkıs Yapılıyor...")
                                time.sleep(1)
                                print("Çıkış Yapıldı!")
                                break
                            else:
                                print("Geçerli bir Seçim Yapınız!")
                        except ValueError:
                            print("Geçerli bir Seçim Yapınız!")
                elif islem == 2:
                    print("""
                    1-) 8 GB = 500
                    2-) 16 GB = 1000
                    3-) 32 GB = 2500
                    4-) Çıkış
                    """)
                    while True:
                        try:
                            ram_islem = int(input("Yükseltmek İstediğiniz Seçenek: "))
                            if ram_islem == 1:
                                print("Yükseltme İşlemi Yapılıyor...")
                                time.sleep(1)
                                self.ram = 8
                                toplam += 500
                                print("Yükseltme İşlemi Başarılı Ram: {} Tutar: 500 TL".format(self.ram))
                                break
                            elif ram_islem == 2:
                                print("Yükseltme İşlemi Yapılıyor...")
                                time.sleep(1)
                                self.ram = 16
                                toplam += 1000
                                print("Yükseltme İşlemi Başarılı Ram: {} Tutar: 1000 TL".format(self.ram))
                                break
                            elif ram_islem == 3:
                                print("Yükseltme İşlemi Yapılıyor...")
                                time.sleep(1)
                                self.ram = 32
                                toplam += 3500
                                print("Yükseltme İşlemi Başarılı Ram: {} Tutar: 3500 TL".format(self.ram))
                                break
                            elif ram_islem == 4:
                                print("Yükseltme İşlemi Yapılmadı Çıkıs Yapılıyor...")
                                time.sleep(1)
                                print("Çıkış Yapıldı!")
                                break
                            else:
                                print("Geçeerli Bir İşlem Giriniz!")
                        except ValueError:
                            print("Geçeerli Bir İşlem Giriniz")
                elif islem == 3:
                    print("""
                    1-) Bronz Anakart = 500 TL
                    2-) Altın Anakart = 1500 TL
                    3-) Emas Anakart = 2500 TL
                    4-) Çıkış
                    """)
                    while True:
                        try:
                            anakart_islem = int(input("Yükseltmek İstediğiniz Seçeneği Seçiniz: "))
                            if anakart_islem == 1:
                                print("Yükseltme Yapılıyor...")
                                time.sleep(1)
                                self.anakart = "Bronz Anakart"
                                toplam += 500
                                print("Yükseltme Tamamlandı! Anakart: {} Tutar: 500 TL".format(self.anakart))
                                break
                            elif anakart_islem == 2:
                                print("Yükseltme Yapılıyor...")
                                time.sleep(1)
                                self.anakart = "Altın Anakart"
                                toplam += 1500
                                print("Yükseltme Tamamlandı! Anakart: {} Tutar: 1500 TL".format(self.anakart))
                                break
                            elif anakart_islem == 3:
                                print("Yükseltme Yapılıyor...")
                                time.sleep(1)
                                self.anakart = "Elmas Anakart"
                                toplam += 2500
                                print("Yükseltme Tamamlandı! Anakart: {} Tutar: 2500 TL".format(self.anakart))
                                break
                            elif anakart_islem == 4:
                                print("Yükseltme Yapılmadı Çıkış Yapılıyor...")
                                time.sleep(1)
                                print("Çıkış Yapıldı!")
                                break
                            else:
                                print("Geçerli Bir İşlem Giriniz!")
                        except ValueError:
                            print("Geçerli Bir Seçim Yapınız!")
                elif islem == 4:
                    print("""
                    1-) Bronz İşlemci = 500 TL
                    2-) Altın İşlemci = 1500 TL
                    3-) Emas İşlemci = 2500 TL
                    4-) Çıkış
                    """)
                    while True:
                        try:
                            islemci_islem = int(input("Yükseltmek İstediğiniz Seçenek: "))
                            if islemci_islem == 1:
                                print("Yükseltme İşlemi Yapılıyor...")
                                time.sleep(1)
                                self.islemci = "Bronz İşlemci"
                                toplam += 500
                                print("Yükseltme Başarılı! İşlemci= {} Tutar: 500 TL".format(self.islemci))
                                break
                            elif islemci_islem == 2:
                                print("Yükseltme İşlemi Yapılıyor...")
                                time.sleep(1)
                                self.islemci = "Altın İşlemci"
                                toplam += 1500
                                print("Yükseltme Başarılı! İşlemci= {} Tutar: 1500 TL".format(self.islemci))
                                break
                            elif islemci_islem == 3:
                                print("Yükseltme İşlemi Yapılıyor...")
                                time.sleep(1)
                                self.islemci = "Elmas İşlemci"
                                toplam += 2500
                                print("Yükseltme Başarılı! İşlemci= {} Tutar: 2500 TL".format(self.islemci))
                                break
                            elif islemci_islem == 4:
                                print("Yükseltme Yapılmadı Çıkış Yapılıyor...")
                                time.sleep(1)
                                print("Çıkış Yapıldı!")
                                break
                            else:
                                print("Geçerli Bir İşlem Giriniz!")
                        except ValueError:
                            print("Geçerli Bir İşlem Giriniz!")
                elif islem== 5:
                    print("Çıkış Yapılıyor...")
                    time.sleep(1)
                    print("Çıkış Yapıldı!")
                    break
                else:
                    print("Geçerli Bir İşlem Giriniz!")
            except ValueError:
                print("Geçerli Bir İşlem Giriniz!")

        print("""
        Yükseltme İşlemleri Başarılı
             Hard Disk: {}
             Ram: {}
             Anakart: {}
             İşlemci: {}
             Toplam Tuar: {}
        """.format(self.hard_dik, self.ram, self.anakart, self.islemci, toplam))
    def __str__(self):
        return "Durum: {}\nMarka: {}\nHard Disk: {} GB\nRam: {} GB\nAnakart: {}\nİşlemci: {}\nYüklü Uygulamalar: {}\nAçık Uygulama: {}".format(self.durum,self.marka,self.hard_dik,self.ram,self.anakart,self.islemci,self.uygulamalar,self.acik_uygulama)

marka=input("Marka: ")
while True:
    try:
        hard_disk = int(input("Hard Disk GB: "))
        break
    except ValueError:
        print("Geçerli Bir Hard disk değeri değeri Giriniz!")
while True:
    try:
        ram = int(input("Ram GB: "))
        break
    except ValueError:
        print("Geçerli Ram değeri Giriniz!")
anakart=input("Anakart: ")
islemci=input("İşlemci: ")
bilgisayar=Bilgisayar(marka,hard_disk,ram,anakart,islemci)
print("""
1) AÇMA
2-) KAPATMA
3-) UYGULAMA EKLE
4-) UYGULAMA AÇ
5-) YÜKSELTME YAP
6-) BİLGİSAYAR BİLGİLERİ
7-) ÇIKIŞ
""")
while True:
    try:
        islem=int(input("Yapmak İstediğiniz İşlem: "))
        if islem==1:
            bilgisayar.acma()
        elif islem==2:
            bilgisayar.kapatma()
        elif islem==3:
            bilgisayar.uygulama_ekle()
        elif islem==4:
            bilgisayar.uygulama_ac()
        elif islem==5:
            bilgisayar.yukseltme()
        elif islem==6:
            print(bilgisayar)
        elif islem==7:
            print("Programdan Çıkış Yapılıyor...")
            time.sleep(1)
            print("Çıkış Yapıldı!")
            break
        else:
            print("Geçerli Bir İşlem Giriniz!")
    except ValueError:
        print("Geçerli Bir İşlem Giriniz!")


