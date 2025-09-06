
def write_big_file(filename):
    try:
        with open(filename, 'w') as f:
            for i in range(1, 100001): 
                f.write(f"This is line number {i}\n")
        print("File written successfully.")
    except Exception as e:
        print(f"Error writing file: {e}")

# Step 2: Generator Function to Read File Line by Line
def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error reading file: {e}")

# Step 3: Driver Code
file_path = "big_file.txt"

# Write the file
write_big_file(file_path)

# Read the file using generator
print("Reading the file line by line:\n")
for line in read_file_line_by_line(file_path):
    print(line)
