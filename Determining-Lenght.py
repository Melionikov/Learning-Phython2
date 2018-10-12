import math

int(input(Enter first x value: ))
#x1 = 20

int(input(Enter first y value: ))
#y1 = 20

int(input(Enter first z value: ))
#z1 = 20

int(input(Enter second x value: ))
#x2 = 10

int(input(Enter second y value: ))
#y2 = 10

int(input(Enter second z value: ))
#z2 = 10

a = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))

if a == 0:
    print("Your points are same.")
else:
    print("Distance between two points are: ",end="")
    print(a)
