def okunus(sayi):
    sayi = str(sayi)
    okunma = str()
    onlar_basamagi = {1: "on", 2: "yirmi", 3: "otuz", 4: "kırk", 5: "elli", 6: "altmış", 7: "yetmiş", 8: "seksen",
                      9: "doksan"}
    birler_basamagi = {1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz"}
    for k, v in onlar_basamagi.items():
        k = str(k)
        if k == sayi[0]:
            okunma += v
    for a, d in birler_basamagi.items():
        a = str(a)
        if a == sayi[1]:
            okunma += d

    return okunma


print("********SAYI OKUMA********")
while True:
    sayi = input(("İki Basamaklı Bir Sayı Giriniz Çıkmak İçin Q ya basınız: "))
    if sayi == "q" or sayi == "Q":
        print("Çıkış Yapıldı!!")
        break
    if len(sayi) != 2:
        print("İKİ BASAMAKLI BİR SAYI GİRİNİZ!!!")
    else:
        print("{} = {}".format(sayi, okunus(sayi)))
