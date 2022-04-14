
print(" EBOB Bulma Programi")

def ebobbulma(sayi1,sayi2):
    ebob = 1
    i = 1

    while (i<=sayi1 and i<=sayi2):

        if (not sayi1%i) and (not sayi2%i):
            ebob = i
        i+=1
    return ebob

sayi1 = int(input("Sayi-1:"))
sayi2 = int(input("Sayi-2:"))

print(ebobbulma(sayi1,sayi2))









