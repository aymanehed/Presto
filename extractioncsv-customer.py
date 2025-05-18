import pandas as pd

# Read the CSV file
input_file_path = r'C:\Users\lenovo\Downloads\customer.csv'
output_file_path = r'C:\Users\lenovo\Downloads\organization.csv'

# Read the CSV into a pandas DataFrame
input_df = pd.read_csv(input_file_path, delimiter=',')

# Extract columns 1-6 and 9
columns_to_extract = input_df.columns[:6].tolist() + [input_df.columns[8]]
output_df = input_df[columns_to_extract]

# Save the extracted DataFrame to a new CSV file
output_df.to_csv(output_file_path, index=False)
