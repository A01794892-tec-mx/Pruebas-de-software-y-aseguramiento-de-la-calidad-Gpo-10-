# -*- coding: utf-8 -*-
"""
computeSales.py - Computes the total cost for all sales based on
information from a JSON price catalogue and a JSON sales record.
The results are printed to the console and saved on SalesResults.txt
It handles invalid data in the files, displaying errors in console,
and includes the time elapsed for execution.
Usage: python computeSales.py priceCatalogue.json salesRecord.json
PEP 8 compliant.
"""


import json
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
import sys
import time


def load_json(file_path):
    """Loads json file from path"""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON in file - {file_path}")
        sys.exit(1)


def compute_total_cost(price_catalogue, sales_record):
    """Compute total costs"""
    total_cost = 0
    for sale in sales_record:
        product_name, quantity = sale["Product"], sale["Quantity"]
        matching_products = [item for item in price_catalogue
                             if item["title"] == product_name]
        if matching_products:
            price = Decimal(matching_products[0]["price"])
            total_cost += price * quantity
        else:
            print(f"Warning: Product '{product_name}' not found"
                  + " in price catalogue.")

    return total_cost


def main():
    """Main function"""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json"
              + "salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    price_catalogue_path = sys.argv[1]
    sales_record_path = sys.argv[2]

    price_catalogue = load_json(price_catalogue_path)
    sales_record = load_json(sales_record_path)

    total_cost = compute_total_cost(price_catalogue, sales_record)

    rnd_ttl_cost = Decimal(total_cost).quantize(Decimal('0.01'),
                                                rounding=ROUND_HALF_UP)

    elapsed_time = time.time() - start_time

    print(f"File: {sales_record_path}")
    print(f"Total cost: ${rnd_ttl_cost}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")

    # Writing results to SalesResults.txt
    with open("SalesResults.txt", "a", encoding="utf-8") as result_file:
        result_file.write(f"{datetime.now()} - File: {sales_record_path} "
                          + f"Total cost: ${rnd_ttl_cost} "
                          + f"Time elapsed: {elapsed_time:.2f} seconds\n")


if __name__ == "__main__":
    main()
