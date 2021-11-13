def pisagor(aralik):
    a=[*range(1,aralik+1)]
    b=[*range(1,aralik+1)]
    c=[*range(1,aralik+1)]
    ozel_ucgen = list()
    for i in a:
        d=i**2
        for k in b:
            e=k**2
            for j in c:
                f=j**2
                if d+e==f and c[j-1]>a[i-1] and c[j-1]>b[k-1] and b[k-1]>a[i-1]:
                    ozel_ucgen.append((a[i - 1], b[k - 1], c[j - 1]))
                elif d+f==e and c[j-1]>a[i-1] and c[j-1]>b[k-1] and b[k-1]>a[i-1]:
                    ozel_ucgen.append((a[i - 1], b[k - 1], c[j - 1]))
                elif f+e==d and c[j-1]>a[i-1] and c[j-1]>b[k-1] and b[k-1]>a[i-1]:
                    ozel_ucgen.append((a[i - 1], b[k - 1], c[j - 1]))
    return ozel_ucgen


aralik=int(input("Kaça kadar olan pisagor üçgenlerini bulmak istersiniz: "))
for i in pisagor(aralik):
    print(i)
