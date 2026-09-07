my_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
unique_value = set()

for i in my_dict.values():
    unique_value.add(i)

unique = list(unique_value)

print(unique)