#1000-9999 arasındaki sayılarda ilk iki basamaktaki rakamların toplamı son iki basamaktaki rakamların toplamına eşit olan sayıları gösteren programı yazınız. (1001 => 1+0 = 0+1)

numbers = range(1000,9999)
desired_numbers = []
list_index = 0

for i in numbers:
    a = str(numbers[list_index])
    if int(a[0]) + int(a[1]) == int(a[2]) + int(a[3]):
        desired_numbers.append(i)
        list_index += 1
    else:
        list_index += 1

count = 1
for number in desired_numbers:
    print(count,".number: ",number)
    count+=1
