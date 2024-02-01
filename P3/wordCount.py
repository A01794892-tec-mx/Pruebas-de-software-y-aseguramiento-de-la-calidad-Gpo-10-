# -*- coding: utf-8 -*-
"""
wordCount.py - A program that reads a text file, identifies distinct words,
and calculates the frequency of each word. The results are printed to the console
and saved in a file named WordCountResults.txt.
The program handles invalid data in the file, displays errors in the console,
and includes the time elapsed for the execution.
Usage: python wordCount.py fileWithData.txt
PEP 8 compliant.
"""

import sys
import time

if len(sys.argv) != 2:
    print("Missing data file.")
    sys.exit(1)

INPUT_FILE_PATH = sys.argv[1]

try:
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as file:
        words_count = {}
        TOTAL_WORDS = 0
        for line in file:
            words = line.split()
            TOTAL_WORDS += len(words)
            for word in words:
                word = word.lower()
                if word in words_count:
                    words_count[word] += 1
                else:
                    words_count[word] = 1

except FileNotFoundError:
    print(f"Error: File '{INPUT_FILE_PATH}' not found.")
    sys.exit(1)


start_time = time.time()


sorted_words_count = sorted(words_count.items(), key=lambda x: x[1], reverse=True)

# Print results to console
print("Word Count Results:")

print('Word\tFrequency')
for word, count in sorted_words_count:
    print(f"{word}\t{count}")

print(f"\nGrand Total: {TOTAL_WORDS}")

# Write results to file
with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
    result_file.write("Word Count Results:\n")
    result_file.write('Word\tFrequency\n')
    for word, count in sorted_words_count:
        result_file.write(f"{word}\t{count}\n")
    result_file.write(f"\nGrand Total: {TOTAL_WORDS}\n")

end_time = time.time()
elapsed_time = end_time - start_time

# Print time elapsed
print(f"\nTime Elapsed: {elapsed_time:.6f} seconds")

# Write time elapsed to file
with open("WordCountResults.txt", 'a', encoding='utf-8') as result_file:
    result_file.write(f"Time Elapsed: {elapsed_time:.6f} seconds\n")
