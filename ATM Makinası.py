print("""
*********ATM MAKİNESİNE HOŞGELDİNİZ**********
İŞLEMLER:
1: BAKİYE SORGULAMA
2: PARA YATIRMA
3: PARA ÇEKME
*********************************************
Çıkış için 'q' ya basınız....
""")
bakiye=0
while True:
    islem = input("Yapmak İstediğiniz İşlem: ")
    if islem == "q" or islem=="Q":
        print("Atm makinasından Çıkış yapıldı Tekrar Bekleriz...")
        break
    if islem=="1":
        print("Bakiyeniz: {}TL dir".format(bakiye))
    elif islem=="2":
        yatirma=int(input("Yatırmak İstediğiniz Tutar: "))
        bakiye+=yatirma
        print("{}TL yatırdınız! Güncel Bakiye: {}".format(yatirma,bakiye))
    elif islem=="3":
        cekme=int(input("Çekmek İstediğiniz Tutar: "))
        bakiye-=cekme
        if bakiye<0:
            bakiye += cekme
            print("Bakiyeniz Yetersiz! Bakiye: {}".format(bakiye))
        else:
            print("{}TL Çekim Yaptınız Güncel Bakiye: {}".format(cekme,bakiye))
    else:
        print("Geçerli Bir İşlem Giriniz....")
