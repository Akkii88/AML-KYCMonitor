import pandas as pd
import numpy as np
import os
from datetime import datetime

np.random.seed(42)

# AML/KYC CONTEXT:
# AML analysts investigate alerts by analyzing customer behavior against their risk profile.
# Investigations consider: source of funds, transaction patterns, geography, and KYC compliance.
# Recommendations are documented in case management systems for audit trails.

ALERTS_PATH = 'data/cleaned/aml_alerts.csv'
CUSTOMERS_PATH = 'data/cleaned/customers_cleaned.csv'
INVESTIGATIONS_PATH = 'data/cleaned/investigation_cases.csv'

def investigate_alerts():
    alerts = pd.read_csv(ALERTS_PATH)
    customers = pd.read_csv(CUSTOMERS_PATH)
    
    print("=" * 60)
    print("AML INVESTIGATION WORKFLOW")
    print("=" * 60)
    
    investigations = []
    case_counter = 1000
    
    findings_templates = {
        'High Value Transaction': [
            'Transaction amount inconsistent with customer income profile',
            'Large transfer may require source of funds verification',
            'No historical precedent for transaction size'
        ],
        'High-Risk Customer': [
            'PEP customer requires enhanced monitoring per FATF guidelines',
            'Sanctions flag requires OFAC verification',
            'Rejected KYC customer conducting suspicious activity'
        ],
        'Activity Spike': [
            'Rapid transaction pattern may indicate structuring behavior',
            'Unusual frequency compared to customer baseline',
            'Multiple transactions in short timeframe raises concern'
        ],
        'Rapid Activity': [
            'Multiple transactions may indicate structuring attempts',
            'Pattern consistent with cash structuring under threshold',
            'Requires enhanced due diligence verification'
        ]
    }
    
    recommendations = {
        'High Value Transaction': ['Enhanced Due Diligence Required', 'Monitor Activity', 'False Positive'],
        'High-Risk Customer': ['Escalate for Review', 'Monitor Activity', 'Temporary Hold Recommended'],
        'Activity Spike': ['Enhanced Due Diligence Required', 'Escalate for Review', 'Monitor Activity'],
        'Rapid Activity': ['Escalate for Review', 'Enhanced Due Diligence Required', 'Temporary Hold Recommended']
    }
    
    for _, alert in alerts.iterrows():
        alert_type = alert['alert_type']
        severity = alert['severity']
        
        finding = np.random.choice(findings_templates.get(alert_type, ['Requires review']))
        recommendation = np.random.choice(recommendations.get(alert_type, ['Monitor Activity']))
        
        if severity == 'High' or recommendation == 'Escalate for Review':
            escalation = 'Yes'
            analyst_decision = np.random.choice(['Review Required', 'Escalate to Senior Analyst', 'Enhanced Due Diligence'])
            status = 'Open'
        else:
            escalation = 'No'
            analyst_decision = 'Monitor'
            status = 'Closed'
        
        investigations.append({
            'case_id': f'CASE{case_counter}',
            'alert_id': alert['alert_id'],
            'customer_id': alert['customer_id'],
            'investigation_findings': finding,
            'recommendation': recommendation,
            'analyst_decision': analyst_decision,
            'investigation_status': status,
            'risk_level': severity,
            'escalation_required': escalation
        })
        case_counter += 1
    
    investigations_df = pd.DataFrame(investigations)
    investigations_df.to_csv(INVESTIGATIONS_PATH, index=False)
    
    print(f"\nTotal investigated cases: {len(investigations_df)}")
    print(f"\nEscalated cases: {(investigations_df['escalation_required'] == 'Yes').sum()}")
    print(f"False positives: {(investigations_df['analyst_decision'] == 'False Positive').sum()}")
    print(f"Enhanced Due Diligence: {(investigations_df['recommendation'] == 'Enhanced Due Diligence Required').sum()}")
    
    print(f"\nRisk distribution:")
    print(investigations_df['risk_level'].value_counts())
    
    print(f"\nRecommendations breakdown:")
    print(investigations_df['recommendation'].value_counts())
    
    print(f"\nSaved investigations to: {INVESTIGATIONS_PATH}")
    
    return investigations_df

if __name__ == "__main__":
    investigate_alerts()