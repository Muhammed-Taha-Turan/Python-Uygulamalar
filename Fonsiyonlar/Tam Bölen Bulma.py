def tambolen(sayi):
    tambolen_liste=[]
    for i in range(1,sayi+1):
        if sayi%i ==0:
            tambolen_liste.append(i)
    return tambolen_liste

while True:
    girilen_sayi=input("Sayı giriniz veya çıkmak için q ya basınız: ")
    if girilen_sayi =="q" or girilen_sayi=="Q":
        print("çıkış yapıldı....")
        break
    else:
        girilen_sayi=int(girilen_sayi)
        print(tambolen(girilen_sayi))
        if len(tambolen(girilen_sayi))==2:
            print("Asal Sayıdır!!!")
