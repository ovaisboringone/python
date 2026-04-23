Dept_A = {}
Dept_B = {}
Dept_C = {}

n1 = int(input("Enter number of entries for Dept_A: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    Dept_A[key] = value

n2 = int(input("Enter number of entries for Dept_B: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    Dept_B[key] = value

n3 = int(input("Enter number of entries for Dept_C: "))
for i in range(n3):
    key = input("Enter key: ")
    value = input("Enter value: ")
    Dept_C[key] = value


Patient_Profile = {}

# Copy Dept_A
for k in Dept_A:
    Patient_Profile[k] = Dept_A[k]

# Copy Dept_B
for k in Dept_B:
    Patient_Profile[k] = Dept_B[k]

# Copy Dept_C
for k in Dept_C:
    Patient_Profile[k] = Dept_C[k]

print("Patient Profile:", Patient_Profile)