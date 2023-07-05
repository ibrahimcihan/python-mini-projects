import random

randomEleman = []
secimler = []

def randomSayıEkla(randomEleman):   
    sayac = 0
    elemanSayısı = int(input("Eleman sayısı giriniz: "))
    altSınır = int(input("Minimum deger giriniz: "))
    ustSınır = int(input("Maximum deger giriniz: "))
        
    while(True):
        sayac += 1

        if elemanSayısı < sayac:
            break
        else:
            sayi = random.randint(altSınır,ustSınır)
            randomEleman.append(sayi)

def sayilariTopla(randomEleman):
    topla = sum(randomEleman)
    return topla

def randomSecimYap():
    adet = int(input("Kaç sayı seçilsin: " ))
    
    if adet == 1:
        randomSecim = random.choice(randomEleman)
        secimler.append(randomSecim)
        print(secimler)
    
    elif adet > 1:  
        while True:
            if adet <= len(secimler):
                print(secimler)
                break
            else:
                x = random.choice(randomEleman)
                secimler.append(x)
                
while(True):
    
    print("******************** MENU ********************")
    print("Seçim '1' => Dizi oluştur. \nSeçim '2' => Diziyi Göster. \nSeçim '3' => Dizinin elemanlarını topla. \nSeçim '4' => Elemanları küçükten büyüğe sırala. \nSeçim '5' => Rastgele eleman veya elemanlar seç. \nSeçim '6' => Seçilen eleman listesini görüntüle. \nSeçim '0' => Çıkış Yap.")

    secim = input("Lütfen yapmak istediğini işlemi seçiniz: ")

    if secim == "0":
        print("Çıkış Yapılıyor...")
        print("Yine Bekleriz...")
        break

    elif secim == "1":
        randomSayıEkla(randomEleman)

    elif secim == "2":
        print(randomEleman)
        print("Eleman Sayısı: ",len(randomEleman))
    
    elif secim == "3":
        print(sum(randomEleman))
    
    elif secim == "4":
        randomEleman.sort(reverse=False)
        print(randomEleman)

    elif secim == "5":
        randomSecimYap()
    
    elif secim == "6":
        print(secimler)

    else:
        print("Geçersiz Seçim !!!")        