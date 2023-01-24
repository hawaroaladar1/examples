def prim_e(szam):
    for i in range(2, szam):
        if szam % i == 0:
            return False
    return True

def primek(tol, ig):

    prim_lista = []

    for num in range(tol, ig + 1):
        
        if prim_e(num) == True:
            prim_lista.append(num)

    return prim_lista


elso_szam = int(input("tol = "))
masodik_szam = int(input("ig = "))

listam_prim = primek(elso_szam, masodik_szam)

if len(listam_prim) == 0:
    print("Nincs az adott 2 érték között prímszám! ")

elif len(listam_prim) > 0:
    print(f"A kettő érték közötti primek: {listam_prim}")