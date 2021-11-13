import random
import time
class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="Trt"):
        self.tv_durum =tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if self.tv_durum=="Kapalı":
            self.tv_durum = "Açık"
            print("Televizyon Açılıyor...")
            time.sleep(1)
            print("TV Açıldı...")
        else:
            print("Tevizyon Zaten Açık")
    def tv_kapat(self):
        if self.tv_durum=="Kapalı":
            print("Televizyon Zaten Kapalı...")
        else:
            self.tv_durum = "Kapalı"
            print("Televizyon Kapanıyor...")
            time.sleep(1)
            print("Televizyon Kapandı...")
    def ses_ayarlari(self):
        while True:
            cevap=input("Ses arttırmak için: +\nSes azaltmak için: -\nçıkmak için 'q' ya basınız: ")
            if cevap=="q" or cevap=="Q":
                print("Çıkış yapılıyor...")
                time.sleep(1)
                print("Çıkıs yapıldı... Ses Seviyesi: {}".format(self.tv_ses))
                break
            elif cevap=="+":
                if self.tv_ses<50:
                    self.tv_ses += 5
                    print("Ses Seviyesi {}".format(self.tv_ses))
                else:
                    print("Ses Seviyesi Maximum da....")
            elif cevap=="-":
                if self.tv_ses>0:
                    self.tv_ses -=5
                    print("Ses Seviyesi {}".format(self.tv_ses))
                else:
                    print("Ses Zaten 0 da")
            else:
                print("Lütfen '+' veya '-' değer giriniz!!!")
    def kanal_ekle(self):
        while True:
            ekleme=input("Eklemek İstediğiniz kanalı girin Çıkmak için 'q' ya basın: ")
            if ekleme=="q" or ekleme=="Q":
                print("Kanallar eklendi Çıkıs yapılıyor...")
                time.sleep(1)
                print("Çıkıs Yapıldı...\nKanal Listesi: {}".format(self.kanal_listesi))
                break
            else:
                self.kanal_listesi.append(ekleme)
                print("{} Kanalı Ekleniyor...".format(ekleme))
                time.sleep(1)
                print("{} Kanalı Eklendi...".format(ekleme))
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        return self.kanal
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durumu: {}\nSes Seviyesi: {}\nKanallar: {}\nŞuanki Kanal:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

print("""
********TELEVİZYON UYGULAMASI********
1-) Televizyon Aç
2-) Televizyon Kapat
3-) TV DURUMU
4-) SES DEĞİŞTİRME
5-) KANAL EKLE
6-) RASTGELE KANALA GİT
7-) TOPLAM KANAL ADETİ
8-) ÇIKIŞ
*************************************
""")
kumanda= Kumanda()
while True:
    try:
        islem = int(input("Yapmak İstediğiniz İşlem: "))
        if islem == 1:
            kumanda.tv_ac()
        elif islem == 2:
            kumanda.tv_kapat()
        elif islem == 3:
            print(kumanda)
        elif islem == 4:
            kumanda.ses_ayarlari()
        elif islem == 5:
            kumanda.kanal_ekle()
        elif islem == 6:
            print("Açılan Kanal {}".format(kumanda.rastgele_kanal()))
        elif islem == 7:
            print("Kanal Sayısı: {}".format(len(kumanda)))
        elif islem == 8:
            print("Programdan Çıkış Yapılıyor...")
            time.sleep(1)
            print("Çıkıs Yapıldı Yine Bekleriz...")
            break
        else:
            print("Geçerli Bir İşlem Giriniz....")
    except ValueError:
        print("Gçerli Bir İşlem Giriniz...")




