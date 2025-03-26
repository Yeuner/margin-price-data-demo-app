import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Skills Demo App", layout="wide")

st.title("📊 Technical Skills Showcase")

st.markdown("""
Welcome! This simple Streamlit demo application is designed to showcase core technical skills through the analysis of data. Here's what the app does:

1. 📥 Accepts a logistics CSV file (or uses sample data).
2. 🔍 Displays the dataset, basic stats, and missing values.
3. 💰 Calculates unit profit and profit margins (requires 'Cost' and 'Price' columns).
4. 📈 Visualizes the distribution of profit margins.
5. 🧠 Allows SQL queries directly on the uploaded dataset.
6. 📢 Summarizes key findings such as average margin and top product.

This app highlights skills in data analysis, pricing logic, SQL querying, and visualization.
""")

# Sidebar - Profile and Skill Badges
st.sidebar.title("👤 About Me")
st.sidebar.info("""
This app demonstrates:
- I am using streamlit library to deploy this app
- Pricing Competency
- Data Tools (Excel/SQL/Python)
""")

st.sidebar.markdown("---")
st.sidebar.caption("Upload a CSV or use our sample data.")

# Upload or Sample Data
uploaded_file = st.file_uploader("Upload Your Logistics CSV", type="csv")
use_sample = st.checkbox("Use sample data instead (demo_logistics_data.csv in current directory)")

if uploaded_file or use_sample:
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    elif os.path.exists("demo_logistics_data.csv"):
        df = pd.read_csv("demo_logistics_data.csv")
    else:
        st.error("Sample file 'demo_logistics_data.csv' not found in the current directory.")
        st.stop()

    st.subheader("📦 Dataset Preview")
    st.dataframe(df.head())

    # Clean & Basic Info
    st.markdown("### 🧹 Data Overview")
    st.write("Shape:", df.shape)
    st.write("Missing Values:", df.isnull().sum())

    # Profit & Margin
    if 'Cost' in df.columns and 'Price' in df.columns:
        df['Profit'] = df['Price'] - df['Cost']
        df['Margin %'] = round((df['Profit'] / df['Price']) * 100, 2)

        st.markdown("### 💸 Pricing & Margin Analysis")
        st.dataframe(df[['Product', 'Cost', 'Price', 'Profit', 'Margin %']])

        fig, ax = plt.subplots()
        df['Margin %'].hist(ax=ax, bins=10)
        ax.set_title("Profit Margin Distribution")
        ax.set_xlabel("Margin %")
        st.pyplot(fig)
    else:
        st.warning("'Cost' and 'Price' columns are needed for pricing analysis.")

    # SQL Query Section
    st.markdown("### 🧠 SQL Analysis")
    conn = sqlite3.connect(":memory:")
    df.to_sql("data", conn, index=False, if_exists='replace')
    query = st.text_area("Write your SQL query:", "SELECT Product, Profit FROM data ORDER BY Profit DESC LIMIT 5")
    try:
        result = pd.read_sql_query(query, conn)
        st.dataframe(result)
    except Exception as e:
        st.error(f"SQL Error: {e}")

    # Summary Communication
    st.markdown("### 📢 Insights Summary")
    st.markdown("""
    Based on the current dataset:
    - **Average Margin:** {:.2f}%
    - **Negative Profit Products:** {}
    - **Top Performer:** {}
    """.format(
        df['Margin %'].mean(),
        (df['Profit'] < 0).sum(),
        df.loc[df['Profit'].idxmax()]['Product'] if 'Product' in df.columns else "N/A"
    ))

    # Skills Recap
    st.markdown("### ✅ Technical Skills Demonstrated")
    st.success("""
    - 📊 **Data Analysis**: pandas, data cleaning, summaries
    - 💸 **Pricing Logic**: cost, price, margin and profit breakdowns
    - 🧠 **SQL Querying**: dynamic query execution on user-provided data
    - 📈 **Visualization**: matplotlib histograms for margin distribution
    """)
else:
    st.info("Upload a logistics-related CSV file or check the box to use sample data.")