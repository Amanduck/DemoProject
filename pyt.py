#program wyliczajacy miejsca zerowe i przedzialy
#wersja 0.07
a= input("Podaj a: ")
b= input("Podaj b: ")
c= input("Podaj c: ")
if a==0:
    print("To jest funkcja liniowa. ")
else:
    print("GOOOD SOUP")
    

delta=int(b)*int(b)-4*int(a)*int(c)
if delta==0:
    x=(-b+delta)/2*a
    print("Ta funkcja ma jedno miejsce zerowe. Jest nim: "+ x)
    if a>0:
        print("Funckja jest malejaca na przedzialach (-niesk, "+x+"). Funckja jest rosnaca na przedzialach: ("+x+", -niesk). ")
    else: print("gud")
else: print("hah")