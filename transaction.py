from faker import Faker
import csv
import random
from datetime import datetime, timedelta

output_file_path_transaction = r'C:\Users\lenovo\Downloads\transaction.csv'
output_file_path_transaction_type = r'C:\Users\lenovo\Downloads\transaction_type.csv'
output_file_path_transaction_location = r'C:\Users\lenovo\Downloads\transaction_location.csv'
output_file_path_location = r'C:\Users\lenovo\Downloads\location.csv'
fake = Faker()
# Define allowed type_name values
allowed_type_names = ['Deposit', 'Withdrawal', 'Transfer', 'Purchase', 'Payment']

# Generate fake transaction types
transaction_types_data = []
for i in range(1, 100001):
    type_name = random.choice(allowed_type_names)
    transaction_types_data.append([i, type_name])

with open(output_file_path_transaction_type, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["type_id", "type_name"])
    writer.writerows(transaction_types_data)
# List of Moroccan cities (you might need a larger list)

# Generate a CSV file with the generated data
import csv
import random

# Dictionary of Moroccan regions and their corresponding cities
moroccan_regions = {
    "Casablanca-Settat": ["Casablanca", "Settat"],
    "Rabat-Sale-Kenitra": ["Rabat", "Sale", "Kenitra"],
    "Marrakech-Safi": ["Marrakech", "Safi"],
    "Fes-Meknes": ["Fes", "Meknes"],
    "Tanger-Tetouan-Al Hoceima": ["Tanger", "Tetouan", "Hoceima"]
}

# Generate a CSV file with the generated data

with open(output_file_path_location, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["location_id", "region", "city"])

    for i in range(1, 100001):
        region = random.choice(list(moroccan_regions.keys()))
        cities = moroccan_regions[region]
        city = random.choice(cities)
        writer.writerow([i, region, city])

transactions_data = []
start_date = datetime(2023, 1, 1)
end_date = datetime.today()
amount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
for i in range(1, 100000):
    transactions_data.append([
        i,
        random.randint(1, 100000),  # Assuming account_ids range from 1 to 100000
        random.randint(1, 5),  # Assuming type_ids range from 1 to 5
        random.choice(list(amount)),
        start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    ])

with open(output_file_path_transaction, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "account_id", "type_id", "amount", "transaction_date"])
    writer.writerows(transactions_data)

# Generate fake transaction locations
transaction_locations_data = []
for i in range(1, 100000):
    transaction_locations_data.append([
        i,
        random.randint(1, 100000),  # Assuming transaction_ids range from 1 to 100000
        round(fake.latitude(), 8),
        round(fake.longitude(), 8)
    ])

with open(output_file_path_transaction_location, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["location_id", "transaction_id", "latitude", "longitude"])
    writer.writerows(transaction_locations_data)
