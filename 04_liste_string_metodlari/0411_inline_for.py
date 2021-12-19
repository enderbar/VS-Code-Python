# region ornek
"""
Haftanın 1. Günü Pazartesi  Haftanın 2. Günü Salı ...
"""
hafaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
# endregion
hafta=[f"Haftanın {a}. Günü: {hafaninGunleri[a]}" for a in range(1,8)]
print(hafta)