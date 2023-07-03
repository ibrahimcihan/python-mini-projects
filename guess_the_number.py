import random

sayi = random.randint(0,6)
deneme = 3
print("********** [0-5] arasındaki sayıyı tahmin et!!! **********")

while True:
    
    print("Kalan Hakkınız:",deneme)
    a = int(input("Sayıyı Tahmin Ediniz: "))
    deneme -= 1
    
    
    if deneme == 0:
        print("Hakkınız bitmiştir. Maalesef bilemediniz :))")
        break
    else:
        if sayi == a:
            print("Tebrikler!! Sayı:",sayi)
            break
        else:
            print("Tekrar deneyiniz")
        
