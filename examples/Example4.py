def metin(cumle,sayi=0):
    
    harfler="aeıioöuüAEIİOÖUÜ"

    for karakter in cumle:
        if karakter in harfler:
            sayi +=1
    return sayi

cumle = input("Bir cumle giriniz : ")
print("Cümledeki ünlü harf sayısı : {}".format(metin(cumle)))            