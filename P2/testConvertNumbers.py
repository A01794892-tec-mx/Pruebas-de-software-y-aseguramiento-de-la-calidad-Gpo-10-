# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:06:26 2024

@author: AMD RYZEN 7
"""

import unittest
import subprocess
import os

class TestconvertNumbers(unittest.TestCase):
    """Test cases for convertNumbers.py"""

    def test_invalid_entry(self):
        """Checks if program handled bad entries and continued."""
        result = subprocess.run(['python', 'convertNumbers.py', 'TC4.txt'],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0)  # Exit code 0 despite file has invalid entries
        self.assertIn("Invalid entry", result.stdout)  # Cehck invalid entry message

    def test_conversion_file_1(self):
        """Checks some conversions for file 1."""
        result = subprocess.run(['python', 'convertNumbers.py', 'TC1.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('6980368|11010101000001100010000|6a8310', result_str)
        self.assertIn('5517055|10101000010111011111111|542eff', result_str)
        self.assertIn('1336159|101000110001101011111|14635f', result_str)
        self.assertIn('6750185|11001101111111111101001|66ffe9', result_str)
        self.assertIn('1771937|110110000100110100001|1b09a1', result_str)

    def test_conversion_file_2(self):
        """Checks some conversions for file 2."""
        result = subprocess.run(['python', 'convertNumbers.py', 'TC2.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('6359493|11000010000100111000101|6109c5', result_str)
        self.assertIn('1967646|111100000011000011110|1e061e', result_str)
        self.assertIn('6575052|11001000101001111001100|6453cc', result_str)
        self.assertIn('2323342|1000110111001110001110|23738e', result_str)
        self.assertIn('6735760|11001101100011110010000|66c790', result_str)
        self.assertIn('8895858|100001111011110101110010|87bd72', result_str)
        self.assertIn('4238091|10000001010101100001011|40ab0b', result_str)
        self.assertIn('7093069|11011000011101101001101|6c3b4d', result_str)

    def test_conversion_file_3(self):
        """Checks some conversions for file 3."""
        result = subprocess.run(['python', 'convertNumbers.py', 'TC3.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('33|100001|21',result_str)
        self.assertIn('-15|-1111|-f',result_str)
        self.assertIn('17|10001|11',result_str)
        self.assertIn('25|11001|19',result_str)
        self.assertIn('-25|-11001|-19',result_str)
        self.assertIn('-5|-101|-5',result_str)
        self.assertIn('33|100001|21',result_str)
        self.assertIn('-13|-1101|-d',result_str)

    def test_conversion_file_4(self):
        """Checks some conversions for file 3."""
        result = subprocess.run(['python', 'convertNumbers.py', 'TC4.txt'],
                                capture_output=True, text=True, check=False)
        result_str='|'.join(result.stdout.split())
        self.assertIn('29|11101|1d',result_str)
        self.assertIn('26|11010|1a',result_str)
        self.assertIn('-5|-101|-5',result_str)
        self.assertIn('-36|-100100|-24',result_str)
        self.assertIn('12|1100|c',result_str)
        self.assertIn('45|101101|2d',result_str)
        self.assertIn('-50|-110010|-32',result_str)
        self.assertIn('0|0|0',result_str)
        self.assertIn('-6|-110|-6',result_str)

    def test_time_elapsed(self):
        """Checks if time elapsed is printed on console."""
        result = subprocess.run(['python', 'convertNumbers.py', 'TC4.txt'],
                                capture_output=True, text=True, check=False)
        self.assertIn('Time Elapsed:',result.stdout)

    def test_time_in_file(self):
        """verifies if Time elapsed is included on the results file and if file is generated"""
        expected= "Time Elapsed:"
        file_path = "ConversionResults.txt"

        self.assertTrue(os.path.exists(file_path))

        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        self.assertIn(expected, file_content)


if __name__ == '__main__':
    unittest.main()
