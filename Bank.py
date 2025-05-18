from faker import Faker
import csv
import random

fake = Faker()
output_file_path_bank = r'C:\Users\lenovo\Downloads\bank.csv'
output_file_path_bank_rentability = r'C:\Users\lenovo\Downloads\bank_rentability.csv'
# Specify the number of rows you want to generate
num_rows = 10
type=["Deposit","Loan","Card","Loan","Deposit","Loan","Card","Loan","Deposit","Loan"]
product = [
    "Savings Account",
    "Personal Loan",
    "Credit Card",
    "Auto Loan",
    "Checking Account",
    "Mortgage",
    "Rewards Credit Card",
    "Business Loan",
    "Money Market Account",
    "Student Loan" ]
# Define the header and field names
products = []
# Generate and write data to the CSV file
for i in range(num_rows):
    product_id = i
    product_name = product[i]
    product_type = type[i]
    interest=round(random.uniform(1, 12), 2)
    products.append((product_id, product_name, product_type,interest))

with open(output_file_path_bank, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(products)  # Write data rows

import csv
from faker import Faker
import random

fake = Faker()

# Specify the number of rows you want to generate
num_rows = 87467

# Generate and write data to the CSV file
with open(output_file_path_bank_rentability, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header
    csvwriter.writerow(['product_id', 'client_id', 'year', 'revenue', 'expenses', 'profit'])

    # Generate and write data rows
    for _ in range(num_rows):
        product_id = random.randint(1, 9)  # Assuming 10 products
        client_id = random.randint(1, 87467)  # Assuming 100 clients
        year = random.randint(2010, 2023)
        revenue = round(random.uniform(1000, 100000000), 2)
        expenses = round(random.uniform(500, 500000), 2)
        profit = round(revenue - expenses, 2)
        while profit<0 and profit<100000:
            # Code to execute in the loop
                revenue = round(random.uniform(1000, 100000000), 2)
                expenses = round(random.uniform(500, 500000), 2)
                profit = round(revenue - expenses, 2)
        csvwriter.writerow([product_id, client_id, year, revenue, expenses, profit])

print(f"{num_rows} rows of fake data generated and written to 'product_rentability.csv'.")
