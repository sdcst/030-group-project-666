def unit():
    a = input("What is the unit?(With a unit, kilogram(kg), gram(g) or pound(lbs)): ")
    b = input("What unit you want to change into? kg, g or lbs? :")
    c = float(input("How heavy is your object(Withput unit)? "))
    if a == "kg" and b == "g":
        d = c * 1000
        print(d, b)
    elif a == "kg" and b == "lbs":
        d=c*2.2
        print(d,b)
    elif a == "kg" and b == "kg":
        d=c*1
        print(d,b)
    elif a == "g" and b == "kg":
        d=c/1000
        print(d,b)
    elif a == "g" and b == "g":
        d=c*1
        print(d,b)
    elif a == "g" and b == "lbs":
        d=c*0.0022
        print(d,b)
    elif a == "lbs" and b == "kg":
        d=c*0.45
        print(d,b)
    elif a == "lbs" and b == "g":
        d=c*453.6
        print(d,b)
    elif a == "lbs" and b == "lbs":
        d=c*1
        print(d,b)
    

if __name__ == "__main__":
    unit()
