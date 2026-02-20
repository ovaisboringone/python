l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

surface_area = 2 * (l*b + b*h + h*l)
volume = l * b * h
print("Surface Area:", surface_area)
print("Volume:", volume)