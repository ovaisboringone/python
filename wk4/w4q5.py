def sum_of_digits(num):
    total = 0
    for digit in num:
        total += int(digit)
    return total

num = input("Enter a number: ")
print("Sum of digits =", sum_of_digits(num))
