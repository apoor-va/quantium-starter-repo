import pandas as pd
import glob

# get all CSV files
files = glob.glob("data/*.csv")

df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

data = pd.concat(df_list, ignore_index=True)

# filter pink morsel only
data = data[data["product"] == "pink morsel"]

# clean price
data["price"] = data["price"].replace(r'[$,]', '', regex=True).astype(float)

# create sales
data["sales"] = data["quantity"] * data["price"]

# keep required columns
data = data[["sales", "date", "region"]]

# save output
data.to_csv("output.csv", index=False)

print("Done! output.csv created")