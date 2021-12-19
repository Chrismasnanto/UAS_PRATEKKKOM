x = int(input("Masukkan bilangan: "))
for i in range(x):
    if i==0:
        print("#",end=" ")
        print("### "*(x-1))
    elif i==x - 1:
        print("### "*(x-1),end="")
        print("##")
    else:
        for j in range(x*2-1):
            print("#",end=" ")
        print("")