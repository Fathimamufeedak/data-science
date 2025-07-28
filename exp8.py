source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

with open(source_file, 'r') as src:
    content = src.read()

with open(destination_file, 'w') as dest:
    dest.write(content)

print(f"File copied successfully from '{source_file}' to '{destination_file}'.")

