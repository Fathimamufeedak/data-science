# Get filename from the user
filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)

    print(f"Number of lines in '{filename}': {line_count}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print("An error occurred:", e)

