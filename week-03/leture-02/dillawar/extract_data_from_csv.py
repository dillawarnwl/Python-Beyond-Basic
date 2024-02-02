import os
import csv

current_directory = os.getcwd()

# Construct the path to the CSV file
csv_file_path = os.path.join(current_directory, 'sample.csv')

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Assuming the age is in the second column (index 1)
    age_column_index = 1
    rows = []

    # Using a lambda function to filter rows where age is 25 and append the age to rows
    filter_function = lambda row: rows.append(int(row[age_column_index])) if int(row[age_column_index]) == 25 else None

    # Applying the filter function to each row
    for row in csv_reader:
        try:
            filter_function(row)
        except (ValueError, IndexError):
            pass

    # Printing the filtered ages
    print(rows)
