#program wyliczajacy miejsca zerowe i przedzialy monotonicznosci funkcji kwadratowej i funkcji liniowej
#wersja 0.5
#TypeError or ValueError


#BIG UPDATE
#Errors repaired by function str()

import math

print("Wzor funkcji kwadratowej ma postac: ax^2+bx+c.")

a= float(input("Podaj a: "))
b= float(input("Podaj b: "))
c= float(input("Podaj c: "))


if a==0:
    print("To jest funkcja liniowa. ")
    if b>0:
        print("Funkcja jest rosnaca.")
    elif b<0:
        print("Funkcja jest malejaca.")
    else:
        print("Funkcja jest stala.")
    

delta=float(b)*float(b)-4*float(a)*float(c)
if delta>=0:
    pierwiastek=math.sqrt(delta)


if delta==0:
    x=(-b+pierwiastek)/2*a
    print("Ta funkcja ma jedno miejsce zerowe. Jest nim: "+ str(x))
    if a>0:
        print("Funckja jest malejaca na przedzialach (-niesk, "+str(x)+"). Funckja jest rosnaca na przedzialach: ("+str(x)+", -niesk). ")
    else: print("Funckja jest rosnaca na przedzialach (-niesk, "+str(x)+"). Funckja jest malejaca na przedzialach: ("+str(x)+", -niesk). ")
elif delta<0:
    print("Funckja nie ma miejsc zerowych, bo delta jest ujemna.")
    if a>0:
        p=-b/2*a
        print("Wykres funkcji znajduje sie nad osia OX. Funckja jest malejaca w przedzialach (-niesk, "+str(p)+"), a rosnaca w przedzialach: ("+str(p)+", +niesk)")
    else:
        p=-b/2*a
        print("Wykres funkcji znajduje sie pod osia OX. Funckja jest rosnaca w przedzialach (-niesk, "+str(p)+"), a malejaca w przedzialach: ("+str(p)+", +niesk)")
else:
    x1=(-b+pierwiastek)/2*a
    x2=(-b-pierwiastek)/2*a
    print("Delta wynosi: "+str(delta)+", funckja ma 2 miejsca zerowe: "+str(x1)+" oraz "+str(x2)+". ")
    p=-b/2*a
    if a<0:
        print("Funckja jest rosnaca w przedzialach (-niesk, "+str(p)+"), a malejaca w przedzialach: ("+str(p)+", +niesk)")
    else:
       print("Funckja jest malejaca w przedzialach (-niesk, "+str(p)+"), a rosnaca w przedzialach: ("+str(p)+", +niesk)") 
