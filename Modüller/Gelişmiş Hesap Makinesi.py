import math
import time

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
            print("Programdan çıkılıyor.....")
            time.sleep(1)
            print("Programdan Çıkış Yapıldı !!!")
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
