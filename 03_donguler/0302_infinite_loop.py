eb = -999999999
sayi = int(input("lütfen sayı giriziniz, çıkmak için -1 yazınız : "))
while sayi != -1:
    sayi = int(input("lütfen sayı giriziniz, çıkmak için -1 yazınız : "))
    if sayi>eb:
        eb = sayi
print(eb)
