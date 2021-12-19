"""
for a in range(1, 11):
    print(f"{a}. Öğrenci" ,end=" ")
"""

"""tekToplam=0
while True:
    sayi=int(input("Lütfen sayı giriniz\t:"))
    if sayi!=-1:
        if sayi%2!=0:
            tekToplam+=sayi
        else:
            print("Lütfen tek sayı giriniz\t:")
    else:
        break 

print(tekToplam)"""

"""tekToplam=0
while True:
    sayi=int(input("Lütfen sayı giriniz\t:"))
    if sayi == -1:
        break
    if sayi%2==0:
        print("Lütfen tek sayı giriniz\t:")
        continue
    tekToplam+=sayi
print(tekToplam)"""


a=int(input("Kaç aylık?:"))
if a>=36 and a<=68:
    print("Hoşgeldiniz.")
else:
    print("Ana okuluna giremez.")

