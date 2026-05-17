import pandas as pd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(42)

# AML/KYC CONTEXT:
# AML reporting supports compliance teams by providing:
# 1. Management oversight of monitoring effectiveness
# 2. Trend analysis for suspicious activity patterns
# 3. Audit trails for regulatory examinations
# 4. Resource allocation for investigations

CUSTOMERS_PATH = 'data/cleaned/customers_cleaned.csv'
TRANSACTIONS_PATH = 'data/cleaned/transactions_cleaned.csv'
ALERTS_PATH = 'data/cleaned/aml_alerts.csv'
INVESTIGATIONS_PATH = 'data/cleaned/investigation_cases.csv'

def generate_reports():
    customers = pd.read_csv(CUSTOMERS_PATH)
    alerts = pd.read_csv(ALERTS_PATH)
    investigations = pd.read_csv(INVESTIGATIONS_PATH)
    
    print("=" * 60)
    print("AML RISK REPORTING")
    print("=" * 60)
    
    os.makedirs('reports/visuals', exist_ok=True)
    
    # Alert Summary
    alert_summary = alerts.groupby(['alert_type', 'severity']).size().reset_index(name='count')
    alert_summary.to_csv('reports/alert_summary.csv', index=False)
    
    # Customer Risk Summary
    customer_risk = customers.groupby('risk_category').agg({
        'customer_id': 'count',
        'pep_flag': 'sum',
        'sanctions_flag': 'sum',
        'kyc_status': lambda x: (x == 'Pending').sum()
    }).reset_index()
    customer_risk.columns = ['risk_category', 'customer_count', 'pep_customers', 'sanctions_customers', 'pending_kyc']
    customer_risk.to_csv('reports/customer_risk_summary.csv', index=False)
    
    # Escalation Summary
    escalations = investigations[investigations['escalation_required'] == 'Yes']
    escalation_summary = escalations.groupby(['risk_level', 'recommendation']).size().reset_index(name='count')
    escalation_summary.to_csv('reports/escalation_summary.csv', index=False)
    
    # PEP Monitoring Report
    pep_customers = customers[customers['pep_flag'] == 1]
    pep_alerts = alerts.merge(pep_customers, on='customer_id', how='inner')
    pep_report = pep_alerts.groupby('alert_type').size().reset_index(name='count')
    pep_report.to_csv('reports/pep_monitoring_report.csv', index=False)
    
    # High-Risk Geographies
    high_risk_countries = ['KP', 'IR', 'SY', 'SD', 'CU', 'VE', 'ZW', 'MM']
    hr_geo = customers[customers['country'].isin(high_risk_countries)]
    hr_geo_summary = hr_geo.groupby('country').size().reset_index(name='customer_count')
    hr_geo_summary.to_csv('reports/high_risk_geographies.csv', index=False)
    
    # Visualizations
    plt.figure(figsize=(10, 6))
    alert_summary.pivot(index='alert_type', columns='severity', values='count').plot(kind='bar')
    plt.title('Alerts by Type and Severity')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('reports/visuals/alert_distribution.png')
    plt.close()
    
    plt.figure(figsize=(8, 6))
    customers['risk_category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Customer Risk Distribution')
    plt.ylabel('')
    plt.savefig('reports/visuals/risk_distribution.png')
    plt.close()
    
    print(f"\nAlerts by type:")
    print(alerts['alert_type'].value_counts())
    print(f"\nEscalations: {len(escalations)}")
    print(f"High-risk countries represented: {hr_geo_summary.shape[0]}")
    
    # Executive Summary
    exec_summary = f"""AML Executive Summary Report
Generated: {pd.Timestamp.now()}

=== OVERVIEW ===
Total Alerts Generated: {len(alerts)}
Total Investigations Completed: {len(investigations)}
Escalated Cases: {len(escalations)}
Enhanced Due Diligence Cases: {(investigations['recommendation'] == 'Enhanced Due Diligence Required').sum()}

=== KEY FINDINGS ===
Alert Types:
{alerts['alert_type'].value_counts().to_string()}

Risk Distribution:
{customers['risk_category'].value_counts().to_string()}

Suspicious Activity Trends:
- High-value transactions require source of funds verification
- PEP customers under enhanced monitoring
- Activity spikes indicate potential structuring behavior

High-Risk Customer Exposure:
- PEP customers: {customers['pep_flag'].sum()}
- Sanctions-flagged: {customers['sanctions_flag'].sum()}
- Pending KYC: {customers['kyc_status'].value_counts().get('Pending', 0)}

Escalation Metrics:
- Escalated investigations: {len(escalations)}
- Recommendation breakdown:
{investigations['recommendation'].value_counts().to_string()}

Geography Risk:
- High-risk country customers: {hr_geo.shape[0]}
"""
    
    with open('reports/executive_summary.txt', 'w') as f:
        f.write(exec_summary)
    
    print(f"\nReports saved to reports/")

if __name__ == "__main__":
    generate_reports()