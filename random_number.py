import random

list = []
sayac = 0

min = int(input("Minimum değer: "))
max = int(input("Maksimum değer: "))
adet = int(input("Kaç tane sayı oluşturulsun: "))

while True:
    a = random.randrange(min,max+1) 
    sayac+=1
    if sayac < adet+1:
        list.append(a)
    else:
        print("Liste:",list)
        break