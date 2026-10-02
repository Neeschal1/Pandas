import pandas as pd

url = "https://raw.githubusercontent.com/Neeschal1/abrovia-csv-data/refs/heads/main/universities/usa.csv"

df=pd.read_csv(url)
print(df)