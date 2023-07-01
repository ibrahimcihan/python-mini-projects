# n = 3
# 1/1! + 1/2! + 1/3! 
# hesaplayan programı yazınız.

n = int(input("n değeri giriniz: "))

def factorial(deger):
    sonuc = 1
    for x in range(1,deger+1):
        sonuc *= x
    return sonuc

toplam = 0
for i in range(1,n+1):  
    islem = 1/factorial(i)
    toplam = toplam + islem

print(toplam)



