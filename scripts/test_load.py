import pandas as pd
import os

def load_and_validate_data(filepath):
    df = pd.read_csv(filepath)
    
    print("=" * 50)
    print("DATA VALIDATION REPORT")
    print("=" * 50)
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nColumns:")
    print(df.columns.tolist())
    
    print("\nShape (rows, columns):")
    print(df.shape)
    
    print("\nNull values per column:")
    print(df.isnull().sum())
    
    print("\nData types:")
    print(df.dtypes)
    
    return df

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    transaction_raw = os.path.join(project_root, "data", "raw", "PS_20174392719_1491204439457_log.csv")
    transaction_clean = os.path.join(project_root, "data", "cleaned", "transactions_cleaned.csv")
    customer_raw = os.path.join(project_root, "data", "raw", "customers.csv")
    customer_clean = os.path.join(project_root, "data", "cleaned", "customers_cleaned.csv")
    
    if os.path.exists(transaction_raw):
        print("\n" + "=" * 50)
        print("TRANSACTION DATA (RAW)")
        print("=" * 50)
        load_and_validate_data(transaction_raw)
    
    if os.path.exists(transaction_clean):
        print("\n" + "=" * 50)
        print("TRANSACTION DATA (CLEANED)")
        print("=" * 50)
        df = load_and_validate_data(transaction_clean)
        print("\nHigh-value transactions:", df['is_high_value_transaction'].sum())
        print("Fraud count:", df[df['isFraud'] == 1].shape[0])
    
    if os.path.exists(customer_raw):
        print("\n" + "=" * 50)
        print("CUSTOMER DATA (RAW)")
        print("=" * 50)
        df = load_and_validate_data(customer_raw)
        print("\nRisk category distribution:")
        print(df['risk_category'].value_counts())
    
    if os.path.exists(customer_clean):
        print("\n" + "=" * 50)
        print("CUSTOMER DATA (CLEANED)")
        print("=" * 50)
        df = load_and_validate_data(customer_clean)
        print("\nRisk category distribution:")
        print(df['risk_category'].value_counts())
        print("\nKYC status distribution:")
        print(df['kyc_status'].value_counts())
        print("\nPending KYC count:", df[df['kyc_status'] == 'Pending'].shape[0])
        print("High-risk customers:", df[df['risk_category'] == 'High'].shape[0])