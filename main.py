import pandas as pd

# Reading expense.csv
df = pd.read_csv("data/expense.csv")



# Printing all transactions
print(df.to_string(index = False))



# Printing total money spent
total_spent = df["Amount"].sum()

print(f"\n\nTotal spent = {total_spent}")



# Printing total spent by each category
print("\n\nTotal Spent by Category")
category_spending = df.groupby("Category")["Amount"].sum()
print(category_spending.sort_values(ascending = False))



# Printing total spent by store
print("\n\nTotal Spent by Store")
store_spending = df.groupby("Transaction_Name")["Amount"].sum()
print(store_spending.sort_values(ascending = False))



# Printing total spent by transaction type
print("\n\nTotal Spent by Transaction Type")
type_spending = df.groupby("Type")["Amount"].sum()
print(type_spending.sort_values(ascending = False))
