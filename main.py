import pandas as pd

# Reading expense.csv
df = pd.read_csv("data/expense.csv")



# Printing all transactions
print(df.to_string(index = False))



# Printing total money spent
total_spent = df["Amount"].sum()

print(f"\n\nTotal spent = {total_spent}")
