import pandas as pd
import numpy as np
import os
from datetime import datetime

np.random.seed(42)

RAW_PATH = 'data/raw/PS_20174392719_1491204439457_log.csv'
CLEANED_PATH = 'data/cleaned/transactions_cleaned.csv'
REPORT_PATH = 'reports/transaction_cleaning_report.txt'

# AML/KYC CONTEXT:
# Clean transaction data is critical for AML analysts because:
# 1. Inconsistent formats delay investigations and SAR filing deadlines
# 2. Negative balances may indicate system errors or structuring attempts
# 3. High-value transactions require enhanced monitoring per BSA/AML regulations
# 4. Hourly patterns help identify suspicious after-hours activity

def clean_transactions():
    df = pd.read_csv(RAW_PATH)
    rows_before = len(df)
    
    print("=" * 60)
    print("TRANSACTION DATA CLEANING")
    print("=" * 60)
    
    print(f"\nRows before cleaning: {rows_before}")
    
    duplicates_before = df.duplicated().sum()
    df = df.drop_duplicates()
    print(f"Duplicates removed: {duplicates_before}")
    
    missing_before = df.isnull().sum().sum()
    print(f"Missing values before: {missing_before}")
    
    df['type'] = df['type'].str.strip().str.upper()
    
    valid_types = ['CASH_IN', 'CASH_OUT', 'PAYMENT', 'TRANSFER', 'DEBIT']
    df = df[df['type'].isin(valid_types)]
    
    df = df[df['amount'] >= 0]
    df = df[df['oldbalanceOrg'] >= 0]
    df = df[df['newbalanceOrig'] >= 0]
    df = df[df['oldbalanceDest'] >= 0]
    df = df[df['newbalanceDest'] >= 0]
    
    df['step'] = df['step'].astype(int)
    df['isFraud'] = df['isFraud'].astype(int)
    df['isFlaggedFraud'] = df['isFlaggedFraud'].astype(int)
    
    df['transaction_hour'] = ((df['step'] - 1) % 24).astype(int)
    df['transaction_day'] = ((df['step'] - 1) // 24 + 1).astype(int)
    df['is_high_value_transaction'] = (df['amount'] > 200000).astype(int)
    
    rows_after = len(df)
    
    os.makedirs('data/cleaned', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    df.to_csv(CLEANED_PATH, index=False)
    
    high_value_count = df['is_high_value_transaction'].sum()
    fraud_count = df[df['isFraud'] == 1].shape[0]
    
    print(f"\nHigh-value transactions (>200k): {high_value_count}")
    print(f"Fraudulent transactions: {fraud_count}")
    
    report = f"""Transaction Cleaning Report
Generated: {datetime.now()}

Rows before cleaning: {rows_before}
Rows after cleaning: {rows_after}
Rows removed: {rows_before - rows_after}
Duplicates removed: {duplicates_before}

Data types:
{df.dtypes.to_string()}

Missing values after cleaning:
{df.isnull().sum().to_string()}
"""
    
    with open(REPORT_PATH, 'w') as f:
        f.write(report)
    
    print(f"\nSaved cleaned data to: {CLEANED_PATH}")
    print(f"Saved report to: {REPORT_PATH}")
    
    return df

if __name__ == "__main__":
    clean_transactions()