def mukemmel(sayi):
    toplam=0
    for i in range(1,sayi):
        if sayi%i==0:
            toplam+=i
    return toplam==sayi

sayi1=int(input("Kaça kadar olan Mükemmel sayıları bulmak istersiniz : "))
for i in range(1,sayi1):
    if mukemmel(i):
        print("{} mükemmel bir sayıdır".format(i))


