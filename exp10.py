# Get file names and words from the user
input_file = input("Enter the input filename: ")
output_file = input("Enter the output filename: ")
search_word = input("Enter the word to search for: ")
replace_word = input("Enter the word to replace it with: ")

try:
    # Read the entire content of the input file
    with open(input_file, 'r') as infile:
        content = infile.read()

    # Replace the word
    new_content = content.replace(search_word, replace_word)

    # Write the new content to the output file
    with open(output_file, 'w') as outfile:
        outfile.write(new_content)

    print(f"'{search_word}' has been replaced with '{replace_word}' in '{output_file}'.")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print("An error occurred:", e)

