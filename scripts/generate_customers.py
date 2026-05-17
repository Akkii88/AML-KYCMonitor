import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

np.random.seed(42)
random.seed(42)

HIGH_RISK_COUNTRIES = ['KP', 'IR', 'SY', 'SD', 'CU', 'VE', 'ZW', 'MM']
MEDIUM_RISK_COUNTRIES = ['NG', 'PK', 'AF', 'IQ', 'JO', 'LB', 'MA', 'SA', 'EG', 'UA']
LOW_RISK_COUNTRIES = ['US', 'GB', 'CA', 'AU', 'DE', 'FR', 'JP', 'SG', 'NL', 'CH']

# AML/KYC CONTEXT:
# KYC (Know Your Customer) data is fundamental for AML compliance
# AML analysts use customer risk profiles to:
# 1. Prioritize high-risk customers for enhanced due diligence (EDD)
# 2. Monitor transaction patterns against customer risk levels
# 3. Investigate suspicious activity reports (SARs)
# 4. Conduct periodic customer risk reassessments
#
# PEP (Politically Exposed Persons) flags identify individuals in prominent positions
# who pose higher corruption and money laundering risk per FATF recommendations
# Sanctions flags identify customers on OFAC, UN, EU watchlists - legally blocked transactions

def generate_customers(n=1000):
    customers = []
    
    for i in range(n):
        customer_id = f"CUST-{random.randint(100000, 999999)}"
        full_name = fake.name()
        age = random.randint(18, 85)
        gender = random.choice(['Male', 'Female', 'Other'])
        country = random.choices(
            HIGH_RISK_COUNTRIES + MEDIUM_RISK_COUNTRIES + LOW_RISK_COUNTRIES,
            weights=[1]*len(HIGH_RISK_COUNTRIES) + [3]*len(MEDIUM_RISK_COUNTRIES) + [15]*len(LOW_RISK_COUNTRIES),
            k=1
        )[0]
        city = fake.city()
        occupation = fake.job()
        annual_income = int(np.random.lognormal(mean=10, sigma=0.7))
        account_age_days = random.randint(1, 3650)
        kyc_status = random.choices(
            ['Verified', 'Pending', 'Expired', 'Rejected'],
            weights=[70, 15, 10, 5]
        )[0]
        pep_flag = random.choices([0, 1], weights=[97, 3])[0]
        sanctions_flag = random.choices([0, 1], weights=[99.5, 0.5])[0]
        
        onboarding_date = datetime.now() - timedelta(days=account_age_days)
        
        if kyc_status == 'Pending':
            risk_score = random.randint(6, 9)
        elif pep_flag == 1:
            risk_score = random.randint(7, 10)
        elif sanctions_flag == 1:
            risk_score = 10
        elif country in HIGH_RISK_COUNTRIES:
            risk_score = random.randint(6, 8)
        elif country in MEDIUM_RISK_COUNTRIES:
            risk_score = random.randint(4, 7)
        else:
            risk_score = random.randint(1, 5)
        
        if risk_score >= 8:
            risk_category = 'High'
        elif risk_score >= 5:
            risk_category = 'Medium'
        else:
            risk_category = 'Low'
        
        email = fake.email() if random.random() > 0.02 else None
        phone_number = fake.phone_number() if random.random() > 0.03 else None
        
        if random.random() < 0.01:
            full_name = full_name.upper()
        if random.random() < 0.005:
            customer_id = customer_id.replace('-', '')
        
        customers.append({
            'customer_id': customer_id,
            'full_name': full_name,
            'age': age,
            'gender': gender,
            'country': country,
            'city': city,
            'occupation': occupation,
            'annual_income': annual_income,
            'account_age_days': account_age_days,
            'kyc_status': kyc_status,
            'pep_flag': pep_flag,
            'sanctions_flag': sanctions_flag,
            'onboarding_date': onboarding_date.strftime('%Y-%m-%d'),
            'risk_category': risk_category,
            'email': email,
            'phone_number': phone_number
        })
    
    return pd.DataFrame(customers)

def add_data_quality_issues(df):
    indices = df.sample(frac=0.02, random_state=42).index
    for idx in indices:
        df.loc[idx, 'annual_income'] = None
        df.loc[idx, 'email'] = None
        df.loc[idx, 'phone_number'] = None
    
    return df

def main():
    df = generate_customers(1000)
    df = add_data_quality_issues(df)
    
    output_path = 'data/raw/customers.csv'
    df.to_csv(output_path, index=False)
    
    print("=" * 60)
    print("CUSTOMER DATA GENERATION COMPLETE")
    print("=" * 60)
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nDataset shape:")
    print(df.shape)
    
    print("\nMissing values per column:")
    print(df.isnull().sum())
    
    print("\nRisk category distribution:")
    print(df['risk_category'].value_counts())
    
    print("\nKYC status distribution:")
    print(df['kyc_status'].value_counts())
    
    print(f"\nSaved to: {output_path}")

if __name__ == "__main__":
    main()