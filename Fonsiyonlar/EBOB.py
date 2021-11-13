def ebob(sayi1, sayi2):
    sayi1_bolenler = set()
    sayi2_bolenler = set()
    for i in range(1, sayi1 + 1):
        if sayi1 % i == 0:
            sayi1_bolenler.add(i)
    for j in range(1, sayi2 + 1):
        if sayi2 % j == 0:
            sayi2_bolenler.add(j)
    ortak_katlar = sayi2_bolenler.intersection(sayi1_bolenler)
    liste = [i for i in ortak_katlar]
    liste.sort()
    return liste[-1]


sayi_1 = int(input("SAYI1: "))
sayi_2 = int(input("SAYI2: "))
print("EBOB({},{}) = {}".format(sayi_1, sayi_2, ebob(sayi_1, sayi_2)))
