"""a=input("Metin girin:")
x=0
while x<5:
    print(a)
    x+=1"""

i, j = 1, 1
while i<16:
    while j<16:
        print(f"{i}.K {j}.Oda", end=(" "))
        j +=1
    i += 1
    j = 1
    print()