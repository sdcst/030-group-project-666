def Ar(tt, ct, crt, dt, lt,tr, clr, crr, dr, lr):
    tf = tr * tt
    cf = clr * ct
    crf = crr * crt
    df = dr * dt
    lf = lr * lt
    totalf = tf + cf + crf + df + lf
    tft = tt + ct + crt + dt + lt
    ar = totalf/ tft

    return ar

def main():
    print("A330 fuel consumption calculator")
    while True:
        try:
            tt= float(input("Please enter departure time (hours):"))
            ct = float(input("Please enter climb time (hours):"))
            crt = float(input("Please enter cruise time (hours):"))
            dt = float(input("Please enter time of descent in hours:"))
            lt = float(input("Please enter landing time in hours:"))
            tr = float(input("Please enter the fuel consumption rate during takeoff (kg/hour):"))
            clr = float(input("Please enter the fuel consumption rate during the climb phase (kg/hour):"))
            crr = float(input("Please enter the fuel consumption rate during cruise phase (kg/hour):"))
            dr = float(input("Please enter the fuel consumption rate during the descent phase (kg/hour):"))
            lr = float(input("Please enter the fuel consumption rate during the landing phase (kg/hour):"))
            break
        except ValueError:
            print("Invalid input, please enter a number.")
    fcr =Ar(
        tt, ct, crt, dt, lt,
        tr, clr, crr, dr, lr
    )
    print("The average fuel consumption rate of the A330 is:", fcr, "kg/hour")

if __name__ == "__main__":
    main()