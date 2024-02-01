# -*- coding: utf-8 -*-
"""
convertNumbers.py - A program that reads a text file containing numerical data,
converts each number to binary and hexadecimal bases, and prints the results to
the console. The converted values, along with the original numbers, are saved
in a file named ConversionResults.txt. The program handles invalid data in the
file and displays errors in the console, ensuring the execution continues.
Usage: python convertNumbers.py fileWithData.txt
PEP 8 compliant.
"""

import sys
import time

if len(sys.argv) != 2:
    print("Missing Data File")
    sys.exit(1)

INPUT_FILE_PATH = sys.argv[1]

try:
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as file:
        numbers = []
        for line in file:
            try:
                value = float(line.strip())
                numbers.append(value)
            except ValueError:
                print(f"Invalid entry '{line.strip()}' in '{INPUT_FILE_PATH}'. Skipping.")

except FileNotFoundError:
    print(f"Error: File '{INPUT_FILE_PATH}' not found.")
    sys.exit(1)

if not numbers:
    print("Error: No valid numbers in the file.")
    sys.exit(1)

start_time = time.time()

binary_results = []
hex_results = []

for num in numbers:
    # Convert to binary and hexadecimal
    binary_result = f"{int(num):b}"
    hex_result = f"{int(num):x}"

    binary_results.append(binary_result)
    hex_results.append(hex_result)

end_time = time.time()
elapsed_time = end_time - start_time

# Print results
print("Conversion Results:")

i = 1

print('Index\tNumber\tBinary\tHex')
for num, binary, hex_value in zip(numbers, binary_results, hex_results):
    print(f"{i}\t{int(num)}\t{binary}\t{hex_value}")
    i += 1

# Write results to file
with open("ConversionResults.txt", 'w', encoding='utf-8') as result_file:
    result_file.write("Conversion Results:\n")
    result_file.write('Index\tNumber\tBinary\tHex\n')
    i = 1
    for num, binary, hex_value in zip(numbers, binary_results, hex_results):
        result_file.write(f"{i}\t{int(num)}\t{binary}\t{hex_value}\n")
        i += 1

# Print time elapsed
print(f"Time Elapsed: {elapsed_time:.6f} seconds")

# Write time elapsed to file
with open("ConversionResults.txt", 'a', encoding='utf-8') as result_file:
    result_file.write(f"Time Elapsed: {elapsed_time:.6f} seconds\n")
