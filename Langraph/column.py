import pandas as pd

# Load the dataset
file_path = 'amazon.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Get all column names
column_names = df.columns.tolist()

# Print the column names
print("Column Names:")
for col in column_names:
    print(col)
