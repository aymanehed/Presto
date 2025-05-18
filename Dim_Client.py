import pandas as pd
from faker import Faker
import csv
import random
from datetime import datetime, timedelta
output_file_path_Dim_Client = r'C:\Users\lenovo\Downloads\Dim_Client.csv'
data = []
fake = Faker()
header = ["Pk_Client", "Id", "Nom","Prenom", "date_de_naissance", "Ville", "NumTel", "Email","Fk_store",'Fk_Commande']
Noms=["Benani","Benjelloun","Tazi","Berrada","Mortaki","Heddad","khafife","Karam","Benmsoud","Behloul","Radi","Amrani","Amani","Fasi","Idrissi","Zaki"]
Prenoms=["Ahmed","Anas","Aymane","Anas","Amine","Amir","Amina","Amira","Achraf","Badr","Basma","abdelkader","abdelaziz","camelia","chaimaa","chorouk", "driss","alaa","alia","ali","fahd","sanaa","yasmina","adam","yasmine","Aya","Ghali","Rania","Jihane","Meriam","Asmaa","Mounir","Merouane","abdellah","Adil","Doha","Hafssa","Ziani","mezyani","Zoubaa","Daki","Daoui","Barakat","Moussaoui","Touzani","Chakib","chakiri","Chakir","kortobi","Jaadi","Benmalak","Ouadi","Bennis"]
Villes=["Casablanca", "Settat","Rabat", "Sale", "Kenitra","Marrakech", "Safi","Fes", "Meknes","Tanger", "Tetouan", "Hoceima"]
for i in range(1, 100001):
    Pk_Client=i;
    Id='PR'+str(Pk_Client) +'SS';
    Nom=random.choice(list(Noms));
    Prenom=random.choice(list(Prenoms));
    Email=Prenom+"."+Nom+"@gmail.com";
    NumTel="+212 6"+str(random.randint(63573899,67484954));
    Ville=random.choice(list(Villes));
    Fk_store=random.randint(1,160);
    Fk_Commande=random.randint(1,250000);
    data.append([
        Pk_Client,
        Id,
        Nom,
        Prenom,
        fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
        Ville,
        NumTel,
        Email,
        Fk_store,
        Fk_Commande


    ]);

with open(output_file_path_Dim_Client, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)