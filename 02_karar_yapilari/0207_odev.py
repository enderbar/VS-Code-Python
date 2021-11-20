a=int(input("Bakiye bilgisi giriniz:"))
b=str(input("Hesabın bulunduğu bankayı giriniz:"))
c=str(input("EFT Yapılacak bankayı giriniz:"))
d=int(input("Lütfen transfer edilecek EFT tutarı giriniz:"))
if b!=c:
    d*=1.1    
kalanMiktar=a-d
print(f"Hesapta kalan tutar: {kalanMiktar}")