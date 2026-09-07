def find_words(words, k):
    result = []

    for word in words:
        if len(word) > k:
            result.append(word)
    return result

print(find_words(["apple", "banana", "mango", "cherry", "lemon"], 5))