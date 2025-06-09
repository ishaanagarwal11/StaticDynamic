import pandas as pd

# Load the Excel file
file_path = "testt.xlsx"
df_raw = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=3)

# Rename columns
df_raw.columns = [
    "Drop", "SR_NO", "STATIC_ECC_A", "PCT_STATIC_ECC",
    "DYNAMIC_ECC", "X", "Y",
    "PCT_DYNAMIC_ECC", "L1", "L2", "U1", "U2",
    "TORQUE_RIPPLE", "TR_PCT", "CURRENT_SPECTRUM", "L1_U1_RATIO"
]

# ✅ Drop unwanted columns — KEEP X and Y this time
columns_to_drop = ["Drop", "SR_NO", "PCT_STATIC_ECC", "PCT_DYNAMIC_ECC", "TR_PCT"]
df_raw.drop(columns=columns_to_drop, inplace=True)

# Drop fully empty rows
df_raw.dropna(how='all', inplace=True)

# Convert all columns to numeric (errors='coerce' will turn invalid values to NaN)
for col in df_raw.columns:
    df_raw[col] = pd.to_numeric(df_raw[col], errors='coerce')

df_cleaned = df_raw.copy()

# Final shape
print("✅ Final shape:", df_cleaned.shape)
print(df_cleaned.head())

# Check for NaN values
nan_summary = df_cleaned.isna().sum()
nan_columns = nan_summary[nan_summary > 0]

if not nan_columns.empty:
    print("\n⚠️ Columns with missing values:")
    print(nan_columns)

    print("\n🔍 Rows with missing values:")
    print(df_cleaned[df_cleaned.isna().any(axis=1)])
else:
    print("\n✅ No missing values found.")

# Save the cleaned data with X and Y
df_cleaned.to_csv("testt.csv", index=False)
print("\n✅ Cleaned data with X and Y saved to 'testt.csv'.")
