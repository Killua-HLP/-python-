terms = int(input("Enter the number: "))

n1, n2 = 0, 1
count = 0

if terms <= 0:
    print("pls enter the positive number.")
elif terms == 1:
    print("Fibonacci sequence upto", terms, ":")
    print(n1)
else:
    print("Fibonacci Sequence: ")
    while count < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1