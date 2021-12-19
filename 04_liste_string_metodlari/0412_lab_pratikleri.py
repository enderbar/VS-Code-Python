ogrenci1 = ["Alp", "Besi", 90,	90]
ogrenci2 = ["Batu", "Koçhan", 10, 90]
ogrenci3 = ["Emir", "Besi", 100,	90]
ogrenci4 = ["Umut", "Ahmet", 95, 80]
ogrenci5 = ["Aziz", "Bektaş", 15, 10]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]
for i in ogrenciler:
    ort=(i[2]+i[3])/2
    if ort<50:
         print(f"Öğrenci adı soyadı: {i[0]} {i[1]} aldığı notlar: {i[2]}, {i[3]}. Kaldı.")
    else:
        print(f"Öğrenci adı soyadı: {i[0]} {i[1]} aldığı notlar: {i[2]}, {i[3]}. Geçti.")