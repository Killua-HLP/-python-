def find_largest_num(numbers):
    if not numbers:
        return None
    largest_num = numbers[0]
    second_largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num >= largest_num:
            second_largest = largest_num
            largest_num = num
        elif num > second_largest and num < largest_num:
            largest_num = num
        elif num < smallest:
            smallest = num
    return largest_num, second_largest, smallest

print("Largest, Sec_largest and Smallest number is:",find_largest_num([3,5,55,79,33,25]))