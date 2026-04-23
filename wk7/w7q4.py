def find_signal_sync(a, b):
    if b==0:
        return a
    else:
        return find_signal_sync(b,a%b)

a=int(input("Enter cycle time a: "))
b=int(input("Enter cycle time b: "))
print(find_signal_sync(a,b))
