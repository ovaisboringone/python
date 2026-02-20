def sum_numbers(*args):
    return sum(args)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum =", sum_numbers(*numbers))
