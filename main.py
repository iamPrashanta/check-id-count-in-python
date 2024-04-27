import pandas as pd

def count_all_member_ids(filename):
    # Load the Excel file
    df = pd.read_excel(filename)

    # Count occurrences of each member ID in the 'REF ID' column
    counts = df['REF ID'].value_counts().to_dict()

    return counts

filename = 'excel_file.xlsx'
output_filename = 'member_ids_new.txt'
counts = count_all_member_ids(filename)
with open(output_filename, 'w') as f:
    for member_id, count in counts.items():
        if count > 30:
            f.write(f"{member_id}, \n")
