import math

def largest(a, b, c):
    return max(a, b, c)

def volume_cylinder(r, h):
    return math.pi * r * r * h

def volume_cube(a):
    return a ** 3

def volume_box(l, w, h):
    return l * w * h

def area_rectangle(l, w):
    return l * w

def circumference_circle(r):
    return 2 * math.pi * r

def swap(a, b):
    return b, a

def distance(p1, p2):
    return math.dist(p1, p2)

print("""
1. Largest of three numbers
2. Volume (Cylinder / Cube / Box)
3. Area of Rectangle
4. Circumference of Circle
5. Swap two numbers
6. Distance between two points
""")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        print("Largest =", largest(a, b, c))

    case 2:
        shape = input("Choose shape (cylinder/cube/box): ").lower()
        if shape == "cylinder":
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            print("Volume =", volume_cylinder(r, h))
        elif shape == "cube":
            a = float(input("Enter side: "))
            print("Volume =", volume_cube(a))
        elif shape == "box":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            print("Volume =", volume_box(l, w, h))
        else:
            print("Invalid shape")

    case 3:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area =", area_rectangle(l, w))

    case 4:
        r = float(input("Enter radius: "))
        print("Circumference =", circumference_circle(r))

    case 5:
        x = int(input("Enter first value: "))
        y = int(input("Enter second value: "))
        x, y = swap(x, y)
        print("After swap:", x, y)

    case 6:
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        print("Distance =", distance((x1, y1), (x2, y2)))

    case _:
        print("Invalid choice")
