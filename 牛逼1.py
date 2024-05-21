<<<<<<< HEAD
def nb1():
    x = (float(input("Entre a mass of a")))
    y = (int(input("Is this object on erath?(1:yes)(2:no)")))
    if y == 2:
        z = (float(input("enter the gravity of this planet")))
        a = x * z
        print(f"The The gravity of this object is {a}N ")
    elif y == 1:
        b = x * 9.8
        print(f"The The gravity of this object is {b}N ")
    else:
        print("Wrong answer")
def main():
    nb1()

if __name__ == "__main__":
    main()   
=======
def force(x, F):
    x = (float(input("entre a mass of a> ")))
    F = x * 9.8
    print(F)
>>>>>>> 3a8c37d1c4ab4f08cffba7d37a57b6ed7ba7d1be
