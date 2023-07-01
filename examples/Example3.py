#Asal sayı bulma

sayi = int(input("bir sayi giriniz:"))
list = []

for i in range(2,sayi):
    durum = False
    for a in range(2,i):
        if i % a == 0:
            durum = True
            break
    if not durum:
        list.append(i)

for i in list:
    print(i)
print("0 ile {} arasında {} tane asal sayi vardır.".format(sayi,len(list)))    
