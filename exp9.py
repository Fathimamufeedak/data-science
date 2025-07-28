# Get filenames from user
input_file = input("Enter the input filename: ")
output_file = input("Enter the output filename: ")

try:
    # Read the contents of the input file
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Capitalize each word using str.upper()
    capitalized_lines = []
    for line in lines:
        words = line.split()
        capitalized_words = [word.upper() for word in words]
        capitalized_line = ' '.join(capitalized_words)
        capitalized_lines.append(capitalized_line)

    # Write the capitalized content to the output file
    with open(output_file, 'w') as outfile:
        for line in capitalized_lines:
            outfile.write(line + '\n')

    print(f"Capitalized content written to '{output_file}' successfully.")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print("An error occurred:", e)

