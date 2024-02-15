# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:53:08 2024

@author: AMD RYZEN 7
"""

import unittest
from unittest.mock import patch
from hotel_reservation_system import HotelManager, CustomerManager, FileManager


class TestCustomerManager(unittest.TestCase):
    """Test cases for the CustomerManager class."""

    @patch('builtins.print')
    def test_load_from_file_error_displayed(self, mock_print):
        """Test if an error is displayed when loading from a non-existent file
        and continues execution"""
        filename = 'nonexistent_file.json'
        result = FileManager.load_from_file(filename)

        mock_print.assert_called_once_with(f'Error loading File: {filename}')
        self.assertEqual(result, {})

    def test_create_customer(self):
        """Test creating a new customer."""
        customer = CustomerManager.create_customer(1, 'Cust Cr',
                                                   'cust_cr@example.com')
        self.assertIsNotNone(customer)

    def test_delete_customer(self):
        """Test deleting a customer."""
        CustomerManager.create_customer(2, 'Cust De', 'cust_de@example.com')
        CustomerManager.delete_customer(2)
        self.assertIsNone(CustomerManager.display_customer_info(2))

    def test_display_customer_info(self):
        """Test displaying customer information."""
        customer = CustomerManager.create_customer(3, 'Cust Dis',
                                                   'cust_dis@example.com')
        retrieved_customer = CustomerManager.display_customer_info(3)

        self.assertEqual(customer.customer_id,
                         retrieved_customer['customer_id'])
        self.assertEqual(customer.name, retrieved_customer['name'])
        self.assertEqual(customer.email, retrieved_customer['email'])

    def test_modify_customer_info(self):
        """Test modifying customer information."""
        CustomerManager.create_customer(5, 'Cust Mod', 'cust_mod@example.com')
        CustomerManager.modify_customer_info(5, 'Modify', 'modify@example.com')
        modified_customer = CustomerManager.display_customer_info(5)
        self.assertEqual(modified_customer['name'], 'Modify')
        self.assertEqual(modified_customer['email'], 'modify@example.com')


class TestHotelManager(unittest.TestCase):
    """Test cases for the HotelManager class."""

    def test_create_hotel(self):
        """Test creating a new hotel."""
        hotel = HotelManager.create_hotel(1, 'Hotel Create', 10)
        self.assertIsNotNone(hotel)

    def test_delete_hotel(self):
        """Test deleting a hotel."""
        HotelManager.create_hotel(2, 'Hotel Delete', 10)
        HotelManager.delete_hotel(2)
        self.assertIsNone(HotelManager.display_hotel_info(2))

    def test_display_hotel_info(self):
        """Test displaying hotel information."""
        hotel = HotelManager.create_hotel(3, 'Hotel Display', 10)
        retrieved_hotel = HotelManager.display_hotel_info(3)

        self.assertEqual(hotel.hotel_id, retrieved_hotel['hotel_id'])
        self.assertEqual(hotel.name, retrieved_hotel['name'])
        self.assertEqual(hotel.rooms_avlbl, retrieved_hotel['rooms_avlbl'])

    def test_modify_hotel_info(self):
        """Test modifying hotel information."""
        HotelManager.create_hotel(4, 'Hotel to modify', 10)
        HotelManager.modify_hotel_info(4, 'Modified Hotel', 5)
        modified_hotel = HotelManager.display_hotel_info(4)
        self.assertEqual(modified_hotel['name'], 'Modified Hotel')
        self.assertEqual(modified_hotel['rooms_avlbl'], 5)

    def test_reserve_room(self):
        """Test reserving a room in a hotel."""
        customer = CustomerManager.create_customer(6, 'Cust Reserve',
                                                   'c_reserve@example.com')
        hotel = HotelManager.create_hotel(5, 'Hotel Reserve', 10)
        reservation = HotelManager.reserve_room(customer, hotel)
        self.assertIsNotNone(reservation)

    def test_cancel_reservation(self):
        """Test canceling a reservation."""
        customer = CustomerManager.create_customer(7, 'Cust Cancell',
                                                   'c_cancell@example.com')
        hotel = HotelManager.create_hotel(6, 'Hotel cancell', 10)
        reservation = HotelManager.reserve_room(customer, hotel)
        success = HotelManager.cancel_reservation(reservation.reservation_id)
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main()
