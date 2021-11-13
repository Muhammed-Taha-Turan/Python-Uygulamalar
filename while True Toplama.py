toplam=0
while True:
    sayi=input("Bir sayı giriniz yada çıkak için q ya basınız: ")
    if sayi=="q" or sayi=="Q":
        print("Programdan çıkıldı...")
        break
    try:
        sayi=int(sayi)
        toplam+=sayi
    except ValueError:
        print("Geçerli bir değer giriniz!!!")
print("Sayıların toplamı : {}".format(toplam))