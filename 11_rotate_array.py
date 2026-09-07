def left_roate(num, k):
    n = len(num)
    if n == 0:
        return num
    k = k % n
    return num[k:] + num[:k]

def right_roate(num, k):
    n = len(num)
    if n == 0:
        return num
    k = k % n
    return num[-k:] + num[:-k]

print(left_roate([1,2,3,4,5], 2))
print(right_roate([1,2,3,4,5], 2))