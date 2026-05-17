import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

TRANSACTION_TYPES = ['CASH_IN', 'CASH_OUT', 'PAYMENT', 'TRANSFER', 'DEBIT']

def generate_transactions(n=10000):
    transactions = []
    
    for i in range(n):
        step = random.randint(1, 744)
        trans_type = random.choices(
            TRANSACTION_TYPES,
            weights=[5, 15, 20, 55, 5],
            k=1
        )[0]
        
        amount = round(np.random.exponential(scale=50000), 2)
        
        if random.random() < 0.001:
            amount = round(random.uniform(1000000, 10000000), 2)
        
        name_orig = f"C{b''.join([chr(random.randint(97, 122)) for _ in range(10)])}"
        name_dest = f"C{b''.join([chr(random.randint(97, 122)) for _ in range(10)])}"
        
        oldbalance_org = round(random.uniform(0, 500000), 2) if trans_type != 'CASH_IN' else 0
        
        if trans_type == 'CASH_OUT' or trans_type == 'TRANSFER':
            newbalance_orig = max(0, oldbalance_org - amount)
        elif trans_type == 'CASH_IN':
            newbalance_orig = oldbalance_org + amount
        else:
            newbalance_orig = oldbalance_org - amount
        
        oldbalance_dest = round(random.uniform(0, 500000), 2) if trans_type != 'CASH_OUT' else 0
        
        if trans_type == 'CASH_IN' or trans_type == 'TRANSFER':
            newbalance_dest = oldbalance_dest + amount
        else:
            newbalance_dest = oldbalance_dest
        
        is_fraud = 0
        is_flagged_fraud = 0
        
        if random.random() < 0.001:
            is_fraud = 1
            if amount > 50000:
                is_flagged_fraud = 1
        
        transactions.append({
            'step': step,
            'type': trans_type,
            'amount': amount,
            'nameOrig': name_orig,
            'oldbalanceOrg': oldbalance_org,
            'newbalanceOrig': newbalance_orig,
            'nameDest': name_dest,
            'oldbalanceDest': oldbalance_dest,
            'newbalanceDest': newbalance_dest,
            'isFraud': is_fraud,
            'isFlaggedFraud': is_flagged_fraud
        })
    
    return pd.DataFrame(transactions)

def main():
    df = generate_transactions(10000)
    output_path = 'data/raw/transactions.csv'
    df.to_csv(output_path, index=False)
    
    print("=" * 60)
    print("TRANSACTION DATA GENERATION COMPLETE")
    print("=" * 60)
    print(f"\nGenerated {len(df)} transactions")
    print(f"Saved to: {output_path}")
    print(f"\nFraud distribution:\n{df['isFraud'].value_counts()}")
    print(f"\nTransaction types:\n{df['type'].value_counts()}")

if __name__ == "__main__":
    main()