'''def srednia():
    marks = []
    counter = int(input("Counter: "))
    srednia = 0.0
    for i in range(0, counter, 1):
        mark=input("Mark: ")
        srednia = 0.0
        marks.append(mark)
        sum = 0
        sum+=int(mark)
    srednia = sum/counter
    return srednia
print(srednia())'''


counter = int(input("Counter: "))
sum = 0
for i in range (int(counter)):
    mark = int(input("Mark: "))
    sum += mark
average = sum/counter
print(average)