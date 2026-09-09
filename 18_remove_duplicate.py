def remove_duplicate():
    n = int(input())
    if n == 0:
        print(0)
        return
    numbers = input().split()
    slow = 0

    for fast in range(1, n):
        if numbers[fast] != numbers[slow]:
            slow += 1
            numbers[slow] = numbers[fast]
    k = slow + 1
    print(k)
    print("".join(numbers[:k]))

if __name__ == "__main__":
    remove_duplicate()

#Another way to remove duplicate numbers

def remove_duplicates(numbers):
    slow = 0
    fast = 1
    while fast < len(numbers):
        if numbers[fast] != numbers[slow]:
            slow += 1
            numbers[slow] = numbers[fast]
            fast += 1

        fast += 1
    return numbers


print(remove_duplicates([1, 1, 2, 2, 3, 4, 4]))