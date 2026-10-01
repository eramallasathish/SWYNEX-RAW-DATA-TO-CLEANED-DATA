from pathlib import Path
import pandas as pd

folder = Path(__file__).resolve().parent
input_file = folder / "e commerce project.csv.xlsx"
output_file = folder / "all_data.csv"

# Read the workbook: row 1 is a title; row 2 contains the headers.
df = pd.read_excel(
    input_file,
    sheet_name="cleaned data",
    header=1
)
df.columns = df.columns.str.strip()

# Save all rows and headers to a CSV file.
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"Saved {len(df)} rows and {len(df.columns)} columns to:")
print(output_file)
print(f"First order: {df.iloc[0]['Order id']}")
print(f"Last order:  {df.iloc[-1]['Order id']}")

# Display the full table in batches so PowerShell can keep up.
batch_size = 25

for start in range(0, len(df), batch_size):
    end = min(start + batch_size, len(df))
    print(f"\nRows {start + 1}–{end} of {len(df)}")
    print(df.iloc[start:end].to_string(index=False))

    if end < len(df):
        input("Press Enter to display the next rows...")