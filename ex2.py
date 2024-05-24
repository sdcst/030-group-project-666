
d=float(input("The distance(km):"))
if t<0:
    print("Something Wrong!")
elif d<0:
    print("Something Wrong!")
else:
 v=d/t
 v1=round(v,1)
 print(f"The speed is {v1} km/h")