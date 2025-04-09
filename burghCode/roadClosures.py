import pandas as pd


dataUrl = "https://data.wprdc.org/datastore/dump/a9a1d93a-9d3b-4c18-bd80-82ed6f86404a"

# load dataset
data = pd.read_csv(dataUrl)


# Preview data set
print(data.head())


#optional, local copy
data.to_csv("road_closures.csv", index=False)
