#region odev1
"""
a=int(input("Sayı giriniz:"))
if a>0:
    a**=2
elif a<0:
    a**=0.5
else:
    a=0
print(f"{a}")
"""
#endregion
#region odev2
a=int(input("İlk sayıyı giriniz:"))
b1=int(input("İkinci sayıyı giriniz:"))
if a+b1>200:
    d=b1*0.25
    b2=b1*0.75
    c=a+b2
else:
    d=0
    c=a+b1
print(f"Ürünlerin fiyatı {a} ve {b1} TL'dir. İkinci ürüne {d} TL indirim yapılmıştır. Borcunuz {c} TL'dir.")
#endregion