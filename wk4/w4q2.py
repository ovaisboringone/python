import math

def sphere_volume(radius):
    if radius < 0:
        return "Invalid radius"
    return round((4/3) * math.pi * radius**3, 2)

radius = float(input("Enter radius: "))
print("Volume =", sphere_volume(radius))
