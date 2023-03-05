

a=int(input("Podaj a:"))

d = ''
while a > 0:
    d = str(a % 2) + d
    a = int(a / 2)
    print(d)
    print(str(a)+".")
print(d)

