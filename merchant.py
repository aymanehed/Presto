import csv
import random
from faker import Faker

fake = Faker()
output_file_path_merchant = r'C:\Users\lenovo\Downloads\merchant.csv'
output_file_path_merchant_transaction = r'C:\Users\lenovo\Downloads\merchant_transaction.csv'
# Define the number of merchants you want to generate
num_merchants = 100

# Generate fake merchant data
merchants = []
for _ in range(num_merchants):
    merchant_id = fake.random_int(min=1, max=1000)
    merchant_name = fake.company()
    category = fake.random_element(elements=('Electronics', 'Clothing', 'Groceries', 'Books'))
    merchants.append((merchant_id, merchant_name, category))

with open(output_file_path_merchant, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['merchant_id', 'merchant_name', 'category'])  # Write header
    csv_writer.writerows(merchants)  # Write data rows

amount = [100000, 200000, 300000, 400000, 500000, 60000, 700000, 8000000, 9000000, 1000000, 20000000, 30000000, 4000000,
          500000, 600000, 7000000, 800000, 9000000, 10000000]
num_transactions = 100  # You can adjust the number of transactions to generate
transaction_data = []
for id in range(1, 100):
    transaction_data.append([
        id,
        random.randint(1, 100000),
        random.randint(1, 100),
        random.choice(list(amount))
    ])


with open(output_file_path_merchant_transaction, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['merchant_transaction_id', 'transaction_id', 'merchant_id', 'amount'])
    csv_writer.writerows(transaction_data)
