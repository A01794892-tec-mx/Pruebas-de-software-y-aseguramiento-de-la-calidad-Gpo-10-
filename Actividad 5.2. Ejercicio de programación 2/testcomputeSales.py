# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:06:26 2024

@author: AMD RYZEN 7
"""

import unittest
import subprocess
import os


class testComputeSales(unittest.TestCase):
    """Test cases for computeSales.py"""

    def test_sales_total_file_1(self):
        """
        Checks Results for TC1
        """

        result = subprocess.run(['python', 'computeSales.py',
                                 "TC1.ProductList.json", "TC1.Sales.json"],
                                capture_output=True, text=True, check=False)

        self.assertIn('2481.86', result.stdout)

    def test_sales_total_file_2(self):
        """
        Checks Results for TC2
        """

        result = subprocess.run(['python', 'computeSales.py',
                                 "TC1.ProductList.json", "TC2.Sales.json"],
                                capture_output=True, text=True, check=False)

        self.assertIn('166568.23', result.stdout)

    def test_sales_total_file_3(self):
        """
        Checks Results for TC3
        """

        result = subprocess.run(['python', 'computeSales.py',
                                 "TC1.ProductList.json", "TC3.Sales.json"],
                                capture_output=True, text=True, check=False)

        self.assertIn('165235.37', result.stdout)

    def test_invalid_entry(self):
        """Checks if program handled bad entries and continued."""
        result = subprocess.run(['python', 'computeSales.py',
                                 "TC1.ProductList.json", "TC3.Sales.json"],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0)  # Exit code should be 0

        # Check if invalid message was displayed
        self.assertIn("Warning: Product", result.stdout)

    def test_time_elapsed(self):
        """Checks if Time elapsed is printed on console."""

        result = subprocess.run(['python', 'computeSales.py',
                                 "TC1.ProductList.json", "TC3.Sales.json"],
                                capture_output=True, text=True, check=False)
        self.assertIn('Time elapsed:', result.stdout)

    def test_time_in_file(self):
        """Verifies if Time elapsed is included on the results file
        and if file is generated"""

        expected = "Time elapsed:"
        file_path = "SalesResults.txt"

        self.assertTrue(os.path.exists(file_path))

        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        self.assertIn(expected, file_content)


if __name__ == '__main__':
    unittest.main()
