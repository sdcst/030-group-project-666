x=float(input("Enter the initial speed(m/s)"))
y=float(input("Enter the final speed(m/s)"))
a=float(input("Enter the initial time(s)"))
b=float(input("Enter the final time(s)"))
if b<a:
    print("Something Wrong!")
else:
 v=y-x
 t=b-a
 ac=v/t
 ac1=round(ac,2)
 print(f"The acceleration is {ac1} m/s/s")
