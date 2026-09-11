import pandas as pd

df = pd.read_csv("data/transactions_clean.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


## Transaction amount analysis

print("\n--- Transaction Amount Analysis ---")

print("\nTransaction amount statistics:")
print(df["Transaction_Amount"].describe())

## Highest-value transactions
print("\nTop 10 highest-value transactions:")

top_transactions = df[
    ["Transaction_ID", "Customer_ID", "Transaction_Amount"]
].sort_values(
    "Transaction_Amount",
    ascending=False
).head(10)

print(top_transactions)

## Failed payment attempts analysis
print("\n--- Failed Payment Attempts Analysis ---")

print("\nFailed payment attempts statistics:")
print(df["Failed_Payment_Attempts"].describe())

print("\nFailed payment attempts distribution:")
print(df["Failed_Payment_Attempts"].value_counts().sort_index())


## Previous cancellations analysis
print("\n--- Previous Cancellations Analysis ---")

print("\nPrevious cancellations statistics:")
print(df["Previous_Cancellations"].describe())

print("\nPrevious cancellations distribution:")
print(df["Previous_Cancellations"].value_counts().sort_index())



## Previous refunds analysis
print("\n--- Previous Refunds Analysis ---")

print("\nPrevious refunds statistics:")
print(df["Previous_Refunds"].describe())

print("\nPrevious refunds distribution:")
print(df["Previous_Refunds"].value_counts().sort_index())

## New payment method analysis
print("\n--- New Payment Method Analysis ---")

print("\nNew payment method distribution:")
print(df["New_Payment_Method"].value_counts())


## New delivery address analysis
print("\n--- New Delivery Address Analysis ---")

print("\nNew delivery address distribution:")
print(df["New_Delivery_Address"].value_counts())


## Account age analysis
print("\n--- Account Age Analysis ---")

print("\nAccount age statistics:")
print(df["Account_Age_Days"].describe())

## Previous orders analysis
print("\n--- Previous Orders Analysis ---")

print("\nPrevious orders statistics:")
print(df["Previous_Orders"].describe())


## Risk indicator: High transaction amount
amount_threshold = df["Transaction_Amount"].quantile(0.75)

df["High_Transaction_Amount"] = (
    df["Transaction_Amount"] > amount_threshold
).astype(int)

print("\n--- High Transaction Amount Indicator ---")

print("Amount threshold:", amount_threshold)

print("\nHigh transaction amount distribution:")
print(df["High_Transaction_Amount"].value_counts())


## Risk indicator: Multiple failed payment attempts
failed_payment_threshold = df["Failed_Payment_Attempts"].quantile(0.75)

df["Multiple_Failed_Payments"] = (
    df["Failed_Payment_Attempts"] > failed_payment_threshold
).astype(int)

print("\n--- Multiple Failed Payment Indicator ---")

print("Failed payment threshold:", failed_payment_threshold)

print("\nMultiple failed payment distribution:")
print(df["Multiple_Failed_Payments"].value_counts())


## Risk indicator: High cancellation history
cancellation_threshold = df["Previous_Cancellations"].quantile(0.75)

df["High_Cancellation_History"] = (
    df["Previous_Cancellations"] > cancellation_threshold
).astype(int)

print("\n--- High Cancellation History Indicator ---")

print("Cancellation threshold:", cancellation_threshold)

print("\nHigh cancellation history distribution:")
print(df["High_Cancellation_History"].value_counts())

## Risk indicator: High refund history
refund_threshold = df["Previous_Refunds"].quantile(0.75)

df["High_Refund_History"] = (
    df["Previous_Refunds"] > refund_threshold
).astype(int)

print("\n--- High Refund History Indicator ---")

print("Refund threshold:", refund_threshold)

print("\nHigh refund history distribution:")
print(df["High_Refund_History"].value_counts())

## Risk indicator: New payment method
df["New_Payment_Method_Indicator"] = (
    df["New_Payment_Method"] == "Yes"
).astype(int)

print("\n--- New Payment Method Indicator ---")

print(
    df["New_Payment_Method_Indicator"].value_counts()
)

## Risk indicator: New delivery address
df["New_Delivery_Address_Indicator"] = (
    df["New_Delivery_Address"] == "Yes"
).astype(int)

print("\n--- New Delivery Address Indicator ---")

print(
    df["New_Delivery_Address_Indicator"].value_counts()
)


## Risk indicator: New/young account
account_age_threshold = df["Account_Age_Days"].quantile(0.25)

df["New_Account_Indicator"] = (
    df["Account_Age_Days"] < account_age_threshold
).astype(int)

print("\n--- New Account Indicator ---")

print("Account age threshold:", account_age_threshold)

print("\nNew account indicator distribution:")
print(df["New_Account_Indicator"].value_counts())



## Creating risk score
risk_indicators = [
    "High_Transaction_Amount",
    "Multiple_Failed_Payments",
    "High_Cancellation_History",
    "High_Refund_History",
    "New_Payment_Method_Indicator",
    "New_Delivery_Address_Indicator",
    "New_Account_Indicator"
]

df["Risk_Score"] = df[risk_indicators].sum(axis=1)

print("\n--- Risk Score Distribution ---")

print(df["Risk_Score"].value_counts().sort_index())


def classify_risk(score):
    if score <= 1:
        return "Low"
    elif score <= 3:
        return "Medium"
    else:
        return "High"


df["Risk_Level"] = df["Risk_Score"].apply(classify_risk)

print("\n--- Risk Level Distribution ---")
print(df["Risk_Level"].value_counts())



## investigation T10126
print("\n--- Investigation: T10126 ---")

case = df[df["Transaction_ID"] == "T10126"].iloc[0]

print("\nTransaction Details:")
print("Transaction ID:", case["Transaction_ID"])
print("Customer ID:", case["Customer_ID"])
print("Transaction Amount:", case["Transaction_Amount"])
print("Payment Method:", case["Payment_Method"])
print("Account Age (Days):", case["Account_Age_Days"])
print("Previous Orders:", case["Previous_Orders"])
print("Previous Cancellations:", case["Previous_Cancellations"])
print("Previous Refunds:", case["Previous_Refunds"])
print("Failed Payment Attempts:", case["Failed_Payment_Attempts"])
print("New Payment Method:", case["New_Payment_Method"])
print("New Delivery Address:", case["New_Delivery_Address"])

print("\nRisk Indicators:")
print("High Transaction Amount:", case["High_Transaction_Amount"])
print("Multiple Failed Payments:", case["Multiple_Failed_Payments"])
print("High Cancellation History:", case["High_Cancellation_History"])
print("High Refund History:", case["High_Refund_History"])
print("New Payment Method Indicator:", case["New_Payment_Method_Indicator"])
print("New Delivery Address Indicator:", case["New_Delivery_Address_Indicator"])
print("New Account Indicator:", case["New_Account_Indicator"])

print("\nFinal Assessment:")
print("Risk Score:", case["Risk_Score"])
print("Risk Level:", case["Risk_Level"])





print("\n--- Top High-Risk Transactions ---")

high_risk_transactions = df[
    df["Risk_Level"] == "High"
].sort_values(
    "Risk_Score",
    ascending=False
)
top_10_cases = high_risk_transactions.head(10).copy()

top_10_cases["Triggered_Indicators"] = top_10_cases[
    risk_indicators
].sum(axis=1)


## top 10 high risk investigation summary
print("\n--- Top 10 High-Risk Investigation Summary ---")

top_10_cases = high_risk_transactions.head(10).copy()

top_10_cases["Triggered_Indicators"] = top_10_cases[
    risk_indicators
].sum(axis=1)

print(
    top_10_cases[
        [
            "Transaction_ID",
            "Transaction_Amount",
            "Account_Age_Days",
            "Previous_Cancellations",
            "Previous_Refunds",
            "Failed_Payment_Attempts",
            "New_Payment_Method",
            "New_Delivery_Address",
            "Risk_Score",
            "Risk_Level",
            "Triggered_Indicators"
        ]
    ].to_string(index=False)
)


## risk indicator frequency
print("\n--- Risk Indicator Frequency in High-Risk Transactions ---")

indicator_frequency = high_risk_transactions[
    risk_indicators
].sum().sort_values(ascending=False)

print(indicator_frequency)


## overall vs high risk tansaction 
print("\n--- Overall vs High-Risk Indicator Frequency ---")
overall_frequency = df[risk_indicators].sum()
high_risk_frequency = high_risk_transactions[risk_indicators].sum()

comparison = pd.DataFrame({
    "Overall_Count": overall_frequency,
    "High_Risk_Count": high_risk_frequency
})

print(comparison)


print("\n--- Overall vs High-Risk Indicator Percentage ---")
overall_percentage = (
    overall_frequency / len(df) * 100
)

high_risk_percentage = (
    high_risk_frequency / len(high_risk_transactions) * 100
)

percentage_comparison = pd.DataFrame({
    "Overall_Percentage": overall_percentage.round(2),
    "High_Risk_Percentage": high_risk_percentage.round(2)
})

print(
    percentage_comparison.to_string(
        formatters={
            "Overall_Percentage": "{:.2f}%".format,
            "High_Risk_Percentage": "{:.2f}%".format
        }
    )
)

## Risk Score ke according transaction amount
print("\n--- Transaction Amount by Risk Score ---")

amount_by_risk_score = (
    df.groupby("Risk_Score")["Transaction_Amount"]
    .agg(["count", "mean", "median", "max"])
    .round(2)
)

print(amount_by_risk_score)

## Risk Level summary
print("\n--- Risk Level Summary ---")

risk_level_summary = (
    df.groupby("Risk_Level")["Transaction_Amount"]
    .agg(["count", "mean", "median", "max"])
    .round(2)
)

print(risk_level_summary)


