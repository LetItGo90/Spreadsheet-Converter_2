import csv
from collections import defaultdict
import os

# Read the source file and group by CASE_ID
grouped_data = defaultdict(list)

with open('your_spreadsheet.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    
    for row in reader:
        case_id = row['CASE_ID']
        grouped_data[case_id].append(row)

# Create output directory
output_dir = 'output_files'
os.makedirs(output_dir, exist_ok=True)

# Write each group to its own file, named by CASE_ID
for case_id, rows in grouped_data.items():
    # Clean the case_id for use as filename
    safe_filename = "".join(c if c.isalnum() or c in ('-', '_') else '_' for c in str(case_id))
    
    filepath = os.path.join(output_dir, f'{safe_filename}.csv')
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

print(f"Created {len(grouped_data)} files in '{output_dir}/'")
