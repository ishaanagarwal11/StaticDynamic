import pandas as pd

# Load the file
df = pd.read_csv("testt.csv")

# Add engineered features
df["L_diff"] = df["L1"] - df["L2"]
df["U_diff"] = df["U1"] - df["U2"]
df["L_ratio"] = df["L1"] / (df["L2"] + 1e-6)
df["U_ratio"] = df["U1"] / (df["U2"] + 1e-6)
df["Power_like"] = df["L1"] * df["U1"]
df["Combined_spectrum"] = df["CURRENT_SPECTRUM"] * df["TORQUE_RIPPLE"]

# Save updated version
updated_path = "test_clean.csv"
df.to_csv(updated_path, index=False)

print(f"✅ Updated data with engineered features saved to '{updated_path}'.")