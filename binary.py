

dziesietna=int(input("Podaj liczbe dziesietna: "))

bin=''
while dziesietna>0:
    bin=str(dziesietna%2)+bin
    dziesietna=int(dziesietna/2)
print(bin)

