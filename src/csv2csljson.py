import json
import pandas as pd

# Load the CSV file
file_path = "./in/pocket-export.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the CSV to understand its structure
df.head()

# Convert the DataFrame to CSL-JSON format
csl_json = [
        {
            "type": "webpage",
            "title": row["title"],
            "URL": row["url"],
            # Unix timestamp
            "issued": {"date-parts": [[int(row["time_added"])]]},
            "categories": [row["tags"]] if pd.notna(row["tags"]) else []
            }
        for _, row in df.iterrows()
        ]

# Save the CSL-JSON to a file
csl_json_path = "./out/converted_csl.json"
with open(csl_json_path, "w", encoding="utf-8") as f:
    json.dump(csl_json, f, indent=4)

csl_json_path
