import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("sample_data.xlsx", index=False)

print("Excel file created with sample data.")