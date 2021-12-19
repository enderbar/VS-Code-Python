#region 1
"""
def sonuc():
    s1 = input("Lütfen sayı giriniz:")
    s2 = input("Lütfen sayı giriniz:")
    if s1.isdigit() and s2.isdigit():
        s1, s2 = int(s1), int(s2)
        if s1 > s2:
            return s1+s2
        elif s1 < s2:
            return s1-s2
        else:
            return s1, s2
    else:
        return "Lütfen sayısal değer giriniz."


print(sonuc())
"""
#endregion
"""
1→ birlestir isimli fonk. olacak
2→ birlestir() isimli fonk. iki ifadeyi birleştirecek
3→ birleştirirken de İlk harfleri büyük şekilde birleştirecek
	Örn: 	ali kemal
		Ali Kemal
"""
#region 2
"""
def birlestir(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return (a.capitalize(), b.capitalize())
print(birlestir("ender","barış"))
"""
#endregion

print(round(123455.8799789 , 3))
x = round(123455.8799789 , 3)
print(x)
