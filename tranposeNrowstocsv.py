import pandas as pd

# Read data from text file into a list
file_path = 'statement.txt'  # Replace with the actual path to your text file
with open(file_path, 'r') as file:
    data_list = file.read().splitlines()

# Create DataFrame from the list
df = pd.DataFrame(data_list, columns=['Data'])

# Group by integer division of index by 5, select the 'Data' column, and transpose
df.groupby(df.index // 4).apply(lambda x: x.reset_index(drop=True).squeeze())
