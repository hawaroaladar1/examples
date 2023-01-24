from math import sqrt

def elso_masodfoku(a, b, c):
    eredmeny01 = (- b + sqrt(b * b - 4 * a * c)) / 2 * a
    return eredmeny01

def masodik_masodfoku(a, b, c):
    eredmeny02 = (- b - sqrt(b * b - 4 * a * c)) / 2 * a
    return eredmeny02


def megoldasok(a, b, c):

    gyok_alatt = b * b - 4 * a * c


    if gyok_alatt < 0:
        return []
    
    elif gyok_alatt == 0:
        return [elso_masodfoku(a, b, c)]
    
    else:
        return [elso_masodfoku(a, b, c), masodik_masodfoku(a, b, c)]


a_szam = int(input("Adja meg az A értékét! "))
b_szam = int(input("Adja meg a B értékét! "))
c_szam = int(input("Adja meg a C értékét! "))


listam_megoldasok = megoldasok(a_szam, b_szam, c_szam)


if len(listam_megoldasok) == 0:
    print("Nincs megoldása! ")

elif len(listam_megoldasok) == 1:
    print(f"Egy megoldás van: {(listam_megoldasok)}")

else:
    print(f"A megoldások: {(listam_megoldasok)}")
