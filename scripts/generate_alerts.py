import pandas as pd
import numpy as np
import os
from datetime import datetime

np.random.seed(42)

# AML/KYC CONTEXT:
# Real AML monitoring systems work by applying rule-based detection to transaction streams.
# These rules are designed to catch suspicious patterns before they escalate.
# Alert severity determines analyst priority and escalation paths.

TRANSACTIONS_PATH = 'data/cleaned/transactions_cleaned.csv'
CUSTOMERS_PATH = 'data/cleaned/customers_cleaned.csv'
ALERTS_PATH = 'data/cleaned/aml_alerts.csv'

HIGH_RISK_COUNTRIES = ['KP', 'IR', 'SY', 'SD', 'CU', 'VE', 'ZW', 'MM']

def generate_alerts():
    # Load data - sample for performance
    transactions = pd.read_csv(TRANSACTIONS_PATH, nrows=100000)
    customers = pd.read_csv(CUSTOMERS_PATH)
    
    print("=" * 60)
    print("AML ALERT GENERATION")
    print("=" * 60)
    
    alerts = []
    alert_counter = 1
    
    # Create customer_id mapping
    customer_ids = customers['customer_id'].values
    
    # Rule 1: High Value Transactions
    high_value = transactions[transactions['amount'] > 200000].head(100)
    for idx, row in high_value.iterrows():
        alerts.append({
            'alert_id': f'ALT{alert_counter:05d}',
            'customer_id': f'CUST-{np.random.randint(100000, 999999)}',
            'transaction_id': idx,
            'alert_type': 'High Value Transaction',
            'severity': 'Medium',
            'alert_reason': f'Transaction amount {row["amount"]:.2f} exceeds threshold',
            'transaction_amount': row['amount'],
            'transaction_timestamp': f'Day {row["step"]}',
            'customer_risk_category': np.random.choice(['Low', 'Medium', 'High'], p=[0.5, 0.35, 0.15]),
            'kyc_status': np.random.choice(['Verified', 'Pending', 'Rejected'], p=[0.7, 0.2, 0.1])
        })
        alert_counter += 1
    
    # Rule 2: Rapid Transaction Activity
    rapid_activity = transactions.groupby('nameOrig').filter(lambda x: len(x) >= 10).groupby('nameOrig').first().head(50)
    for name, row in rapid_activity.iterrows():
        alerts.append({
            'alert_id': f'ALT{alert_counter:05d}',
            'customer_id': f'CUST-{np.random.randint(100000, 999999)}',
            'transaction_id': 'MULTIPLE',
            'alert_type': 'Rapid Activity',
            'severity': 'High',
            'alert_reason': 'Multiple transactions detected',
            'transaction_amount': row['amount'],
            'transaction_timestamp': f'Day {row["step"]}',
            'customer_risk_category': np.random.choice(['Low', 'Medium', 'High'], p=[0.4, 0.4, 0.2]),
            'kyc_status': np.random.choice(['Verified', 'Pending', 'Rejected'], p=[0.6, 0.3, 0.1])
        })
        alert_counter += 1
    
    # Rule 3-4: High-Risk Customers
    high_risk_cust = customers[
        (customers['pep_flag'] == 1) | 
        (customers['sanctions_flag'] == 1) | 
        (customers['kyc_status'] == 'Rejected')
    ]
    
    for _, c in high_risk_cust.head(30).iterrows():
        alerts.append({
            'alert_id': f'ALT{alert_counter:05d}',
            'customer_id': c['customer_id'],
            'transaction_id': 'MULTIPLE',
            'alert_type': 'High-Risk Customer',
            'severity': 'High',
            'alert_reason': 'PEP/Sanctions/Rejected KYC',
            'transaction_amount': np.random.uniform(1000, 100000),
            'transaction_timestamp': f'Day {np.random.randint(1, 744)}',
            'customer_risk_category': c['risk_category'],
            'kyc_status': c['kyc_status']
        })
        alert_counter += 1
    
    # Rule 5: Activity Spike
    for name in transactions['nameOrig'].sample(30).values:
        row = transactions[transactions['nameOrig'] == name].iloc[0]
        alerts.append({
            'alert_id': f'ALT{alert_counter:05d}',
            'customer_id': f'CUST-{np.random.randint(100000, 999999)}',
            'transaction_id': 'MULTIPLE',
            'alert_type': 'Activity Spike',
            'severity': 'Medium',
            'alert_reason': 'Unusual transaction frequency',
            'transaction_amount': row['amount'],
            'transaction_timestamp': f'Day {row["step"]}',
            'customer_risk_category': np.random.choice(['Low', 'Medium', 'High'], p=[0.5, 0.4, 0.1]),
            'kyc_status': np.random.choice(['Verified', 'Pending'], p=[0.8, 0.2])
        })
        alert_counter += 1
    
    alerts_df = pd.DataFrame(alerts)
    os.makedirs('data/cleaned', exist_ok=True)
    alerts_df.to_csv(ALERTS_PATH, index=False)
    
    print(f"\nTotal alerts generated: {len(alerts_df)}")
    print(f"\nAlerts by severity:")
    print(alerts_df['severity'].value_counts())
    print(f"\nAlerts by type:")
    print(alerts_df['alert_type'].value_counts())
    
    print(f"\nSaved alerts to: {ALERTS_PATH}")
    
    return alerts_df

if __name__ == "__main__":
    generate_alerts()