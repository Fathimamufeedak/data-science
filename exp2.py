n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)

