# df = pd.read_csv("")
# df = (df
# .assign(
#     new_column=lambda x: x["Document No"].str.split('-').str[0]
#     ):
#     parts = code.split('-')
#     # Take first 2 parts if possible
#     main = ''.join(parts[:2])
#     # Remove any slashes or dashes
#     cleaned = main.replace('/', '').replace('-', '')
#     return cleaned

# # Example usage
# raw_list = [
#     "AR-PY357583-abdbf-fjenf-jfnfjf",
#     "JV-24/08/23",
#     "AP-123456-other-extra",
#     "RV-01/07/25-extra-info",
#     "UOB-ABC123-xyz-data",
#     "RV/01/07/25-extra"
# ]

# cleaned_list = [clean_code(x) for x in raw_list]
# print(cleaned_list)
import pandas as pd

# Define your clean_code function
def clean_code(code):
    parts = str(code).split('-')
    main = ''.join(parts[:2])  # Take first two parts
    cleaned = main.replace('/', '').replace('-', '')
    return cleaned

# Read CSV (replace with actual path)
df = pd.read_excel(r"C:\Users\shaunteojw\Downloads\Shaun\Copy of GL.xlsx")

# Create new cleaned column
df['cleaned_doc_no'] = df['Document No'].apply(clean_code)

# Preview
print(df[['Document No', 'cleaned_doc_no']])
