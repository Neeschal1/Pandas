import pandas as pd
from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Swift GO14\OneDrive\Desktop\Neeschal.py\Pandas\basics\students.csv"
)

print(df)
print(tabulate(df,headers="keys", tablefmt="grid"))
