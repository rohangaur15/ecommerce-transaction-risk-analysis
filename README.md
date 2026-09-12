# E-commerce Transaction Risk Analysis

## Overview

This project is a small data analysis project based on e-commerce transactions. The main idea was to look at transaction details and customer history and identify transactions that have multiple characteristics that may need further review.

I created a synthetic dataset of 5,000 transactions and added information such as transaction amount, payment method, account age, previous orders, cancellations, refunds, failed payment attempts, and changes in payment method or delivery address.

The project follows a simple workflow: generate the data, introduce some data-quality problems, clean and validate the data, explore the different variables, create risk indicators, and finally assign a risk level to each transaction.

The risk classification is rule-based. It is meant to help prioritize transactions for further investigation and is **not** intended to confirm whether a transaction is fraudulent.

---

## Objectives

The main things I wanted to work on in this project were:

- Creating a structured synthetic transaction dataset.
- Working with transaction and customer-level data.
- Practicing data cleaning and validation.
- Handling missing values, duplicates, and invalid records.
- Performing basic exploratory data analysis.
- Creating useful risk indicators from the available data.
- Building a simple rule-based risk score.
- Classifying transactions into Low, Medium, and High Risk.
- Looking at High Risk transactions and the indicators associated with them.
- Practicing an end-to-end data analysis workflow using Python.

---

## Dataset

The dataset was generated using Python, NumPy, and Pandas. It contains **5,000 transaction records** associated with approximately **1,000 customers**.

The main columns in the dataset are:

| Column | Description |
|---|---|
| `Transaction_ID` | Unique ID of the transaction |
| `Customer_ID` | ID of the customer |
| `Transaction_Amount` | Amount of the transaction |
| `Payment_Method` | Payment method used |
| `Account_Age_Days` | Age of the customer's account in days |
| `Previous_Orders` | Number of previous orders |
| `Previous_Cancellations` | Previous cancelled orders |
| `Previous_Refunds` | Previous refunds |
| `Failed_Payment_Attempts` | Previous failed payment attempts |
| `New_Payment_Method` | Whether a new payment method is being used |
| `New_Delivery_Address` | Whether a new delivery address is being used |

The dataset is completely synthetic. It does not contain real customer information, real transactions, or confirmed fraud labels.

---

## Data Cleaning

To practice working with imperfect data, I created a separate dirty copy of the original dataset and intentionally added a few common data-quality problems.

The dirty dataset contains:

- Missing transaction amounts.
- Duplicate records.
- Negative transaction amounts.
- An invalid payment method.

I used Pandas to identify these issues and then cleaned the data by removing records with missing transaction amounts, removing duplicates, filtering out negative amounts, and keeping only valid payment methods.

After cleaning and validation, the final dataset contained **4,994 valid transactions**.

The cleaned dataset was then used for the remaining analysis.

---

## Exploratory Data Analysis

After cleaning the data, I performed some basic exploratory analysis to understand the transaction and customer-related variables.

The analysis included:

- Transaction amount statistics.
- Failed payment attempts.
- Previous cancellation and refund history.
- New payment method usage.
- New delivery address usage.
- Customer account age.
- Previous orders.
- Risk score and risk-level distributions.

The transaction amounts in the cleaned dataset ranged from approximately **30.51 to 28,005.02**, with a median of approximately **1,056.56**.

The transaction amount showed a wide range, so I used it as one of the risk signals rather than treating it as a standalone indicator of risk.

---

## Risk Indicators

I created seven indicators using the available transaction and customer information:

| Risk Indicator | How it is used |
|---|---|
| High Transaction Amount | Transaction amount is above the 75th percentile |
| Multiple Failed Payments | Failed payment attempts are above the 75th percentile |
| High Cancellation History | Cancellation history is above the 75th percentile |
| High Refund History | Refund history is above the 75th percentile |
| New Payment Method | A new payment method is being used |
| New Delivery Address | A new delivery address is being used |
| New Account | Account age is below the 25th percentile |

Each indicator has a value of either `1` or `0`.

`1` means the condition is present and `0` means it is not.

The idea is not to consider one indicator as proof of risk. Instead, multiple indicators are considered together when assigning the overall risk score.

---

## Risk Scoring

Each triggered risk indicator contributes one point to the transaction's risk score.

**Risk Score = Sum of all triggered risk indicators**

There are seven indicators, so the theoretical score can range from 0 to 7. In this dataset, the highest observed score was 5.

I used the following project-defined thresholds:

| Risk Score | Risk Level |
|---|---|
| 0–1 | Low |
| 2–3 | Medium |
| 4–7 | High |

These thresholds are assumptions made specifically for this project. They are not based on the internal rules or policies of any particular e-commerce company.

A High Risk transaction in this project simply means that several predefined indicators were triggered. It does not mean that the transaction is confirmed to be fraudulent.

---

## Key Findings

After applying the scoring logic to the 4,994 cleaned transactions, the risk levels were distributed as follows:

| Risk Level | Transactions | Percentage |
|---|---:|---:|
| Low | 2,942 | 58.9% |
| Medium | 1,913 | 38.3% |
| High | 139 | 2.8% |

Only 139 transactions were classified as High Risk using the project-defined rules.

Among these High Risk transactions, the most common indicators were:

| Risk Indicator | High-Risk Transactions | Percentage |
|---|---:|---:|
| High Transaction Amount | 101 | 72.7% |
| New Account | 99 | 71.2% |
| High Cancellation History | 94 | 67.6% |
| Multiple Failed Payments | 86 | 61.9% |
| High Refund History | 74 | 53.2% |
| New Payment Method | 68 | 48.9% |
| New Delivery Address | 49 | 35.3% |

The average and median transaction amounts were also higher for the Medium and High Risk groups:

| Risk Level | Average Amount | Median Amount |
|---|---:|---:|
| Low | 1,268.87 | 879.06 |
| Medium | 2,363.00 | 1,536.65 |
| High | 3,326.60 | 2,843.41 |

This suggests that higher-value transactions were more common in the higher-risk groups in this particular dataset. However, transaction amount alone was not enough to determine the risk level.

---

## Project Structure

```text
ecommerce-transaction-risk-analysis/
│
├── data/
│   ├── transactions_raw.csv
│   ├── transactions_dirty.csv
│   └── transactions_clean.csv
│
├── src/
│   ├── generate_dataset.py
│   ├── data_analysis.py
│   └── risk_analysis.py
│
├── .gitignore
├── requirements.txt
└── README.md

```
## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rohangaur15/ecommerce-transaction-risk-analysis.git
```

### 2. Move into the project folder

```bash
cd ecommerce-transaction-risk-analysis
```

### 3. Create a virtual environment

On Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

### 6. Generate the dataset

```bash
python src/generate_dataset.py
```

### 7. Run the data cleaning process

```bash
python src/data_analysis.py
```

### 8. Run the risk analysis

```bash
python src/risk_analysis.py
```
