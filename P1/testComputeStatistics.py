# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:06:26 2024

@author: AMD RYZEN 7
"""

import unittest
import subprocess

class TestComputeStatistics(unittest.TestCase):
    """
    Test cases for computeStatistics.py
    """
    def test_invalid_entry(self):
        """Checks if program handled bad entries and continued."""
        result = subprocess.run(['python', 'computeStatistics.py',
                                 'TC1.txt'], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode,0) # Exit code should be 0 for success
        self.assertIn("Invalid entry", result.stdout) # Cehck if invalid message was displayed

    def test_statistics_file_2(self):
        """Checks statistics for file 2."""
        result = subprocess.run(['python', 'computeStatistics.py',
                                 'TC2.txt'], capture_output=True, text=True, check=False)
        self.assertIn('Count: 1977', result.stdout)
        self.assertIn('Mean:  250.7840162', result.stdout)
        self.assertIn('Median: 247.0', result.stdout)
        self.assertIn('Mode: 230.0', result.stdout)
        self.assertIn('Standard Deviation:  144.1713187', result.stdout)
        self.assertIn('Variance:  20785.3691325', result.stdout)

    def test_statistics_file_3(self):
        """Checks statistics for file 3."""
        result = subprocess.run(['python', 'computeStatistics.py',
                                 'TC3.txt'], capture_output=True, text=True, check=False)
        self.assertIn('Count: 12624', result.stdout)
        self.assertIn('Mean:  249.7762199', result.stdout)
        self.assertIn('Median: 249.0', result.stdout)
        self.assertIn('Mode: 94.0', result.stdout)
        self.assertIn('Standard Deviation:  145.3178498', result.stdout)
        self.assertIn('Variance:  21117.2774732', result.stdout)

    def test_statistics_file_4(self):
        """Checks statistics for file 4."""
        result = subprocess.run(['python', 'computeStatistics.py',
                                 'TC4.txt'], capture_output=True, text=True, check=False)
        self.assertIn('Count: 12624', result.stdout)
        self.assertIn('Mean:  149.0026735', result.stdout)
        self.assertIn('Median: 147.75', result.stdout)
        self.assertIn('Mode: 123.75', result.stdout)
        self.assertIn('Standard Deviation:  130.4144196', result.stdout)
        self.assertIn('Variance:  17007.9208430', result.stdout)


    def test_statistics_file_5(self):
        """Checks statistics for file 5."""
        result = subprocess.run(['python', 'computeStatistics.py',
                                 'TC5.txt'], capture_output=True, text=True, check=False)
        self.assertIn('Count: 307', result.stdout)
        self.assertIn('Mean:  241.4951140', result.stdout)
        self.assertIn('Median: 241.0', result.stdout)
        self.assertIn('Mode: 393.0', result.stdout)
        self.assertIn('Standard Deviation:  145.4648479', result.stdout)
        self.assertIn('Variance:  21160.0219631', result.stdout)


    def test_statistics_file_6(self):
        """Checks statistics for file 6."""
        result = subprocess.run(['python', 'computeStatistics.py',
                                 'TC6.txt'], capture_output=True, text=True, check=False)
        self.assertIn('Count: 3000', result.stdout)
        self.assertIn('Mean:  187906599279774728192.0000000', result.stdout)
        self.assertIn('Median: 1.88008049965543e+20', result.stdout)
        self.assertIn('Mode: 1.27620004531949e+20', result.stdout)
        self.assertIn('Standard Deviation:  107382050173809999872.0000000', result.stdout)
        self.assertIn('Variance:  11530904699530646862954721780958962384896.0000000', result.stdout)


    def test_statistics_file_7(self):
        """Checks statistics for file 7."""
        result = subprocess.run(['python', 'computeStatistics.py',
                                 'TC7.txt'], capture_output=True, text=True, check=False)
        self.assertIn('Count: 12767', result.stdout)
        self.assertIn('Mean:  247467395499714904064.0000000', result.stdout)
        self.assertIn('Median: 2.4664097307429e+20', result.stdout)
        self.assertIn('Mode: 1.57638329490099e+20', result.stdout)
        self.assertIn('Standard Deviation:  144605647009847033856.0000000', result.stdout)
        self.assertIn('Variance:  20910793147136483762414542324695312629760.0000000', result.stdout)



if __name__ == '__main__':
    unittest.main()
