# Function to read a dictionary from user input
def get_dict_input(n):
    user_dict = {}
    for i in range(n):
        key = input(f"Enter key {i + 1}: ")
        value = input(f"Enter value for '{key}': ")
        user_dict[key] = value
    return user_dict

# Get user input for two dictionaries
n1 = int(input("How many items in Dictionary 1? "))
dict1 = get_dict_input(n1)

n2 = int(input("How many items in Dictionary 2? "))
dict2 = get_dict_input(n2)

print("\nDictionary 1:", dict1)
print("Dictionary 2:", dict2)

# 1️⃣ Using update()
merged_update = dict1.copy()
merged_update.update(dict2)
print("\nMerged using update():", merged_update)

# 2️⃣ Using ** unpacking
merged_unpacking = {**dict1, **dict2}
print("Merged using ** unpacking:", merged_unpacking)

# 3️⃣ Using | operator (Python 3.9+)
merged_pipe = dict1 | dict2
print("Merged using | operator:", merged_pipe)

