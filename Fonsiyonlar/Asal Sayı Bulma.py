def asalmi(sayi):
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                return False
        return True


while True:
    sayi = input("Bir Sayı Giriniz Çıkmak için q ya basınız :")
    if sayi == "q" or sayi == "Q":
        print("Programdan Çıkıldı...")
        break
    else:
        sayi = int(sayi)
        if asalmi(sayi):
            print("Sayı Asal")
        else:
            print("Asal Değil")
