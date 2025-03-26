
# 📊 Technical Skills Showcase — Streamlit Demo App

This Streamlit application is a hands-on demo designed to showcase core technical skills related to data analysis, pricing logic, SQL querying, and visualization. It simulates a simple real-world logistics dataset analysis workflow and serves as a personal project to practice and demonstrate the following:

- 📊 **Data Analysis** with pandas
- 💸 **Pricing & Profitability Calculations**
- 🧠 **SQL Query Execution** using SQLite
- 📈 **Visualization** using matplotlib
- 📥 **CSV Handling** and dynamic input management

---

## 🚀 What This App Does

1. **Upload Data**: Accepts a logistics-style CSV file or uses a sample dataset (`demo_logistics_data.csv`).
2. **Preview Data**: Displays the first few rows and gives a shape + null count summary.
3. **Profit & Margin Analysis**: Automatically calculates unit profit and margin percent using `Price` and `Cost` columns.
4. **Histogram Visualization**: Shows the distribution of profit margins.
5. **SQL Query Engine**: Allows you to write SQL queries directly on the uploaded data.
6. **Insights Summary**: Shows top-performing products and key profitability metrics.

---

## 📂 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yeuner/margin-price-data-demo-app.git
   cd margin-price-data-demo-app
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 📦 Sample Data

If you don’t upload a file, the app will use `demo_logistics_data.csv` located in the same folder. Make sure it’s present in the root directory.

---

## 🛠️ Tech Stack

- **Streamlit**: UI and app engine
- **pandas**: Data manipulation
- **matplotlib**: Visualizations
- **sqlite3**: In-memory SQL engine

---

## 📚 Why This Project?

This project was created to **practice and demonstrate key technical skills** in a compact and professional way as part of my personal portfolio.

---

## 📬 Feedback & Contributions

Feel free to fork the repo, try it out, and share feedback or improvements!
