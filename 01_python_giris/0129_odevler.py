#region ödev 1
"""
km = int(input("Kilomentre bilgisi giriniz: "))
mil = km/1.609344
print(f" Girilen kilometre bilgisi: {km} \n Girilen değerin mil karşılığı: {mil} ")
"""
#endregion
#region ödev 2
"""
a = int(input("A köşe açısını giriniz: "))
b = int(input("B köşe açısını giriniz: "))
c = 180-a-b 
print(f"Girilen A değeri: {a}\nGirilen B değeri: {b}\nC köşe açısı: {c}")
"""
#endregion
#region ödev 3
"""
x1 = int(input("x1 değeri giriniz:"))
x2 = int(input("x2 değeri giriniz:"))
y1 = int(input("y1 değeri giriniz:"))
y2 = int(input("y2 değeri giriniz:"))
x=abs(x1-x2)
y=abs(y1-y2)
sonuc=(x**2+y**2)**0.5
print(f"Girilen noktalar arası uzaklık: {round(sonuc, 2)}")
"""
#endregion
#region ödev 4
"""
at=int(input("Aylık tüketim giriniz:"))
aeb=at*0.39736
db=aeb*0.2474
teb=aeb+db
kdv=(teb+3.97+1.39+9.92)*0.18
vgt=3.97+1.39+9.92+kdv
topFatura=vgt+teb
print(f"Aylık elektrik faturanız: {topFatura} TL")
"""
#endregion
#region ödev 5
"""
gbi=float(input("Güncel benzin indeksini giriniz:"))
yt=float(input("100 km başına yakıt tüketimini giriniz:"))
alınanYol=int(input("Kaç kilometre yol aldığınızı giriniz:"))
yakit=alınanYol/100*yt*gbi
print(f"Toplam Yakıt Tüketiminiz: {yakit} Litre")
"""
#endregion
#region ödev 6
"""
x=input("Ürün adınızı giriniz:")
y=int(input(f"{x} - Satın alınacak adet:"))
z=float(input("Ürün fiyatı giriniz:"))
t=int(input("% İndirim oranını giriniz:"))
tutar=z*y*((100-t)/100)
print(f"Ödenecek tutar: {tutar} TL")
"""
#endregion













