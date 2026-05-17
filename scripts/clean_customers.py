import pandas as pd
import numpy as np
import os
from datetime import datetime

np.random.seed(42)

RAW_PATH = 'data/raw/customers.csv'
CLEANED_PATH = 'data/cleaned/customers_cleaned.csv'
REPORT_PATH = 'reports/customer_cleaning_report.txt'

HIGH_RISK_COUNTRIES = ['KP', 'IR', 'SY', 'SD', 'CU', 'VE', 'ZW', 'MM']

# AML/KYC CONTEXT:
# Clean customer data is essential for AML compliance because:
# 1. Standardized KYC statuses enable automated monitoring rules
# 2. Age validation prevents identity fraud and KYC bypass
# 3. Country normalization ensures OFAC/sanctions screening accuracy
# 4. KYC risk flags trigger enhanced due diligence workflows

def clean_customers():
    df = pd.read_csv(RAW_PATH)
    rows_before = len(df)
    
    print("=" * 60)
    print("CUSTOMER DATA CLEANING")
    print("=" * 60)
    
    print(f"\nRows before cleaning: {rows_before}")
    
    duplicates_before = df.duplicated(subset=['customer_id']).sum()
    df = df.drop_duplicates(subset=['customer_id'], keep='first')
    print(f"Duplicates removed: {duplicates_before}")
    
    missing_before = df.isnull().sum().sum()
    print(f"Missing values before: {missing_before}")
    
    df = df[df['age'].between(18, 100)]
    
    df['kyc_status'] = df['kyc_status'].str.strip().str.title()
    valid_kyc = ['Verified', 'Pending', 'Expired', 'Rejected']
    df = df[df['kyc_status'].isin(valid_kyc)]
    
    df['risk_category'] = df['risk_category'].str.strip().str.title()
    valid_risk = ['Low', 'Medium', 'High']
    df = df[df['risk_category'].isin(valid_risk)]
    
    df['country'] = df['country'].str.strip().str.upper()
    
    df['email'] = df['email'].str.strip()
    df['phone_number'] = df['phone_number'].astype(str).str.strip()
    
    df['customer_age_group'] = pd.cut(
        df['age'],
        bins=[0, 25, 45, 65, 100],
        labels=['18-25', '26-45', '46-65', '65+']
    )
    
    df['kyc_risk_flag'] = df['kyc_status'].apply(
        lambda x: 1 if x in ['Pending', 'Rejected'] else 0
    )
    
    rows_after = len(df)
    
    os.makedirs('data/cleaned', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    df.to_csv(CLEANED_PATH, index=False)
    
    pending_kyc = df[df['kyc_status'] == 'Pending'].shape[0]
    high_risk = df[df['risk_category'] == 'High'].shape[0]
    high_risk_countries_active = df[df['country'].isin(HIGH_RISK_COUNTRIES)].shape[0]
    
    print(f"\nPending KYC customers: {pending_kyc}")
    print(f"High-risk customers: {high_risk}")
    print(f"High-risk country customers: {high_risk_countries_active}")
    
    report = f"""Customer Cleaning Report
Generated: {datetime.now()}

Rows before cleaning: {rows_before}
Rows after cleaning: {rows_after}
Rows removed: {rows_before - rows_after}
Duplicates removed: {duplicates_before}

KYC Status Distribution:
{df['kyc_status'].value_counts().to_string()}

Risk Category Distribution:
{df['risk_category'].value_counts().to_string()}

High-risk country customers: {high_risk_countries_active}
"""
    
    with open(REPORT_PATH, 'w') as f:
        f.write(report)
    
    print(f"\nSaved cleaned data to: {CLEANED_PATH}")
    print(f"Saved report to: {REPORT_PATH}")
    
    return df

if __name__ == "__main__":
    clean_customers()