# Read a text file in the same folder
file_name = "sample.txt" 
 # File name relative to the script
import os
print("Current working directory:", os.getcwd())


try:
    with open(file_name, 'r') as file:
        print("Reading file content:")
        for line in file:
            print(line.strip())  # .strip() removes newline and extra spaces
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found in the folder.")
except Exception as e:
    print(f"An error occurred: {e}")
  