def unit():
    a = input("What is the unit?(With a unit, kilogram(kg), gram(g) or pound(lbs)): ").strip().lower()
    b = input("What unit you want to change into? kg, g or lbs? :").strip().lower()
    c = float(input("How heavy is your object(Withput unit)? ").strip())
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
    else:
        print("Your inputs are incorrect, please try again (Reminder: Units are to be written as labled)\n")
        unit()

if __name__ == "__main__":
    unit()
