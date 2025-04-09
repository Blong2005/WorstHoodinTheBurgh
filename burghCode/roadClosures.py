import pandas as pd

# URL to the CSV export of the dataset
url = "https://data.wprdc.org/datastore/dump/a9a1d93a-9d3b-4c18-bd80-82ed6f86404a"

# Load the dataset
df = pd.read_csv(url)

# Show the first few rows
print(df.head())

# Optionally save a local copy
df.to_csv("road_closures.csv", index=False)
