print("*********Fibonacci*********")
sayi=int(input("Kaç Elemanlı Seri : "))
liste=[1,1]
for i in range(0,sayi+1):
    seri=liste[i]+liste[i+1]
    liste.append(seri)
print(liste)

