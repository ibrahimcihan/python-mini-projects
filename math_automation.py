import math

def topla(a,b):
    işlem = a+b
    return işlem
def çarp(a,b):
    işlem = a*b
    return işlem
def böl(a,b):
    işlem = a/b
    return işlem
def çıkart(a,b):
    işlem = a-b
    return işlem
def üs_alma(a,b):
    işlem = a**b
    return işlem

print("***************************MATEMATİK SİHİRBAZINA HOŞGELDİNİZ*******************************")

while True:
    print("Ne yapmak istersiniz?")
    print("1 => 4 işlem hesaplama\n2 => Faktoriyel hesaplama\n3 => Üssünü alma\nÇıkış => Herhangi bir karakter giriniz.")
    seçim = input("Seçim Yapınız: ")
        
    if seçim == "1":

        print("Hangi operatörü kullanmak istersiniz?")
        print("1 => (+)\n2 => (-)\n3 => (*)\n4 => (/)\nÇıkış => Herhangi bir karakter giriniz.")
        seçim = input("Seçim Yapınız: ")

            
        if seçim == "1" :
            a = int(input("Bir sayı giriniz: "))
            b = int(input("Bir sayı giriniz: "))
            print("Sonuç:",topla(a,b))
        
        elif seçim == "2" :
            a = int(input("Bir sayı giriniz: "))
            b = int(input("Bir sayı giriniz: "))
            print("Sonuç:",çıkart(a,b))
            
        elif seçim == "3" :
            a = int(input("Bir sayı giriniz: "))
            b = int(input("Bir sayı giriniz: "))
            print("Sonuç:",çarp(a,b))
            
        elif seçim == "4" :
            a = int(input("Bir sayı giriniz: "))
            b = int(input("Bir sayı giriniz: "))
            print("Sonuç:",böl(a,b))            
            
        else:
            break
        
    elif seçim == "2":
        a = int(input("Bir sayi giriniz: "))
        print("Sonuç:",math.factorial(a))

    elif seçim == "3":
        a = int(input("Bir sayı giriniz: "))
        b = int(input("Üssünü giriniz: "))
        print("Sonuç:",üs_alma(a,b))

    else:
        break
