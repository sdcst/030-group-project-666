import math
def VR(): 
    m = float(input("Please enter the mass of this aircraft:"))
    a = float(input("Please enter air density"))
    s = float(input("please enter the SA of wings"))
    c = float(input("please enter lift coefficient"))
    w = m * 9.8
    v = math.sqrt((2*w)/(a*s*c))
    VR = v / 0.51444
    VR = round(VR)
    print(f"The speed of rotate is {VR}")
def main():
    VR()

if __name__ == "__main__":
    main()  

