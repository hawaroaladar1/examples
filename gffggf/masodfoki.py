a = int(input("A értéke: "))
b = int(input("B értéke: "))
c = int(input("C értéke: "))


diszkr = b * b - 4 * a * c

if diszkr < 0:
    print("Nincs megoldás")

elif diszkr == 0:
    print("Egy megoldás van!")

else:
    print("Két megoldás van")