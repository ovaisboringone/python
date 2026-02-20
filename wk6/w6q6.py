import math
print("Enter sides of triangle: ")
a = float(input("Enter 1st side : "))
b = float(input("Enter 2nd side : "))
c = float(input("Enter 3rd side : "))
if (a > 0 and b > 0 and c > 0):
    if (a+b > c and b+c > a and a+c > b):
        if (a == b or b == c or a==c):
            print("Isosceles Triangle")
        elif (a == b and b == c):
            print("Equilateral Triangle")
        else:
            print("Scalene Triangle")

        s = (a+b+c)/2

        area = math.sqrt(s*(s-a)*(s-b)*(s-c))

        print("Area is: ", area)
    else:
        print("These sides cant form a triangle")
else:
    print("Invalid length")
