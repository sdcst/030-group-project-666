def rockets():
    x = int(input("What would you like to calculate relating to a rockets? \n(1: Thrust required to take off) \n(2: drag force) \n(3: Orbital Velocity/Escape Velocity)\n> "))
    
    if x == 1:
        print("Looks like you want to calculate thrust. Here's the information I will need from you. Mass of Rocket, Acceleration of Gravity (9.81m/s^2 for Earth), and desired acceleration")
        for i in range(10000000000):
            m = float(input("Please enter the mass of your rocket (Kg) > "))
            g = float(input("Please enter the gravitational acceleration (m/s^2) > "))
            a = float(input("Please enter the desired acceleration (m/s^2) > "))
            for i in range(10000000):
                if m > 0 and g > 0 and a > 0:
                    T = m * (g + a)
                    print(f"The minimum thrust required to liftoff for your rocket is {T} Newtons")
                    return 
                else:
                    print("Your inputs are invalid, try again (Reminder: The numbers can't be negative)")
                    break
    if x == 2:
        print("Looks like you want to calculate the drag force, in order to do so, I will need the air density, velocity, drag coefficient and the cross-sectional area.")
        for i in range(10000000000):
            p = float(input("Please enter the air density> "))
            v = float(input("Please enter the velocity of the rocket> "))
            d = float(input("Please enter the drag coefficient> "))
            A = float(input("Please enter the cross-sectional area> "))
            for i in range(10000000):
                if p > 0 and v > 0 and d > 0 and A > 0:
                    F = (1/2)*(p)*(v ** 2)*(d)*(A)
                    print(f"The drag force is {F} Newtons")
                    return
                else:
                    print("Your inputs are invalid, try again (Reminder: The numbers can't be negative)")
                    break
    
    return
        

def main():
    rockets()
    
if __name__ == "__main__":
    main()