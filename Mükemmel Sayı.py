print("*******Mükemmel Sayı********")
sayi=int(input("Bir Sayı Giriniz: "))
toplam=0
for i in range(1,sayi):
    if sayi%i==0:
        toplam+=i
if toplam==sayi:
    print("{} Sayısı Mükemmel Bir sayıdr.".format(sayi))
else:
    print("{} Sayısı Mükemmel Bir sayıl Değildir.".format(sayi))
