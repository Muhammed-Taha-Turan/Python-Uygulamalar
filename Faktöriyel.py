print("Çıkış için 'q' ya basınız....")
while True:
    sayi = (input("Bir Sayı Giriniz: "))
    if sayi=="q" or sayi=="Q":
        print("Programdan Çıkış Yapıldı....")
        break
    try:
        sayi = int(sayi)
        fak=1
        for i in range(1, sayi + 1):
                fak *= i
        print("Sayının Faktöriyeli= {}".format(fak))
        fak=1
    except ValueError:
        print("Geçerli bir değer giriniz!!!")

