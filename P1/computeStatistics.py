# -*- coding: utf-8 -*-
"""
computeStatistics.py - A program that performs descriptive statistics on a set
of numerical data provided in a text file. The program calculates and prints
the mean, median, mode, standard deviation, and variance of the data. Results are
displayed on the console and saved in a file named StatisticsResults.txt.
The program can handle large datasets and includes mechanisms to skip invalid
entries, ensuring uninterrupted execution. The execution time for computation
and file processing is reported at the end of the program.
Usage: python computeStatistics.py fileWithData.txt
PEP 8 compliant.
"""

import sys
import time

if len(sys.argv) != 2:
    print("Missing data file.")
    sys.exit(1)

INPUT_FILE_PATH = sys.argv[1]

try:
    with open(INPUT_FILE_PATH, 'r',encoding='utf-8') as file:
        data = []
        for line in file:
            try:
                value = float(line.strip())
                data.append(value)
            except ValueError:
                print(f"Invalid entry '{line.strip()}' in '{INPUT_FILE_PATH}'. Skipping.")

except FileNotFoundError:
    print(f"Error: File '{INPUT_FILE_PATH}' not found.")
    sys.exit(1)

if not data:
    print("Error: No valid data in the file.")
    sys.exit(1)

start_time = time.time()

# Calculate mean, median, standard deviation, and variance
mean = sum(data) / len(data)
sorted_data = sorted(data)
N = len(data)
median = (sorted_data[N // 2] + sorted_data[(N - 1) // 2]) / 2
squared_diff = [(x - mean) ** 2 for x in data]
variance = sum(squared_diff) / N
std_dev = variance ** 0.5


# Calculate mode
freqs = {}
for num in data:
    freqs[num] = freqs.get(num, 0) + 1

mode = max(freqs, key=freqs.get)


end_time = time.time()
elapsed_time = end_time - start_time

# Print statistics
print("\n--------------------------------------")
print("Statistics:\n")
print(f"Count: {N}")
print(f"Mean: {mean: .7f}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev: .7f}")
print(f"Variance: {variance: .7f}")
print(f"Time Elapsed: {elapsed_time:.6f} seconds")

# Write results to file
with open("StatisticsResults.txt", 'w', encoding='utf-8') as result_file:
    result_file.write("Statistics:\n")
    result_file.write(f"Count: {N}\n")
    result_file.write(f"Mean:{mean: .7f}\n")
    result_file.write(f"Median: {median}\n")
    result_file.write(f"Mode: {mode}\n")
    result_file.write(f"Standard Deviation: {std_dev: .7f}\n")
    result_file.write(f"Variance: {variance: .7f}\n")
    result_file.write(f"Time Elapsed: {elapsed_time:.6f} seconds\n")
