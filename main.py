import pandas as pd

# Reading expense.csv
df = pd.read_csv("data/expense.csv")



# Printing all transactions
print(df.to_string(index = False))

