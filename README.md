# 🤖 Data Analytics AI Bot Dashboard

An interactive **AI-powered Data Analytics Dashboard** built using **Streamlit, Python, and PostgreSQL**, designed to automate data cleaning, transformation, analysis, and visualization for CSV and Excel datasets.

This project demonstrates **end-to-end data analytics workflow** — from raw data upload to insights generation — with user activity logging and an admin monitoring panel.

---

## 🚀 Project Overview

The **Data Analytics AI Bot** enables users to:

* Upload raw CSV or Excel datasets
* Automatically clean missing values, duplicates, and outliers
* Transform datasets (rename columns, change data types, encode categoricals)
* Perform exploratory data analysis (EDA)
* Generate interactive charts and visual insights
* Log user activity securely into a PostgreSQL database

An **Admin Dashboard** allows monitoring of user uploads and activity logs.

---

## 📊 Key Features

### 🔹 Data Handling

* CSV & Excel file support
* Automatic data loading
* Real-time data preview

### 🔹 Data Cleaning

* Missing value handling (mean/mode-based)
* Duplicate removal
* Outlier detection using Z-score method

### 🔹 Data Transformation

* Column renaming
* Data type conversion
* One-hot encoding for categorical variables

### 🔹 Data Analysis

* Summary statistics
* Correlation analysis
* Categorical pattern detection

### 🔹 Data Visualization

* Bar charts
* Line charts
* Pie charts
* Scatter plots
* Correlation heatmaps

### 🔹 User & Admin Management

* User name capture
* Dataset upload logging
* Admin login system
* User activity tracking via PostgreSQL

---

## 🧠 Dashboard Sections

### 1️⃣ User Analytics Dashboard

Includes:

* Raw data preview
* Cleaned dataset view
* Transformed dataset view
* Summary statistics
* Correlation matrix
* Pattern analysis

---

### 2️⃣ Visualization Dashboard

Includes:

* Dynamic chart selection
* X-axis and Y-axis controls
* Interactive Plotly-based visuals
* Real-time chart generation

---

### 3️⃣ Admin Dashboard

Includes:

* Secure admin login
* User upload logs
* Timestamped activity records
* Tabular activity view

---

## 🛠 Tools & Technologies Used

### 🧩 Core Technologies

* Python
* Streamlit
* PostgreSQL

### 📚 Libraries

* pandas
* numpy
* scipy
* matplotlib
* seaborn
* plotly
* psycopg2
* openpyxl

---

## 📁 Project Structure

| File                 | Description                              |
| -------------------- | ---------------------------------------- |
| `app.py`             | Main Streamlit application               |
| `admin.py`           | Admin dashboard & login                  |
| `data_processing.py` | Data cleaning, transformation & analysis |
| `visualization.py`   | Chart & visualization logic              |
| `database.py`        | PostgreSQL connection & logging          |
| `config.py`          | Database & admin configuration           |
| `requirements.txt`   | Project dependencies                     |



---

## 🎯 Purpose of This Project

This project aims to:

* Demonstrate real-world data analytics workflows
* Showcase Python-based dashboard development
* Practice data cleaning and EDA techniques
* Integrate analytics with databases
* Build a portfolio-ready analytics application

---

## 📈 Key Insights Delivered

* Automated data quality improvement
* Faster exploratory data analysis
* Visual-driven decision support
* User behavior tracking
* Scalable analytics workflow

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/data-analytics-ai-bot.git

# Navigate to project directory
cd data-analytics-ai-bot

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

> Ensure PostgreSQL is running and database credentials are correctly set in `config.py`.

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome.
Feel free to fork the repository and submit a pull request.

---

## ⭐ Support

If you find this project useful, please **star the repository** to support the work and encourage further development.

---

