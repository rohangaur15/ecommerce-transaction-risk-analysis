## Data inspection
## Data set information

import pandas as pd
import numpy as np

df = pd.read_csv("data/transactions_raw.csv")

print("Dataset shape:", df.shape)
print("\nDataset information:")
df.info()

## checking missing values 
print("\nMissing values:")
print(df.isnull().sum())

## checking duplicate transactions
print("\nDuplicate rows:")
print(df.duplicated().sum())

## checking numerical values
print("\nTransaction amount statistics:")
print(df["Transaction_Amount"].describe())

## checking account age
print("\nAccount age statistics:")
print(df["Account_Age_Days"].describe())

## checking previous order
print("\nPrevious orders statistics:")
print(df["Previous_Orders"].describe())

## checking previous cancellations
print("\nPrevious cancellations statistics:")
print(df["Previous_Cancellations"].describe())

## checking previous refunds
print("\nPrevious refunds statistics:")
print(df["Previous_Refunds"].describe())

## checking previous failed payment attempts
print("\nFailed payment attempts statistics:")
print(df["Failed_Payment_Attempts"].describe())

## checking payment method values
print("\nPayment Method values:")
print(df["Payment_Method"].value_counts())

## checking new payment method values
print("\nNew Payment Method values:")
print(df["New_Payment_Method"].value_counts())

## checking new delivery address
print("\nNew Delivery Address values:")
print(df["New_Delivery_Address"].value_counts())


## checking duplicate transaction IDs
print("\nDuplicate Transaction IDs:")
print(df["Transaction_ID"].duplicated().sum())

## checking unique customers
print("\nUnique customers:")
print(df["Customer_ID"].nunique())

## checking negative numerical values
print("\nNegative numerical values:")

numerical_columns = [
    "Transaction_Amount",
    "Account_Age_Days",
    "Previous_Orders",
    "Previous_Cancellations",
    "Previous_Refunds",
    "Failed_Payment_Attempts"
]

for column in numerical_columns:
    print(column, ":", (df[column] < 0).sum())


    ## creating a working copy for data quality testing
df_dirty = df.copy()
print("\nWorking copy created successfully!")
print("Dirty dataset shape:", df_dirty.shape)

## introducing missing values

df_dirty.loc[10, "Transaction_Amount"] = np.nan
df_dirty.loc[25, "Transaction_Amount"] = np.nan
df_dirty.loc[50, "Transaction_Amount"] = np.nan

print("\nMissing values introduced:")
print(df_dirty["Transaction_Amount"].isnull().sum())

## introducing duplicate rows
df_dirty = pd.concat(
    [df_dirty, df_dirty.iloc[[100, 200, 300]]],
    ignore_index=True
)

print("\nDuplicate rows introduced:")
print(df_dirty.duplicated().sum())

## introducing invalid transaction amounts
df_dirty.loc[150, "Transaction_Amount"] = -500
df_dirty.loc[250, "Transaction_Amount"] = -1000

print("\nInvalid transaction amounts introduced:")
print((df_dirty["Transaction_Amount"] < 0).sum())

## introducing invalid payment method
df_dirty.loc[350, "Payment_Method"] = "Bitcoin"

print("\nInvalid payment methods introduced:")
valid_payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

print(
    (~df_dirty["Payment_Method"].isin(valid_payment_methods)).sum()
)

## saving dirty dataset
df_dirty.to_csv("data/transactions_dirty.csv", index=False)

print("\nDirty dataset saved successfully!")
print("Dirty dataset shape:", df_dirty.shape)



## detecting missing values
print("\nMissing values in dirty dataset:")
print(df_dirty.isnull().sum())

## detecting duplicate rows
print("\nDuplicate rows in dirty dataset:")
print(df_dirty.duplicated().sum())

## detecting negative transaction amounts
print("\nNegative transaction amounts in dirty dataset:")
print((df_dirty["Transaction_Amount"] < 0).sum())

## detecting invalid payment methods
valid_payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

invalid_payment_methods = ~df_dirty["Payment_Method"].isin(valid_payment_methods)

print("\nInvalid payment methods in dirty dataset:")
print(invalid_payment_methods.sum())


## cleaning step
## cleaning missing transaction amounts

df_clean = df_dirty.dropna(subset=["Transaction_Amount"])

print("\nAfter removing missing transaction amounts:")
print("Rows:", df_clean.shape[0])
print("Missing transaction amounts:", df_clean["Transaction_Amount"].isnull().sum())


## cleaning duplicate rows
df_clean = df_clean.drop_duplicates()
print("\nAfter removing duplicate rows:")
print("Rows:", df_clean.shape[0])
print("Duplicate rows:", df_clean.duplicated().sum())

## cleaning negative transaction amounts
df_clean = df_clean[df_clean["Transaction_Amount"] >= 0]
print("\nAfter removing negative transaction amounts:")
print("Rows:", df_clean.shape[0])
print("Negative transaction amounts:", (df_clean["Transaction_Amount"] < 0).sum())


## cleaning invalid payment methods
df_clean = df_clean[
    df_clean["Payment_Method"].isin(valid_payment_methods)
]

print("\nAfter removing invalid payment methods:")
print("Rows:", df_clean.shape[0])
print(
    "Invalid payment methods:",
    (~df_clean["Payment_Method"].isin(valid_payment_methods)).sum()
)


## validating cleaned dataset

print("\n--- Cleaned Dataset Validation ---")

print("Dataset shape:", df_clean.shape)

print("\nMissing values:")
print(df_clean.isnull().sum())

print("\nDuplicate rows:")
print(df_clean.duplicated().sum())

print("\nNegative transaction amounts:")
print((df_clean["Transaction_Amount"] < 0).sum())

print("\nInvalid payment methods:")
print(
    (~df_clean["Payment_Method"].isin(valid_payment_methods)).sum()
)


## saving cleaned dataset

df_clean.to_csv("data/transactions_clean.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Cleaned dataset shape:", df_clean.shape)