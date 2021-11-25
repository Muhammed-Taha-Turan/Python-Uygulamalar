def cift_sayi(a):
    if a %2 ==0:
        return a
    else:
        raise ValueError("HATA FIRLATILDI...")
liste=[1,2,3,4,7,8,88,77,44,55,67,78,41]
for i in liste:
    try:
        print(cift_sayi(i))
    except ValueError:
        pass