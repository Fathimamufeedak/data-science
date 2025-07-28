n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
largest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num
print("The largest number in the list is:", largest)

