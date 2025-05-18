import pandas as pd
output_file_path_customer = r'C:\Users\lenovo\Downloads\customer.csv'
output_file_path_account = r'C:\Users\lenovo\Downloads\account.csv'
data = []
from faker import Faker
import csv
import random
from datetime import datetime, timedelta
fake = Faker()
header = ["customer_id", "first_name", "last_name", "date_of_birth", "address", "phone_number", "email"]
data = []
lasts=["Benani","Benjelloun","Tazi","Berrada","Mortaki","Heddad","khafife","Karam","Benmsoud","Behloul","Radi","Amrani","Amani","Fasi","Idrissi","Zaki" ]
adresses=["Casablanca", "Settat","Rabat", "Sale", "Kenitra","Marrakech", "Safi","Fes", "Meknes","Tanger", "Tetouan", "Hoceima"]
firsts=["Ahmed","Anas","Aymane","Anas","Amine","Amir","Amina","Amira","Achraf","Badr","Basma","abdelkader","abdelaziz","camelia","chaimaa","chorouk", "driss","alaa","alia","ali","fahd","sanaa","yasmina","adam","yasmine","Aya","Ghali","Rania","Jihane","Meriam","Asmaa","Mounir","Merouane","abdellah","Adil","Doha","Hafssa","Ziani","mezyani","Zoubaa","Daki","Daoui","Barakat","Moussaoui","Touzani","Chakib","chakiri","Chakir","kortobi","Jaadi","Benmalak","Ouadi","Bennis"]
for i in range(1, 100001):
    first=random.choice(list(firsts));
    last=random.choice(list(lasts));
    email=first+"."+last+"@gmail.com";
    phone="+212 6"+str(random.randint(63573899,67484954));
    adress=random.choice(list(adresses));
    data.append([
        i,
        first,
        last,
        fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
        adress,
        phone,
        email

    ]);

with open(output_file_path_customer, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

header = ["account_id", "customer_id", "balance", "open_date"]
data = []

for i in range(1, 100001):
    data.append([
        i,
        random.randint(1, 100000),  # Assuming customer_ids range from 1 to 100000
        round(random.uniform(100, 10000), 2),
        (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
    ])
with open(output_file_path_account, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)