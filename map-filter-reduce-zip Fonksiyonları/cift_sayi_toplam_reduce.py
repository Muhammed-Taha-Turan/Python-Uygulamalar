from functools import reduce
def cift_mi(sayi):
    if sayi % 2 ==0:
        return True
    else:
        return False
def toplam(x,y):
    return x+y


liste=[1,2,3,4,5,6,7,8,9,10]
ciftsayilar=list(filter(cift_mi,liste))
print(reduce(toplam,ciftsayilar))
