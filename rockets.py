def rockets():
    import math
    x = (input("What would you like to calculate relating to a rockets? \n(1: Thrust required to take off) \n(2: drag force) \n(3: Orbital Velocity/Escape Velocity)\n> "))
    x = x.strip()
    if x == "1":
        print("Looks like you want to calculate thrust. Here's the information I will need from you. Mass of Rocket, Acceleration of Gravity (9.81m/s^2 for Earth), and desired acceleration")
        for i in range(10000000000):
            m = float(input("Please enter the mass of your rocket (Kg) > "))
            g = float(input("Please enter the gravitational acceleration (m/s^2) > "))
            a = float(input("Please enter the desired acceleration (m/s^2) > "))
            for i in range(10000000):
                if m > 0 and g > 0 and a > 0:
                    T = m * (g + a)
                    print(f"The minimum thrust required to liftoff for your rocket is {T} Newtons")   
                else:
                    print("Your inputs are invalid, try again (Reminder: The numbers can't be negative)")
                    rockets()
                    break
    if x == "2":
        print("Looks like you want to calculate the drag force, in order to do so, I will need the air density, velocity, drag coefficient and the cross-sectional area.")
        for i in range(10000000000):
            p = float(input("\n Please enter the air density> "))
            v = float(input("\n Please enter the velocity of the rocket> "))
            d = float(input("\n Please enter the drag coefficient> "))
            A = float(input("\n Please enter the cross-sectional area> "))
            for i in range(10000000):
                if p > 0 and v > 0 and d > 0 and A > 0:
                    F = (1/2)*(p)*(v ** 2)*(d)*(A)
                    print(f"The drag force is {F} Newtons")
                    return
                else:
                    print("Your inputs are invalid, try again (Reminder: The numbers can't be negative) \n")
                    rockets()
                    break
    if x == "3":
        for i in range(1000000000000):
            j = input("Please specify what you'd like to calculate (1. Orbital Velocity)(2. Escape Velocity)> ")
            if j == "1":
                print("To calculate the Orbital Velocity, I will need the mass of the object you're orbiting, and the distance to the object")
                for i in range(10000000000):
                    m = float(input("\n Please enter the mass of the object (Kg)> "))
                    r = float(input("\n Please enter the distance from the object (meters)> "))
                    G = 6.674 * (10 ** -11)
                    for i in range(10000000):
                        if m > 0 and r > 0:
                            Vo = math.sqrt((G * m) / (r))
                            Vo = round(Vo, 4)
                            print(f"The orbital velocity is {Vo} m/s")
                            return
                        else:
                            print("Your inputs are invalid, try again (Reminder: The numbers can't be negative) \n")
                            rockets()
                            break
            elif j == "2":
                print("To calculate the Orbital Velocity, I will need the mass of the object you're orbiting, and the distance to the object")
                for i in range(10000000000):
                    m = float(input("\n Please enter the mass of the object (Kg)> "))
                    r = float(input("\n Please enter the distance from the object (meters)> "))
                    G = 6.674 * (10 ** -11)
                    for i in range(10000000):
                        if m > 0 and r > 0:
                            Ve = math.sqrt(2*(G * m) / (r))
                            Ve = round(Vo, 4)
                            print(f"The orbital velocity is {Ve} m/s")
                            return
                        else:
                            print("Your inputs are invalid, try again (Reminder: The numbers can't be negative) \n")
                            rockets()
                            break
            else:
                print("Your inputs are invalid, try again")   
                
    for i in range(100000):
        o = input("\n Would you like to calculate something else? (1. Yes)(2. No)> ")
        if o == "1":
            main()
            break
        elif o == "2":
            break
        else:
            print("the value you entered is invalid, try again")
    return
        

def main():
    rockets()
    
if __name__ == "__main__":
    main()