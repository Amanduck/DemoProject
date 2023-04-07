#algorithm for reducing formulas
#defining functions

#creating a new function
def newF (x):
    if x == "sin":
        return "cos"
    if x == "cos":
        return "sin"
    if x == "tg":
        return "ctg"
    if x == "ctg":
        return "tg"
#checks for quartet
def quart (angle):
    if angle < 90:
        return 1
    elif angle < 180:
        return 2
    elif angle < 270:
        return 3
    elif angle < 360:
        return 4
x="n"
while x == "n" or x== "N":
    print("")
    function= input("Give a name of the function (sin/cos/tg/ctg): ")
    print("")
    angle = 0
    while angle == 0 or angle == 90 or angle == 180 or angle == 270 or angle == 360: 
        print("Angle cannot be equal to 0, 90, 180, 270 or 360 degrees.")
        angle = int(input("Get angle: "))

    if angle > 360:
        angle = angle % 360

    quartet = quart(angle)

    sign = " "

    newFunction = function

    if quartet == 1:
        newFunction = newF(function)
    if quartet == 2:
        if function != "sin":
            sign = "-"
    elif quartet == 3:
        if function != "tg" and function != "ctg":
            sign = "-"
        newFunction = newF(function)
    else:
        if function != "cos":
            sign = "-"

    if quartet == 1:
        degrees = 90 - angle
    elif quartet == 2:
        degrees = 180 - angle
    elif quartet == 3:
        degrees = 270 - angle
    else:
        degrees = 360 - angle

    print("")
    print("The new function: " + str(sign) + newFunction + "(" + str(degrees) + ")")
    print("")
    print("Do you wanna leave? Y/N: ")
    x = input(" ")

