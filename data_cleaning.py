import pandas as pd
# Load your data
df = pd.read_excel("Raw Data.xlsx")
# Check for duplicate rows
duplicates = df[df.duplicated()]
print(f"Number of duplicate rows: {duplicates.shape[0]}")
# View duplicate rows (optional)
print(duplicates)

# Remove duplicate rows
df_cleaned = df.drop_duplicates()
# Save to new Excel file
df_cleaned.to_excel("Cleaned_Data.xlsx",index=False)


#missing values
print(df.isnull().sum())
df['Income'].fillna(df['Income'].mean(), inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)       #for categorical data


# Check unique values in each categorical column
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"{col}:", df[col].unique())

    
