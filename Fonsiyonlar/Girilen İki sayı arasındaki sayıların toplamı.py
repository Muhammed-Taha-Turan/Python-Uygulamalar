def ikisayi(sayi1,sayi2):
    toplam=0
    for i in range(sayi1+1,sayi2):
        toplam+=i
    return toplam

try:
    while True:

        sayi1 = int(input("Sayi1: "))
        sayi2 = int(input("Sayi2: "))
        if sayi1>sayi2:
            print("Sayı1 sayı2 den büyük olamazz!!!")
        else:
            print("{} ile {} arasındaki sayıların toplamı: {}".format(sayi1, sayi2, ikisayi(sayi1, sayi2)))
            break
except ValueError:
    print("Geçerli bir değer giriniz!!!")


