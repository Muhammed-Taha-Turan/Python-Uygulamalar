cumle=input("Bir Cümle Giriniz: ")
cumle=list(cumle)
harfler=set()
for i in cumle:
    adet=cumle.count(i)
    harfler.add("{} Karakteri {} Adet Geçmiştir".format(i,adet))

for i in harfler:
    print(i)