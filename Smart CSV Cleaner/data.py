import pandas as pd

df= pd.read_csv(r"C:\Users\sachi\OneDrive\MINI PROJECT\Smart CSV Cleaner\messy_data.csv")

print(df.head())

df.columns =[col.strip().lower().replace(" ","_") for col in df.columns]

print(df.dtypes)


# Remove Space 
# Convert into lowercase
for col in df.select_dtypes(include="object"):
    df[col]=df[col].astype(str).str.strip().str.lower()
    

# Email Validation

# Remove @@ if present

df['email']=df["email"].str.replace("@@","@", regex=False)
df["email"]  =df["email"].str.strip()
df["email"] = df["email"].str.lower()


# missing values 

df['name']= df["name"].replace("nan","unknown")
df["age"]= df["age"].fillna(df["age"].mean()).astype(int) 
df["salary"]= df['salary'].fillna(47000).astype(int)


# Parse the data column

df['join_date']= pd.to_datetime(df['join_date'],errors='coerce') 
df['join_date']= df['join_date'].fillna(pd.to_datetime('2021-01-01'))

duplicates =df.duplicated()  

count=duplicates.sum()
print(count)


df=df.drop_duplicates() 

df.to_csv("cleaned_data.csv",index=False)

print("Cleaned file saved as 'cleaned_data.csv'")   