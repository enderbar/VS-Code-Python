fiyat = int(input("Lütfen bilet fiyatını giriniz:"))
agirlik = float(input("Lütfen bavul ağırlığı giriniz:"))
ogrenciMi = str(input("Öğreni misiniz? (Evet/Hayır): "))
if agirlik>15.0:
    fiyat += (agirlik-15)*5
if ogrenciMi == "Hayır":
    fiyat*=1.18
print(f"Bilet fiyatınız: {round(fiyat, 2)}")   