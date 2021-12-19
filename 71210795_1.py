#program 2 input

pertama = int(input("Masukkan angka pertama: "))
kedua = int(input("Masukkan angka kedua: "))

if pertama %2==0 and pertama %2==0:
    print("Hasil yang didapat adalah: ", (pertama ** kedua))
elif pertama %2!=0 and kedua %2!=0:
    print("Hasil yang didapat adalah: ", (pertama - kedua))
elif pertama %2!=0 and kedua %2==0:
    print("Hasil yang didapat adalah: ", (pertama / kedua))
elif pertama %2==0 and kedua %2!=0:
    print("Hasil yang didapat adalah: ", (pertama + kedua))