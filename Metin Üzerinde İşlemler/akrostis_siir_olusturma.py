import time


class Siir():
    def __init__(self):
        with open("siir.txt", "r", encoding = "utf-8") as dosya:
            self.siir = dosya.read()
            dosya.seek(0)
            satirlar = dosya.readlines()
            self.temiz_satirlar = list()
            for i in satirlar:
                i = i.strip("\n")
                i = i.strip(".")
                self.temiz_satirlar.append(i)

    def goruntule_siir(self):
        print(self.siir)

    def akrostis(self):
        akrostis = str()
        for i in self.temiz_satirlar:
            akrostis += i[0]
        print(akrostis)

dosya = Siir()
print(""" 
****işlemler:*****
------------------
1-)Şiiri YAZDIR
2-)akrostiş i çıkar
3-)Çıkış
----------------
""")
while True:
    try:
        islem = int(input("Yapmak İstediğiniz İşlem: "))
        if islem == 1:
            print("Şiir Ekrana Yazılıyor...")
            time.sleep(1)
            dosya.goruntule_siir()
        elif islem == 2:
            print("Akrostiş ortaya çıkarılıyor...")
            time.sleep(1)
            dosya.akrostis()
        elif islem == 3:
            print("Çıkış yapaılıyor...")
            time.sleep(1)
            print("Çıkıs Başarılı...")
            break
        else:
            print("Geçerli Bir İşlem Giriniz!!!")

    except:
        print("Geçerli Bir İşlem Giriniz!!!")
