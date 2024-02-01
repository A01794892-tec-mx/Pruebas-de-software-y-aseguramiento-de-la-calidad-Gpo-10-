# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:06:26 2024

@author: AMD RYZEN 7
"""

import unittest
import subprocess
import os

class TestwordCount(unittest.TestCase):
    """Test cases for wordCount.py"""

    def test_word_count_file_1(self):
        """
        Checks first word count (most repeated as program orders by greater frequency)
        and grand total for TC1
        """

        result = subprocess.run(['python', 'wordCount.py', 'TC1.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('Word|Frequency|conservative|2', result_str)
        self.assertIn('Grand|Total:|100', result_str)

    def test_word_count_file_2(self):
        """Checks first word count (most repeated as program orders by greater frequency)
        and grand total for TC2"""

        result = subprocess.run(['python', 'wordCount.py', 'TC2.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('Word|Frequency|lease|4', result_str)
        self.assertIn('Grand|Total:|184', result_str)

    def test_word_count_file_3(self):
        """Checks first word count (most repeated as program orders by greater frequency)
        and grand total for TC3"""

        result = subprocess.run(['python', 'wordCount.py', 'TC3.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('Word|Frequency|notice|3', result_str)
        self.assertIn('Grand|Total:|500', result_str)

    def test_word_count_file_4(self):
        """Checks first word count (most repeated as program orders by greater frequency)
        and grand total for TC4"""

        result = subprocess.run(['python', 'wordCount.py', 'TC4.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('Word|Frequency|started|3', result_str)
        self.assertIn('Grand|Total:|1000', result_str)

    def test_word_count_file_5(self):
        """Checks first word count (most repeated as program orders by greater frequency)
        and grand total for TC5"""

        result = subprocess.run(['python', 'wordCount.py', 'TC5.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('Word|Frequency|wilderness|5', result_str)
        self.assertIn('Grand|Total:|5000', result_str)

    def test_time_elapsed(self):
        """Checks if Time elapsed is printed on console."""

        result = subprocess.run(['python', 'wordCount.py', 'TC4.txt'],
                                capture_output=True, text=True, check=False)
        self.assertIn('Time Elapsed:',result.stdout)


    def test_time_in_file(self):
        """verifies if Time elapsed is included on the results file and if file is generated"""

        expected= "Time Elapsed:"
        file_path = "WordCountResults.txt"

        self.assertTrue(os.path.exists(file_path))

        with open(file_path, 'r',encoding='utf-8') as file:
            file_content = file.read()

        self.assertIn(expected, file_content)


if __name__ == '__main__':
    unittest.main()
