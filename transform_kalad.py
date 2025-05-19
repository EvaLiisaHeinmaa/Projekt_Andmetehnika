import pandas as pd

# Read the Excel file
df = pd.read_excel("kalad.xlsx", engine="openpyxl")

# Rename columns
df = df.rename(columns={
    df.columns[0]: "Näitaja",
    df.columns[1]: "Aasta"
})

# Strip whitespace from column names
df.columns = [col.strip() for col in df.columns]

# Convert "Aasta" to numeric (nullable integer)
df["Aasta"] = pd.to_numeric(df["Aasta"], errors="coerce").astype("Int64")

# Convert all fish-related columns to numeric (everything except "Näitaja")
fish_cols = df.columns.drop("Näitaja")
df[fish_cols] = df[fish_cols].apply(pd.to_numeric, errors="coerce")

# Add a numeric ID for each unique "Näitaja"
df["Näitaja_ID"] = df["Näitaja"].astype("category").cat.codes

# Move "Näitaja_ID" to the first column
cols = df.columns.tolist()
cols.remove("Näitaja_ID")
cols.insert(0, "Näitaja_ID")
df = df[cols]

# Save to Parquet
df.to_parquet("kalad.parquet", index=False)
