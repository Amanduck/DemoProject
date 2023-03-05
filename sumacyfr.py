liczba=int((input("Give me a number: ")))

sum=0
while liczba>0:
    sum=liczba%10+sum
    liczba=int(liczba/10)
print(sum)