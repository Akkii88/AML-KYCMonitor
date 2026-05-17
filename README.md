# AML & KYC Risk Monitoring Analysis

**A comprehensive simulation of Anti-Money Laundering (AML) and Know Your Customer (KYC) compliance workflows used in banking and financial institutions.**

---

## Project Overview

This project simulates the end-to-end AML monitoring and compliance operations workflow used by banks, fintech companies, and Big 4 risk advisory teams. It demonstrates how financial institutions detect suspicious activity, investigate alerts, manage escalations, and report compliance metrics to leadership.

The project replicates real-world processes including:

- Transaction monitoring and suspicious activity detection
- Customer risk profiling and KYC verification
- AML alert generation and triage
- Analyst investigation workflows
- Escalation management and enhanced due diligence
- Compliance reporting and executive dashboards

### Dashboard Preview

**Streamlit AML Analyst Dashboard**
![Streamlit Dashboard](./Dashboards/Streamlit/Screenshot%202026-05-18%20at%203.38.16%20AM.png)

**Excel Executive MIS Dashboard**
![Excel Dashboard](./Dashboards/Excel/Screenshot%202026-05-18%20at%203.41.18%20AM.png)

---

## Business Objective

The primary objective was to build a realistic AML operations simulation that mirrors the daily responsibilities of compliance and risk analysts. This includes:

- Generating rule-based alerts for suspicious transactions
- Simulating customer onboarding and KYC risk assessment
- Modeling investigation and escalation processes
- Producing management-ready compliance reports
- Creating analyst dashboards for monitoring and decision-making

This project serves as a practical demonstration of AML monitoring capabilities relevant to roles in:

- AML/Financial Crime teams in banks and fintechs
- Risk and Compliance advisory at Big 4 firms
- Regulatory reporting and audit support functions

---

## Industry Context

In real financial institutions, AML operations follow a structured lifecycle:

1. **Transaction Monitoring Systems** continuously scan customer activity against predefined rules (high-value transfers, rapid transaction patterns, high-risk geographies).

2. **Alerts** are generated when transactions or customer behaviors deviate from expected norms. These alerts enter a queue for analyst review.

3. **KYC Analysts** assess customer risk profiles using onboarding data, PEP (Politically Exposed Person) flags, sanctions screening, and geographic exposure.

4. **Investigations** involve reviewing transaction history, customer documentation, and risk indicators to determine whether activity is legitimate or suspicious.

5. **Escalations** occur when cases require senior review, enhanced due diligence, or potential Suspicious Activity Report (SAR) filing.

6. **Management Reporting** provides leadership with visibility into alert volumes, escalation trends, high-risk customer segments, and KYC compliance gaps.

This project replicates each stage of this operational lifecycle using realistic data and analyst-style decision logic.

---

## End-to-End AML Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    CUSTOMER ONBOARDING                      │
│         (KYC Verification • Risk Scoring • PEP Screening)   │
└─────────────────────────────┬───────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 TRANSACTION MONITORING                      │
│      (Rule-Based Detection • High-Value • Rapid Activity)   │
└─────────────────────────────┬───────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   AML ALERT GENERATION                      │
│         (High-Risk Customers • Geography • Structuring)     │
└─────────────────────────────┬───────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    ALERT INVESTIGATION                      │
│    (Transaction Review • Customer Profile Analysis • EDD)   │
└─────────────────────────────┬───────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              ESCALATION & DOCUMENTATION                     │
│         (Case Management • Findings • Recommendations)      │
└─────────────────────────────┬───────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  COMPLIANCE REPORTING                       │
│        (Excel Workbooks • Word Reports • Audit Trail)       │
└─────────────────────────────┬───────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   EXECUTIVE DASHBOARD                       │
│      (KPI Tracking • Trend Analysis • Management Reporting) │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Transaction Monitoring** | Rule-based detection of high-value transfers, rapid activity patterns, and unusual transaction volumes |
| **AML Alert Generation** | Automated flagging of suspicious activity using severity-based classification (High/Medium) |
| **KYC Risk Analysis** | Customer risk categorization based on PEP status, sanctions flags, geography, and KYC completeness |
| **Investigation Workflow** | Simulation of analyst case review with findings documentation and recommendation logic |
| **Escalation Management** | Tracking of cases requiring senior review, enhanced due diligence, or temporary holds |
| **Excel Investigation Workbook** | Multi-sheet compliance tracker with alert queue, investigation logs, and escalation summaries |
| **Word Compliance Report** | Professional investigation summary with executive findings and recommendations |
| **Streamlit Dashboard** | Interactive AML monitoring portal with KPI cards, charts, and risk tables |

---

## Analyst Responsibilities Simulated

This project replicates core responsibilities performed daily by AML and KYC analysts:

- **Alert Triage**: Reviewing generated alerts to assess legitimacy versus suspicious activity
- **Customer Risk Assessment**: Analyzing KYC status, PEP exposure, sanctions flags, and geographic risk
- **Transaction Pattern Analysis**: Identifying structuring behavior, rapid activity, and high-value inconsistencies
- **Case Documentation**: Recording investigation findings, recommendations, and escalation decisions
- **Enhanced Due Diligence**: Flagging accounts requiring additional scrutiny or source-of-funds verification
- **Escalation Preparation**: Preparing cases for senior analyst or compliance officer review
- **Compliance Reporting**: Generating summary reports for management and audit purposes
- **High-Risk Customer Monitoring**: Tracking PEP and sanctions-flagged customers for ongoing activity

---

## Dashboard & Reporting Outputs

### Interactive Dashboard (Streamlit)
- Executive KPI overview with real-time metrics
- Alert monitoring by type and severity
- KYC risk distribution and customer segmentation
- Investigation analytics and escalation tracking
- Top flagged customers and high-risk geography tables

### Excel Management Information System
- **Executive Dashboard**: KPI cards and 5 professional charts
- **Alert Queue**: Active suspicious activity alerts
- **Investigation Tracker**: Analyst case notes and decisions
- **High-Risk Customers**: PEP, sanctions, and elevated-risk profiles
- **Escalation Summary**: Management escalation metrics
- **KYC Review**: Pending and incomplete customer verification status
- **Suspicious Transactions**: High-value and pattern-based flagged activity

### Compliance Documentation
- Professional Word investigation report with findings and recommendations
- Audit-ready formatting with clear sections and executive summary

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Data Processing | Python, Pandas, NumPy |
| Synthetic Data Generation | Faker |
| Visualization | Plotly, Matplotlib |
| Dashboard | Streamlit |
| Excel Reporting | OpenPyXL |
| Word Reporting | python-docx |
| Data Storage | CSV (simulation of database exports) |

---

## Project Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Raw Data   │────▶│ Data Cleaning│────▶│ Alert Engine │
│  (Transactions│     │ & Validation │     │  (Rule-Based) │
│   + KYC)     │     │              │     │              │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                 │
┌──────────────┐     ┌──────────────┐     ┌──────▼───────┐
│  Dashboards  │◀────│   Reporting  │◀────│ Investigation│
│ (Streamlit + │     │  (Excel/Word)│     │   Workflow   │
│   Excel)     │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

**Workflow Layers:**
1. **Data Ingestion**: PaySim transaction logs + synthetic KYC profiles
2. **Data Cleaning**: Standardization, null handling, derived field creation
3. **Alert Generation**: Rule-based detection of suspicious patterns
4. **Investigation Processing**: Analyst review simulation with findings and recommendations
5. **Reporting**: Excel workbooks, Word reports, and visual dashboards
6. **Visualization**: Interactive Streamlit portal and static MIS charts

---

## Dataset Information

| Dataset | Source | Records | Purpose |
|---------|--------|---------|---------|
| **Transactions** | PaySim (Kaggle) | 6,362,620 | Mobile money transaction logs with fraud labels |
| **Customers** | Synthetic (Faker) | 999 | KYC profiles with risk attributes, PEP flags, sanctions status |

**Transaction Features**: step, type, amount, origin/destination accounts, balances, fraud indicators

**Customer Features**: customer_id, demographics, country, income, KYC status, PEP flag, sanctions flag, risk category, onboarding date

---

## Key Risk Insights

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Total Alerts Generated | 160 | Suspicious activity flagged for review |
| Escalated Investigations | 37 | Cases requiring senior analyst attention |
| High-Risk Customers | 123 | Elevated monitoring required |
| Pending KYC Customers | 161 | Compliance remediation needed |
| Fraudulent Transactions | 8,213 | Confirmed fraud within dataset |
| PEP Customers | 28 | Politically Exposed Persons under enhanced scrutiny |
| Sanctions-Flagged | 7 | OFAC/UN watchlist matches requiring blocking review |
| High-Value Transactions | 1,673,570 | Activity exceeding 200,000 threshold |

**Key Observations:**
- High-value transaction alerts represent the largest alert category, indicating need for source-of-funds verification processes
- 23% of alerts (37/160) required escalation, reflecting appropriate risk triage sensitivity
- Pending KYC exposure (161 customers) represents a material compliance gap requiring immediate remediation

---

## Screenshots

### Streamlit AML Analyst Dashboard

| View | Description | Screenshot |
|------|-------------|------------|
| Executive Overview | KPI cards and high-level metrics | ![Streamlit 1](./Dashboards/Streamlit/Screenshot%202026-05-18%20at%203.38.16%20AM.png) |
| AML Monitoring | Alert analytics and activity patterns | ![Streamlit 2](./Dashboards/Streamlit/Screenshot%202026-05-18%20at%203.38.28%20AM.png) |
| KYC Risk Analysis | Customer risk distribution and profiles | ![Streamlit 3](./Dashboards/Streamlit/Screenshot%202026-05-18%20at%203.38.38%20AM.png) |
| Investigation Metrics | Escalation and outcome tracking | ![Streamlit 4](./Dashboards/Streamlit/Screenshot%202026-05-18%20at%203.39.05%20AM.png) |

### Excel Executive Dashboard & MIS Reporting

| View | Description | Screenshot |
|------|-------------|------------|
| Main Dashboard | KPI summary with professional charts | ![Excel 1](./Dashboards/Excel/Screenshot%202026-05-18%20at%203.41.18%20AM.png) |
| Alert Analysis | Severity and type breakdown | ![Excel 2](./Dashboards/Excel/Screenshot%202026-05-18%20at%203.41.43%20AM.png) |
| KYC & Escalations | Status distribution and summary | ![Excel 3](./Dashboards/Excel/Screenshot%202026-05-18%20at%203.42.19%20AM.png) |
| Geography Risk | High-risk country activity | ![Excel 4](./Dashboards/Excel/Screenshot%202026-05-18%20at%203.42.27%20AM.png) |
| Investigation Tracker | Case management and findings | ![Excel 5](./Dashboards/Excel/Screenshot%202026-05-18%20at%203.44.13%20AM.png) |
| High-Risk Monitoring | PEP and sanctions customer view | ![Excel 6](./Dashboards/Excel/Screenshot%202026-05-18%20at%203.44.38%20AM.png) |

---

## Project Folder Structure

```
AML_KYC_Risk_Monitoring/
│
├── data/
│   ├── raw/
│   │   └── PS_20174392719_1491204439457_log.csv    # PaySim transactions
│   └── cleaned/
│       ├── transactions_cleaned.csv
│       ├── customers_cleaned.csv
│       ├── aml_alerts.csv
│       └── investigation_cases.csv
│
├── reports/
│   ├── dashboard_data/           # Aggregated KPI tables for visualization
│   ├── visuals/                  # Chart images
│   ├── AML_Investigation_Workbook.xlsx
│   ├── AML_Investigation_Report.docx
│   └── executive_summary.txt
│
├── scripts/
│   ├── generate_customers.py
│   ├── clean_transactions.py
│   ├── clean_customers.py
│   ├── generate_alerts.py
│   ├── investigate_alerts.py
│   ├── generate_risk_reports.py
│   ├── prepare_dashboard_data.py
│   └── generate_aml_documents.py
│
├── app.py                        # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1. Clone and Setup Environment

```bash
git clone <repository-url>
cd AML_KYC_Risk_Monitoring

python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

### 4. Generate Reports (Optional)

```bash
python scripts/generate_aml_documents.py
```

This regenerates the Excel investigation workbook and Word compliance report.

---

## Future Improvements

- **Machine Learning Integration**: Anomaly detection models for unsupervised suspicious activity identification
- **Real-Time Monitoring**: Streaming transaction ingestion with live alert generation
- **Database Backend**: Migration from CSV to PostgreSQL/MySQL for production-scale data
- **SAR Automation**: Template generation for Suspicious Activity Report filing
- **Role-Based Access**: Multi-user dashboard with analyst, manager, and auditor views
- **Geographic Heatmaps**: Interactive risk exposure visualization by country/region
- **Alert Tuning Simulator**: Rule parameter adjustment with impact analysis on alert volumes

---

## Conclusion

This project demonstrates a comprehensive understanding of AML monitoring operations, KYC compliance workflows, investigation analytics, and regulatory reporting processes used in financial services. By simulating the full lifecycle from transaction monitoring through escalation and executive reporting, it provides a practical foundation for roles in financial crime prevention, risk advisory, and compliance analytics.

The deliverables—including rule-based alert engines, investigation trackers, professional Excel MIS dashboards, and interactive analyst portals—reflect the operational tools and documentation standards expected in banking AML teams and Big 4 risk consulting practices.

---

*This project was developed as a portfolio demonstration of AML/KYC operations and compliance analytics capabilities.*