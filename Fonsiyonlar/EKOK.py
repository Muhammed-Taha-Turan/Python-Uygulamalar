def ekok(sayi1,sayi2):
    buyuk_sayi=0
    if sayi1 > sayi2:
        buyuk_sayi=sayi1
    elif sayi2 > sayi1:
        buyuk_sayi=sayi2
    else:
        buyuk_sayi=sayi1
    sayi1_katlar=set()
    sayi2_katlar=set()
    i=0
    sayi1_carpanlar=sayi1
    sayi2_carpanlar=sayi2
    while (i<=buyuk_sayi):
        sayi1_katlar.add(sayi1_carpanlar)
        sayi1_carpanlar+=sayi1
        sayi2_katlar.add(sayi2_carpanlar)
        sayi2_carpanlar+=sayi2
        i+=1
    ortak_kat=sayi1_katlar.intersection(sayi2_katlar)
    liste=[i for i in ortak_kat]
    liste.sort()
    return liste[0]
print("******EKOK******")
sayi_1=int(input("Sayı1 :"))
sayi_2=int(input("Sayı2: "))
print("EKOK({},{})={}".format(sayi_1,sayi_2,ekok(sayi_1,sayi_2)))




