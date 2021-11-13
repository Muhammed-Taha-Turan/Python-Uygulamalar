import random
import time

print("***********SAYI TAHMİN OYUNU************")
rasgele_sayi=random.randint(1,40)
sayac=1
while True:
    girilen_sayi = int(input("1-40 ARASI BİR SAYİ GİRİNİZ : "))
    time.sleep(0.5)
    if girilen_sayi==rasgele_sayi:
        time.sleep(0.5)
        print("Tebrikler.... {}. denemede buldunuz".format(sayac))
        break
    elif girilen_sayi > rasgele_sayi:
        time.sleep(0.5)
        print("Girdiğiniz sayı büyük")
        sayac +=1
    else:
        time.sleep(0.5)
        print("Girdiğiniz sayı küçük")
        sayac+=1
    if sayac==7:
        print("Deneme Hakkınız Kalmadı...")
        break


