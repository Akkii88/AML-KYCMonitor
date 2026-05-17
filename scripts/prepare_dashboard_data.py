import pandas as pd
import numpy as np
import os

np.random.seed(42)

# AML/KYC CONTEXT:
# Dashboard datasets aggregate complex transaction/investigation data into digestible metrics.
# These tables feed Power BI/Tableau dashboards for real-time compliance monitoring.
# KPIs enable management to track AML program effectiveness over time.

TRANSACTIONS_PATH = 'data/cleaned/transactions_cleaned.csv'
CUSTOMERS_PATH = 'data/cleaned/customers_cleaned.csv'
ALERTS_PATH = 'data/cleaned/aml_alerts.csv'
INVESTIGATIONS_PATH = 'data/cleaned/investigation_cases.csv'

def prepare_dashboard_data():
    transactions = pd.read_csv(TRANSACTIONS_PATH)
    customers = pd.read_csv(CUSTOMERS_PATH)
    alerts = pd.read_csv(ALERTS_PATH)
    investigations = pd.read_csv(INVESTIGATIONS_PATH)
    
    print("=" * 60)
    print("DASHBOARD DATA PREPARATION")
    print("=" * 60)
    
    os.makedirs('reports/dashboard_data', exist_ok=True)
    
    # KPI Summary
    kpi_summary = pd.DataFrame([{
        'total_transactions': len(transactions),
        'total_customers': len(customers),
        'total_alerts': len(alerts),
        'escalated_cases': len(investigations[investigations['escalation_required'] == 'Yes']),
        'high_risk_customers': len(customers[customers['risk_category'] == 'High']),
        'fraudulent_transactions': int(transactions['isFraud'].sum()),
        'pending_kyc_customers': len(customers[customers['kyc_status'] == 'Pending']),
        'pep_customers': int(customers['pep_flag'].sum()),
        'sanctions_customers': int(customers['sanctions_flag'].sum())
    }])
    kpi_summary.to_csv('reports/dashboard_data/kpi_summary.csv', index=False)
    
    # Alert Analytics
    alerts_by_type = alerts.groupby('alert_type').size().reset_index(name='count')
    alerts_by_type.to_csv('reports/dashboard_data/alerts_by_type.csv', index=False)
    
    alerts_by_severity = alerts.groupby('severity').size().reset_index(name='count')
    alerts_by_severity.to_csv('reports/dashboard_data/alerts_by_severity.csv', index=False)
    
    # Customer Risk Tables
    risk_cat_dist = customers['risk_category'].value_counts().reset_index()
    risk_cat_dist.columns = ['risk_category', 'count']
    risk_cat_dist.to_csv('reports/dashboard_data/risk_category_distribution.csv', index=False)
    
    kyc_status_dist = customers['kyc_status'].value_counts().reset_index()
    kyc_status_dist.columns = ['kyc_status', 'count']
    kyc_status_dist.to_csv('reports/dashboard_data/kyc_status_distribution.csv', index=False)
    
    # Investigation Analytics
    investigation_outcomes = investigations.groupby('investigation_status').size().reset_index(name='count')
    investigation_outcomes.to_csv('reports/dashboard_data/investigation_outcomes.csv', index=False)
    
    recommendation_summary = investigations['recommendation'].value_counts().reset_index()
    recommendation_summary.columns = ['recommendation', 'count']
    recommendation_summary.to_csv('reports/dashboard_data/recommendation_summary.csv', index=False)
    
    # Top Risk Tables
    top_flagged = investigations['customer_id'].value_counts().head(10).reset_index()
    top_flagged.columns = ['customer_id', 'flag_count']
    top_flagged.to_csv('reports/dashboard_data/top_flagged_customers.csv', index=False)
    
    escalation_dist = investigations['risk_level'].value_counts().reset_index()
    escalation_dist.columns = ['risk_level', 'count']
    escalation_dist.to_csv('reports/dashboard_data/escalation_distribution.csv', index=False)
    
    # Hourly Activity
    hourly_activity = transactions.groupby('transaction_hour').size().reset_index(name='transaction_count')
    hourly_activity.to_csv('reports/dashboard_data/hourly_transaction_activity.csv', index=False)
    
    # Additional tables for Streamlit dashboard
    # PEP and Sanctions summaries
    pep_summary = customers[customers['pep_flag'] == 1][['customer_id', 'country', 'risk_category', 'kyc_status']].head(20)
    pep_summary.to_csv('reports/dashboard_data/pep_customer_summary.csv', index=False)
    
    sanctions_summary = customers[customers['sanctions_flag'] == 1][['customer_id', 'country', 'risk_category']].head(20)
    sanctions_summary.to_csv('reports/dashboard_data/sanctions_summary.csv', index=False)
    
    # High-risk geographies
    high_risk_countries = ['KP', 'IR', 'SY', 'SD', 'CU', 'VE', 'ZW', 'MM']
    hr_geo = customers[customers['country'].isin(high_risk_countries)].groupby('country').size().reset_index(name='customer_count')
    hr_geo.to_csv('reports/dashboard_data/high_risk_geographies.csv', index=False)
    
    # Top high-value transactions
    top_txn = transactions[transactions['amount'] > 200000].nlargest(20, 'amount')[['step', 'type', 'amount', 'nameOrig']]
    top_txn.columns = ['day', 'transaction_type', 'amount', 'customer_id']
    top_txn.to_csv('reports/dashboard_data/top_high_value_transactions.csv', index=False)
    
    print("Dashboard tables created:")
    print("  - kpi_summary.csv")
    print("  - alerts_by_type.csv, alerts_by_severity.csv")
    print("  - risk_category_distribution.csv, kyc_status_distribution.csv")
    print("  - investigation_outcomes.csv, recommendation_summary.csv")
    print("  - top_flagged_customers.csv, escalation_distribution.csv")
    print("  - hourly_transaction_activity.csv")
    print("  - pep_customer_summary.csv, sanctions_summary.csv")
    print("  - high_risk_geographies.csv, top_high_value_transactions.csv")
    
    print(f"\nKPI Summary:")
    print(kpi_summary.to_string(index=False))

if __name__ == "__main__":
    prepare_dashboard_data()