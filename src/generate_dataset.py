import pandas as pd
import numpy as np

np.random.seed(42)

## creating customer id
num_customers = 1000

customer_ids = [f"C{1000 + i}" for i in range(num_customers)]

print(customer_ids[:10])
print("Total customers:", len(customer_ids))

## creating transaction id
num_transactions = 5000

transaction_ids = [f"T{10000 + i}" for i in range(num_transactions)]

print(transaction_ids[:10])
print("Total transactions:", len(transaction_ids))

## assigning transaction to customers
customer_for_transaction = np.random.choice(
    customer_ids,
    size=num_transactions
)

print(customer_for_transaction[:10])

## generating transaction amount
transaction_amounts = np.round(
    np.random.lognormal(mean=7, sigma=1, size=num_transactions),
    2
)

print(transaction_amounts[:10])

## generating payment methods
payment_methods = np.random.choice(
    ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"],
    size=num_transactions
)

print(payment_methods[:10])

## generating account age for each customer

account_age = {
    customer_id: np.random.randint(1, 1501)
    for customer_id in customer_ids
}

print(list(account_age.items())[:10])

## generating previous order count for each customer

previous_orders = {
    customer_id: np.random.randint(0, 101)
    for customer_id in customer_ids
}

print(list(previous_orders.items())[:10])

## generating previous cancellation count for each customers
previous_cancellations = {
    customer_id: np.random.randint(0, 21)
    for customer_id in customer_ids
}

print(list(previous_cancellations.items())[:10])

## generating previous refund count for each customers
previous_refunds = {
    customer_id: np.random.randint(0, 16)
    for customer_id in customer_ids
}

print(list(previous_refunds.items())[:10])

## generating previous failed payment attempt for each customer
failed_payment_attempts = {
    customer_id: np.random.randint(0, 11)
    for customer_id in customer_ids
}

print(list(failed_payment_attempts.items())[:10])

## generating whether the payment method is new for the customer 
new_payment_method = np.random.choice(
    ["Yes", "No"],
    size=num_transactions,
    p=[0.15, 0.85]
)

print(new_payment_method[:10])

## generate whether the dilivery address is new 
new_delivery_address = np.random.choice(
    ["Yes", "No"],
    size=num_transactions,
    p=[0.10, 0.90]
)

print(new_delivery_address[:10])

# Get account age for each transaction's customer
transaction_account_age = [
    account_age[customer_id]
    for customer_id in customer_for_transaction
]

print(transaction_account_age[:10])

# Get previous orders for each transaction's customer
transaction_previous_orders = [
    previous_orders[customer_id]
    for customer_id in customer_for_transaction
]

print(transaction_previous_orders[:10])

# Get previous cancellations for each transaction's customer
transaction_previous_cancellations = [
    previous_cancellations[customer_id]
    for customer_id in customer_for_transaction
]

print(transaction_previous_cancellations[:10])

# Get previous refunds for each transaction's customer
transaction_previous_refunds = [
    previous_refunds[customer_id]
    for customer_id in customer_for_transaction
]

print(transaction_previous_refunds[:10])


# Get failed payment attempts for each transaction's customer
transaction_failed_payment_attempts = [
    failed_payment_attempts[customer_id]
    for customer_id in customer_for_transaction
]

print(transaction_failed_payment_attempts[:10])


# Create the transaction DataFrame
df = pd.DataFrame({
    "Transaction_ID": transaction_ids,
    "Customer_ID": customer_for_transaction,
    "Transaction_Amount": transaction_amounts,
    "Payment_Method": payment_methods,
    "Account_Age_Days": transaction_account_age,
    "Previous_Orders": transaction_previous_orders,
    "Previous_Cancellations": transaction_previous_cancellations,
    "Previous_Refunds": transaction_previous_refunds,
    "Failed_Payment_Attempts": transaction_failed_payment_attempts
})

print(df.head())


df = pd.DataFrame({
    "Transaction_ID": transaction_ids,
    "Customer_ID": customer_for_transaction,
    "Transaction_Amount": transaction_amounts,
    "Payment_Method": payment_methods,
    "Account_Age_Days": transaction_account_age,
    "Previous_Orders": transaction_previous_orders,
    "Previous_Cancellations": transaction_previous_cancellations,
    "Previous_Refunds": transaction_previous_refunds,
    "Failed_Payment_Attempts": transaction_failed_payment_attempts,
    "New_Payment_Method": new_payment_method,
    "New_Delivery_Address": new_delivery_address
})

print(df.head())

# Save the raw dataset
df.to_csv("data/transactions_raw.csv", index=False)

print("Raw dataset saved successfully!")


