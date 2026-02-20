def rectangle_perimeter(length, width):
    return 2 * (length + width)

length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Perimeter =", rectangle_perimeter(length, width))
