import math
r=input("The radius of the ball:")
if float(r) < 0:
    print("Invalid input")
else:
    r = float(r)
    s= math.pi*4*r*r
    s1=round(s,2)
    print(f"The surface area is{s1}")
    v=(4/3)*math.pi*(r**3)
    v1=round(v,2)
    print(f"The volume is{v1}")