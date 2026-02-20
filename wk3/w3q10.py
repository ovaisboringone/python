n = int(input("Enter a number: "))

if n < 0:
    print("Invalid input")
else:
    a, b = 0, 1
    is_fib = False
    while a <= n:
        if a == n:
            is_fib = True
            break
        a, b = b, a + b

    if is_fib:
        print("Fibonacci number")
    else:
        print("Not a Fibonacci number")