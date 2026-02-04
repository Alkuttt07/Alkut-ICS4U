
x= float(input("What is the length? "))
y= float(input("What is the width? "))
z= float(input("What is the height? "))
n= int(input("""Please share the number what you need?
1.surface area
2.volume
"""))
if n==1:
    print(f"The surface area is {2*(x*y+x*z+y*z)}.",end='')
elif n==2:
    print(f"The volume is {x*y*z}." ,end='')
else:
    print("Your selection is invalid.")