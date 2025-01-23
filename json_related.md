## Read Json to Pandas df using Json ( more control and flexibility for complex JSON data)
```
import json
import pandas as pd
import os

def load_and_normalize_json(file_path):
    """Load a JSON file and normalize it into a Pandas DataFrame."""
    try:
        # Ensure the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file at {file_path} does not exist.")
        
        # Open and load the JSON data
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Normalize the JSON data into a DataFrame
        df = pd.json_normalize(data, 
                               record_path='links', 
                               meta=['name', 'customInfo'], 
                               record_prefix='links_')

        # Check if DataFrame is empty
        if df.empty:
            print("Warning: The resulting DataFrame is empty. Check the JSON structure.")

        return df

    except FileNotFoundError as fnf_error:
        print(f"File error: {fnf_error}")
    except json.JSONDecodeError as json_error:
        print(f"JSON decode error: {json_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the file path
file_path = r'\\fradata05.eu.degussanet.com\adn2fra005$\NSODataShare\WAN\SDWAN\SDWAN-IPs-json-lbl.txt'

# Load and normalize the JSON data
df_normalized = load_and_normalize_json(file_path)

# Optionally, display the DataFrame or perform further analysis
if df_normalized is not None:
    print(df_normalized.head())  # Display the first few rows of the DataFrame

```


## ## Read Json to Pandas df using Json (straight forward)
```
import pandas as pd
import os

def load_and_explode_json(file_path):
    """Load a JSON file and explode the 'links' column into a DataFrame."""
    try:
        # Ensure the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file at {file_path} does not exist.")
        
        # Read the JSON file into a DataFrame
        df = pd.read_json(file_path)

        # Check if the DataFrame is empty
        if df.empty:
            print("Warning: The resulting DataFrame is empty. Check the JSON structure.")
            return None

        # Explode the 'links' column
        df_exploded = df.explode('links').reset_index(drop=True)

        # Normalize the 'links' column to separate columns
        links_normalized = pd.json_normalize(df_exploded['links'])

        # Combine the original DataFrame with the normalized links
        df_final = pd.concat([df_exploded.drop(columns=['links']), links_normalized], axis=1)

        return df_final

    except ValueError as ve:
        print(f"Error reading JSON: {ve}")
    except FileNotFoundError as fnf_error:
        print(f"File error: {fnf_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the file path
file_path = r'\\fradata05.eu.degussanet.com\adn2fra005$\NSODataShare\WAN\SDWAN\SDWAN-IPs-json-lbl.txt'

# Load and process the JSON data
df_processed = load_and_explode_json(file_path)

# Optionally, display the DataFrame or perform further analysis
if df_processed is not None:
    print(df_processed.head())  # Display the first few rows of the DataFrame

```
