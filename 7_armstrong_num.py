num = int(input("Enter the number: "))

num_str = str(num)
digit_num = len(num_str)

armstrong_sum = sum(int(digit) ** digit_num for digit in num_str)

if num == armstrong_sum:
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number.")
