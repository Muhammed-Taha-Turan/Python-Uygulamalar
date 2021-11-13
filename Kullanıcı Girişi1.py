print(".......Kayıt Ekranı.......")
kayit_kullanici=input("Kullanıcı Adınızı Giriniz: ")
kayit_sifre = input("Şifrenizi Giriniz: ")
print("Tebrikler Kayıt Başarılı...")
print(".......Giriş Ekranı........")
giris_hakki=3
while True:
    kullanici_ad = input("Kullanıcı Adınızı Griniz: ")
    sifre = input("Şifrenizi Giriniz: ")
    if (giris_hakki==1):
        print("Çok fazla hatalı giriş yaptınız Programdan Çıkılıyor...")
        break
    if (kayit_kullanici==kullanici_ad and kayit_sifre==sifre):
        print("Giriş Başarılı!!!")
        break
    elif (kayit_kullanici==kullanici_ad and kayit_sifre!=sifre):
        giris_hakki-=1
        print("{} Deneme hakkınız kaldı!".format(giris_hakki))
        print("Şifreniz Yanlış!!!")
        cikis=input("Çıkmak için 'q' ya basınız Devam etmek için 'enter! tuşuna basınız")
        if (cikis=="q" or cikis=="Q"):
            print("Çıkış Yapıldı!!!")
            break
    elif (kayit_kullanici!=kullanici_ad and kayit_sifre==sifre):
        giris_hakki -= 1
        print("{} Deneme hakkınız kaldı!".format(giris_hakki))
        print("Kullanıcı Adınız Yanlış!!!")
        cikis=input("Çıkmak için 'q' ya basınız Devam etmek için 'enter! tuşuna basınız")
        if (cikis=="q" or cikis=="Q"):
            print("Çıkış Yapıldı!!!")
            break
    else:
        print("Kullanıcı Adınız Ve Şifreniz Yanlış!!!")
        giris_hakki -= 1
        print("{} Deneme hakkınız kaldı!".format(giris_hakki))
        cikis=input("Çıkmak için 'q' ya basınız Devam etmek için 'enter! tuşuna basınız")
        if (cikis=="q" or cikis=="Q"):
            print("Çıkış Yapıldı!!!")
            break
