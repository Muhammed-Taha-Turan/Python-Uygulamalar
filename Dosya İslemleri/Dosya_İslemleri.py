import time
def ekleme_yap(dosya_ismi,eklenen):
    with open(dosya_ismi,"a",encoding="utf-8") as dosya_ismi:
        dosya_ismi.write(eklenen)
def dosya_okuma(dosya_ismi):
    with open(dosya_ismi,"r",encoding="utf-8") as dosya_ismi:
        print(dosya_ismi.read())

dosya_listesi=list()
while True:
    print("""
    1-)Dosya Listesi
    2-)Dosya Veri Ekleme
    3-)Dosya Okuma
    4-)Dosya Ekleme
    5-)Çıkış
    """)
    try:
        islem = int(input("Yapmak İstediğiniz İşlem: "))
        if islem==1:
            if len(dosya_listesi)==0:
                print("Listenizde Dosya Bulunmamaktadır...")
            else:
                print("işleminiz Yapılıyor...")
                time.sleep(1)
                a=1
                print("****Dosyalar*****")
                for i in dosya_listesi:
                    print("{}- {}".format(a,i))
                    a+=1
                print("*******************")
        elif islem==2:
            if len(dosya_listesi)==0:
                print("Dosyanız Bulunmamakta...")
                while True:
                    dosya_islemi=input("Yeni Dosya Olusturmak İstermisiniz? Y/N")
                    if dosya_islemi=="Y" or dosya_islemi=="y":
                        dosya_adi=input("Dosya Adını Giriniz")
                        dosya_adi+=".txt"
                        print("{} Dosyası Oluşturuluyor...".format(dosya_adi))
                        time.sleep(1)
                        dosya_listesi.append(dosya_adi)
                        with open(dosya_adi,"w",encoding="utf-8") as dosya_adi:
                            print("Dosya Olusturuldu...")
                    elif dosya_islemi=="n" or dosya_islemi=="N":
                        print("Ana Menüye Dönülüyor....")
                        time.sleep(1)
                        break
                    else:
                        print("Lütfen Geçerli Bir Değer Giriniz!!")
            else:
                sira=1
                for i in dosya_listesi:
                    print("{}-){}".format(sira,i))
                    sira+=1
                try:
                    dosya_Acma = int(input("Açmak İstediğiniz Dosya: "))
                    dosya_yolu=dosya_Acma-1
                    if dosya_Acma > len(dosya_listesi):
                        print("Listenizde {} adet dosya var!!".format(len(dosya_listesi)))
                    else:
                        print("{} Dosyası Açılıyor....".format(dosya_listesi[dosya_yolu]))
                        time.sleep(1)
                        print("{} Dosyası Açıldı!".format(dosya_listesi[dosya_yolu]))
                        while True:
                            veri = input("Ekelemek İstediğiniz Veri Cıkımak için 'q' ya basın: ")
                            if veri == "q" or veri == "Q":
                                print("Ana Menüye Dönülüyor...")
                                time.sleep(1)
                                break
                            else:
                                print("Ekleme Yapılıyor....")
                                time.sleep(1)
                                ekleme_yap(dosya_listesi[dosya_yolu], veri)
                                print("Ekleme Yapıldı")
                except ValueError:
                    print("Geçerli Bir Değer Giriniz!!")
        elif islem==3:
            if len(dosya_listesi)==0:
                print("Okunacak Bir Dosyanız Bulunmamaktadır...")
                while True:
                    dosya_islemi=input("Yeni Dosya Olusturmak İstermisiniz? Y/N")
                    if dosya_islemi=="Y" or dosya_islemi=="y":
                        dosya_adi=input("Dosya Adını Giriniz")
                        dosya_adi+=".txt"
                        print("{} Dosyası Oluşturuluyor...".format(dosya_adi))
                        time.sleep(1)
                        dosya_listesi.append(dosya_adi)
                        with open(dosya_adi,"w",encoding="utf-8") as dosya_adi:
                            print("Dosya Olusturuldu...")
                    elif dosya_islemi=="n" or dosya_islemi=="N":
                        print("Ana Menüye Dönülüyor....")
                        time.sleep(1)
                        break
                    else:
                        print("Lütfen Geçerli Bir Değer Giriniz!!")
            else:
                print("Dosyalar Listeleniyor...")
                time.sleep(1)
                sira = 1
                for i in dosya_listesi:
                    print("{}-){}".format(sira, i))
                    sira += 1
                while True:
                    try:
                        dosya_adi = input("Ekrana Yazdırmak İsrediğiniz Dosya Çıkmak için 'q' ya basınız: ")
                        if dosya_adi == "q" or dosya_adi == "Q":
                            print("Ana Menüye Dönülüyor...")
                            time.sleep(1)
                            break
                        else:
                            dosya_adi = int(dosya_adi)
                            print("Dosya Okunuyor...")
                            time.sleep(2)
                            if dosya_adi > len(dosya_listesi):
                                print("Listenizde {} Adet Dosya Bulunmaktadır!!".format(len(dosya_listesi)))
                            else:
                                dosya_okuma(dosya_listesi[dosya_adi - 1])
                    except ValueError:
                        print("Geçerli Bir Değer Giriniz")
        elif islem==4:
            dosya_adi = input("Dosya Adını Giriniz")
            dosya_adi += ".txt"
            print("{} Dosyası Oluşturuluyor...".format(dosya_adi))
            time.sleep(1)
            dosya_listesi.append(dosya_adi)
            with open(dosya_adi, "w", encoding="utf-8") as dosya_adi:
                print("Dosya Olusturuldu...")
        elif islem==5:
            print("Çıkış Yapılıyor...")
            time.sleep(1)
            print("Yine Bekleriz :) ")
            break
        else:
            print("Geçerli Bir İşlem Giriniz!!!")

    except ValueError:
        print("Geçerli Bir İşlem Giriniz!!!")











