import csv
from faker import Faker

fake = Faker()
output_file_path_transaction_fraud_patterns = r'C:\Users\lenovo\Downloads\transaction_fraud_patterns.csv.csv'
# Specify the number of rows you want to generate
num_rows = 253

# Define the header and field names
fraud = []
# Generate and write data to the CSV file
for i in range(num_rows):
    transaction_fraud_id = i
    transaction_id = fake.random_int(min=1, max=100000)
    fraud.append((transaction_fraud_id,transaction_id))

with open(output_file_path_transaction_fraud_patterns , 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(fraud)  # Write data rows
