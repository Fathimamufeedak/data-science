def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))

list1_input = input("Enter the first list of items (separated by space): ")
list2_input = input("Enter the second list of items (separated by space): ")

list1 = list1_input.split()
list2 = list2_input.split()

result = have_common_member(list1, list2)
print("Do the lists have at least one common member?", result)

