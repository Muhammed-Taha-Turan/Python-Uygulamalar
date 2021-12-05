def kontrol_ucgen(kenar):

    if abs(kenar[1]-kenar[2]) < kenar[0] and kenar[0]<kenar[1]+kenar[2]:
        return True
    elif abs(kenar[0]-kenar[2])<kenar[1] and kenar[1]<kenar[0]+kenar[2]:
        return True
    elif abs(kenar[0]-kenar[1])<kenar[2] and kenar[2]<kenar[0]+kenar[1]:
        return True
    else:
        return False



ucgen_liste=[(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(kontrol_ucgen,ucgen_liste)))