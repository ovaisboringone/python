def average_marks(marks):
    return sum(marks) / 5

marks = []
for i in range(5):
    m = float(input("Enter mark: "))
    marks.append(m)

print("Average =", average_marks(marks))
