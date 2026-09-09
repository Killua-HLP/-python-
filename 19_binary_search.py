def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last ) // 2
        if list[midpoint] == target:
            return target
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1

print(binary_search([4,5,2,3,1,7,8],7))


