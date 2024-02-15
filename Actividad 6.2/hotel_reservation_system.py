# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:51:31 2024

@author: AMD RYZEN 7
"""

import json
from dataclasses import dataclass


@dataclass
class Hotel:
    """Class representing a hotel."""
    def __init__(self, hotel_id, name, rooms_avlbl):
        self.hotel_id = hotel_id
        self.name = name
        self.rooms_avlbl = rooms_avlbl


@dataclass
class Customer:
    """Class representing a customer."""
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email


@dataclass
class Reservation:
    """Class representing a reservation."""
    def __init__(self, reservation_id, customer, hotel):
        self.reservation_id = reservation_id
        self.customer = customer.customer_id
        self.hotel = hotel.hotel_id


class FileManager:
    """Class for file operations."""
    @staticmethod
    def load_from_file(filename):
        """
        Load data from a JSON file.

        Args:
            filename (str): The path to the JSON file.

        Returns:
            dict: Loaded data from the file.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            print(f'Error loading File: {filename}')
            # If the file doesn't exist or is empty, return an empty dictionary
            return {}

    @staticmethod
    def save_to_file(filename, data):
        """
        Save data to a JSON file.

        Args:
            filename (str): The path to the JSON file.
            data (dict): Data to be saved to the file.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"Error saving data to {filename}: {error}")


class HotelManager(FileManager):
    """Class for managing hotels."""
    FILE_HOTELS = 'hotels.json'
    FILE_RESERVS = 'reservations.json'

    @staticmethod
    def create_hotel(hotel_id, name, rooms_avlbl):
        """
        Create a new hotel and save it to the file.

        Args:
            hotel_id (int): The ID of the hotel.
            name (str): The name of the hotel.
            rooms_avlbl (int): The number of available rooms.

        Returns:
            Hotel: The created hotel object.
        """
        hotel = Hotel(hotel_id, name, rooms_avlbl)
        existing_data = HotelManager.load_from_file(HotelManager.FILE_HOTELS)
        existing_records = existing_data.get('hotels', [])
        existing_records.append(hotel.__dict__)
        existing_data['hotels'] = existing_records
        HotelManager.save_to_file(HotelManager.FILE_HOTELS, existing_data)
        return hotel

    @staticmethod
    def delete_hotel(hotel_id):
        """
        Delete a hotel by ID.

        Args:
            hotel_id (int): The ID of the hotel to be deleted.
        """
        hotels = HotelManager.load_from_file(HotelManager.FILE_HOTELS)
        existing_records = hotels.get('hotels', [])
        filtered_records = [record for record in existing_records
                            if record.get('hotel_id') != hotel_id]
        hotels['hotels'] = filtered_records
        HotelManager.save_to_file(HotelManager.FILE_HOTELS, hotels)

    @staticmethod
    def display_hotel_info(hotel_id):
        """
        Display information for a specific hotel.

        Args:
            hotel_id (int): The ID of the hotel.

        Returns:
            dict: Information about the hotel.
        """
        hotels = HotelManager.load_from_file(HotelManager.FILE_HOTELS)
        existing_records = hotels.get('hotels', [])
        return next((record for record in existing_records
                     if record.get('hotel_id') == hotel_id), None)

    @staticmethod
    def modify_hotel_info(hotel_id, new_name, new_rooms_avlbl):
        """
        Modify information for a specific hotel.

        Args:
            hotel_id (int): The ID of the hotel.
            new_name (str): The new name for the hotel.
            new_rooms_avlbl (int): The updated number of available rooms.
        """
        hotels = HotelManager.load_from_file(HotelManager.FILE_HOTELS)
        existing_records = hotels.get('hotels', [])
        for record in existing_records:
            if record.get('hotel_id') == hotel_id:
                record['name'] = new_name
                record['rooms_avlbl'] = new_rooms_avlbl
                break
        HotelManager.save_to_file(HotelManager.FILE_HOTELS, hotels)

    @staticmethod
    def reserve_room(customer, hotel):
        """
        Reserve a room in a hotel.

        Args:
            customer (Customer): The customer making the reservation.
            hotel (Hotel): The hotel for the reservation.

        Returns:
            Reservation: The reservation object.
        """
        if hotel.rooms_avlbl > 0:
            existing_data = HotelManager.load_from_file(
                HotelManager.FILE_RESERVS)
            existing_records = existing_data.get('reservations', [])
            reservation_id = len(existing_records) + 1
            reservation = Reservation(reservation_id, customer, hotel)
            existing_records.append(reservation.__dict__)
            existing_data['reservations'] = existing_records
            HotelManager.save_to_file(HotelManager.FILE_RESERVS,
                                      existing_data)
            hotel.rooms_avlbl -= 1
            HotelManager.modify_hotel_info(hotel.hotel_id, hotel.name,
                                           hotel.rooms_avlbl)

            return reservation

        return None

    @staticmethod
    def cancel_reservation(reservation_id):
        """
        Cancel a reservation and update available rooms.

        Args:
            reservation_id (int): The ID of the reservation to be canceled.

        Returns:
            bool: True if the reservation was successfully canceled,
            False otherwise.
        """
        record_deleted = False
        reservations = HotelManager.load_from_file(HotelManager.FILE_RESERVS)
        existing_records = reservations.get('reservations', [])
        hotels = HotelManager.load_from_file(
            HotelManager.FILE_HOTELS).get('hotels', [])
        filtered_records = []
        for reservation in existing_records:
            if reservation.get('reservation_id') == reservation_id:
                hotel_id = reservation.get('hotel_id')
                for hotel in hotels:
                    if hotel.get('hotel_id') == hotel_id:
                        hotel_rooms_avlbl = hotel.get('rooms_avlbl') + 1
                        hotel_name = hotel.get('name')
                        HotelManager.modify_hotel_info(hotel_id, hotel_name,
                                                       hotel_rooms_avlbl)
                record_deleted = True

            else:
                filtered_records.append(reservation)

        reservations['reservations'] = filtered_records
        HotelManager.save_to_file(HotelManager.FILE_RESERVS, reservations)
        return record_deleted


class CustomerManager(FileManager):
    """Class for managing customers."""
    FILE_CUSTOMER = 'customers.json'

    @staticmethod
    def create_customer(customer_id, name, email):
        """
        Create a new customer and save it to the file.

        Args:
            customer_id (int): The ID of the customer.
            name (str): The name of the customer.
            email (str): The email of the customer.

        Returns:
            Customer: The created customer object.
        """
        customer = Customer(customer_id, name, email)
        existing_data = CustomerManager.load_from_file(
            CustomerManager.FILE_CUSTOMER)
        existing_records = existing_data.get('customers', [])
        existing_records.append(customer.__dict__)
        existing_data['customers'] = existing_records
        CustomerManager.save_to_file(CustomerManager.FILE_CUSTOMER,
                                     existing_data)
        return customer

    @staticmethod
    def delete_customer(customer_id):
        """
        Delete a customer by ID.

        Args:
            customer_id (int): The ID of the customer to be deleted.
        """
        customers = CustomerManager.load_from_file(
            CustomerManager.FILE_CUSTOMER)
        existing_records = customers.get('customers', [])
        filtered_records = [record for record in existing_records
                            if record.get('customer_id') != customer_id]
        customers['customers'] = filtered_records
        CustomerManager.save_to_file(CustomerManager.FILE_CUSTOMER, customers)

    @staticmethod
    def display_customer_info(customer_id):
        """
        Display information for a specific customer.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            dict: Information about the customer.
        """
        customers = CustomerManager.load_from_file(
            CustomerManager.FILE_CUSTOMER)
        existing_records = customers.get('customers', [])
        return next((record for record in existing_records
                     if record.get('customer_id') == customer_id), None)

    @staticmethod
    def modify_customer_info(customer_id, new_name, new_email):
        """
        Modify information for a specific customer.

        Args:
            customer_id (int): The ID of the customer.
            new_name (str): The new name for the customer.
            new_email (str): The new email for the customer.
        """
        customers = CustomerManager.load_from_file(
            CustomerManager.FILE_CUSTOMER)
        existing_records = customers.get('customers', [])
        for record in existing_records:
            if record.get('customer_id') == customer_id:
                record['name'] = new_name
                record['email'] = new_email
                break
        CustomerManager.save_to_file(CustomerManager.FILE_CUSTOMER, customers)
