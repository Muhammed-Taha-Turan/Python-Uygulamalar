def alan(x,y):
    return x*y

alan_liste=[(3,4),(10,3),(5,6),(1,9)]
kenar1=list()
kenar2=list()
for i,k in alan_liste:
    kenar1.append(i)
    kenar2.append(k)

print(list(map(alan,kenar1,kenar2)))
