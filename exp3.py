n = int(input("Enter number of key-value pairs: "))
tuple_data = []

for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value {i + 1}: ")
    tuple_data.append((key, value))
tuple_data = tuple(tuple_data)
dict_data = {}

for key, value in tuple_data:
    dict_data[key] = value

print("Dictionary:", dict_data)

