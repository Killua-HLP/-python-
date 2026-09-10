def is_valid(s):
    box = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in box:
            top = stack.pop() if stack else "*"
            if box[char] != top:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


print(is_valid("[{()}]"))
print(is_valid("()"))
print(is_valid("{(})[]"))
