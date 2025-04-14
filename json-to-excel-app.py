import pandas as pd

# Load the JSON file
json_file = 'input_file.json'  # Replace with your JSON file path
data = pd.read_json(json_file)

# Convert the DataFrame to an Excel file
excel_file = 'output_file.xlsx'  # Replace with desired Excel file path
data.to_excel(excel_file, index=False, engine='openpyxl')

print(f'JSON data has been converted to Excel and saved as {excel_file}')
