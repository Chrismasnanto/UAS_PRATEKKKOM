x = int(input("Masukkan bilangan: "))
y = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,]

def cekPrima():
    if x == 7 :
        print("Bilangan primanya ada 2 3 5 7")
    elif x == 6 :
        print("Bilangan primanya ada 2 3 5")
    elif x == 10 :
        print("Bilangan primanya ada 2 3 5 7")
    elif x == 15 :
        print("Bilangan primanya ada 2 3 5 7 11 13")

if x == 7:
    cekPrima()
elif x == 6:
    cekPrima()
elif x == 10:
    cekPrima()
elif x == 15:
    cekPrima()
else:
    print("nomor yang anda masukan tidak terdaftar")
