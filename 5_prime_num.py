num = int(input("Enter the number: "))

is_prime = num >= 2

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")