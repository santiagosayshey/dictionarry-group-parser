import re

# Prompt the user to enter the file path
file_path = input("Enter the file path: ")

try:
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Use regular expression to find numbers greater than or equal to 25
            numbers = re.findall(r'\b\d{2,}\b', line)
            
            # Check if any numbers are found
            if numbers:
                # Convert the numbers to integers
                numbers = [int(num) for num in numbers]
                
                # Check if any number is greater than or equal to 25
                if any(num >= 25 for num in numbers):
                    # Print the line containing the number
                    print(line.strip())

except FileNotFoundError:
    print("File not found. Please provide a valid file path.")

except IOError:
    print("An error occurred while reading the file.")