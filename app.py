import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# AML/KYC CONTEXT:
# AML dashboards provide real-time monitoring for compliance teams.
# Analysts use these tools to track suspicious activity, investigate alerts, and report to management.
# Clean, professional interfaces reduce cognitive load during high-pressure investigations.

st.set_page_config(page_title="AML Analyst Dashboard", layout="wide", initial_sidebar_state="expanded")

# Load dashboard data
@st.cache_data
def load_data():
    data_dir = Path('reports/dashboard_data')
    return {
        'kpi': pd.read_csv(data_dir / 'kpi_summary.csv'),
        'alerts_type': pd.read_csv(data_dir / 'alerts_by_type.csv'),
        'alerts_severity': pd.read_csv(data_dir / 'alerts_by_severity.csv'),
        'risk_dist': pd.read_csv(data_dir / 'risk_category_distribution.csv'),
        'kyc_dist': pd.read_csv(data_dir / 'kyc_status_distribution.csv'),
        'escalation': pd.read_csv(data_dir / 'escalation_distribution.csv'),
        'outcomes': pd.read_csv(data_dir / 'investigation_outcomes.csv'),
        'recommendations': pd.read_csv(data_dir / 'recommendation_summary.csv'),
        'top_customers': pd.read_csv(data_dir / 'top_flagged_customers.csv'),
        'hr_geo': pd.read_csv(data_dir / 'high_risk_geographies.csv'),
        'top_txn': pd.read_csv(data_dir / 'top_high_value_transactions.csv'),
        'hourly': pd.read_csv(data_dir / 'hourly_transaction_activity.csv'),
        'pep': pd.read_csv(data_dir / 'pep_customer_summary.csv'),
        'sanctions': pd.read_csv(data_dir / 'sanctions_summary.csv')
    }

data = load_data()
kpi = data['kpi'].iloc[0]

# Sidebar
st.sidebar.title("AML Monitoring Portal")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["Executive Overview", "AML Monitoring", "KYC Risk Analysis", "Investigation Analytics", "Top Risk Tables"])

# Header
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>AML Analyst Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7F8C8D;'>Anti-Money Laundering Monitoring & Compliance</p>", unsafe_allow_html=True)

if page == "Executive Overview":
    st.markdown("### Key Performance Indicators")
    cols = st.columns(4)
    with cols[0]:
        st.metric("Total Transactions", f"{kpi['total_transactions']:,}")
    with cols[1]:
        st.metric("Total Alerts", f"{kpi['total_alerts']:,}")
    with cols[2]:
        st.metric("Escalated Cases", f"{kpi['escalated_cases']:,}")
    with cols[3]:
        st.metric("High-Risk Customers", f"{kpi['high_risk_customers']:,}")
    
    cols2 = st.columns(4)
    with cols2[0]:
        st.metric("Fraudulent Transactions", f"{kpi['fraudulent_transactions']:,}")
    with cols2[1]:
        st.metric("Pending KYC", f"{kpi['pending_kyc_customers']:,}")
    with cols2[2]:
        st.metric("PEP Customers", f"{kpi['pep_customers']:,}")
    with cols2[3]:
        st.metric("Sanctions Customers", f"{kpi['sanctions_customers']:,}")

elif page == "AML Monitoring":
    st.markdown("### Alert Monitoring")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(data['alerts_type'], x='alert_type', y='count', color='alert_type', 
                     title='Alerts by Type')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.pie(data['alerts_severity'], values='count', names='severity',
                     title='Alerts by Severity', color_discrete_sequence=['#E74C3C', '#F39C12'])
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### Activity Analysis")
    col3, col4 = st.columns(2)
    with col3:
        fig = px.line(data['hourly'], x='transaction_hour', y='transaction_count',
                      title='Hourly Transaction Activity')
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        if len(data['hr_geo']) > 0:
            fig = px.bar(data['hr_geo'], x='country', y='customer_count',
                         title='High-Risk Geography Activity')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No high-risk geography data")

elif page == "KYC Risk Analysis":
    st.markdown("### Customer Risk Distribution")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(data['risk_dist'], x='risk_category', y='count', color='risk_category',
                     title='Risk Category Distribution')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(data['kyc_dist'], x='kyc_status', y='count', color='kyc_status',
                     title='KYC Status Distribution')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### High-Risk Customer Monitoring")
    col3, col4 = st.columns(2)
    with col3:
        if len(data['pep']) > 0:
            st.dataframe(data['pep'][['customer_id', 'country', 'risk_category']], height=300)
        else:
            st.info("No PEP customers")
    with col4:
        if len(data['sanctions']) > 0:
            st.dataframe(data['sanctions'][['customer_id', 'country']], height=300)
        else:
            st.info("No sanctions customers")

elif page == "Investigation Analytics":
    st.markdown("### Investigation Metrics")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(data['escalation'], x='risk_level', y='count', color='risk_level',
                     title='Escalation Distribution', color_discrete_sequence=['#3498DB', '#E74C3C'])
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(data['outcomes'], x='investigation_status', y='count', color='investigation_status',
                     title='Investigation Outcomes')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### Recommendation Summary")
    fig = px.bar(data['recommendations'], x='recommendation', y='count', color='recommendation',
                 title='Analyst Recommendations')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Top Risk Tables":
    st.markdown("### Top Flagged Customers")
    st.dataframe(data['top_customers'], use_container_width=True, height=300)
    
    st.markdown("### High-Value Transactions (>200k)")
    st.dataframe(data['top_txn'], use_container_width=True, height=300)
    
    st.markdown("### High-Risk Geographies")
    st.dataframe(data['hr_geo'], use_container_width=True, height=300)

st.sidebar.markdown("---")
st.sidebar.markdown(f"Data Updated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}")