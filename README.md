📊 Google Data Analytics & Sales Intelligence Dashboard

📌 Project Overview

The Google Data Analytics & Sales Intelligence Dashboard is a data analysis and visualization project designed to analyze customer behavior, sales performance, profitability, product categories, marketing channels, payment methods, and regional performance.

The project uses Python, Pandas, Matplotlib, and Streamlit to transform raw sales data into meaningful insights through data cleaning, feature engineering, exploratory data analysis, visualization, and an interactive dashboard.

The final dashboard allows users to explore sales and customer performance using interactive filters and visualizations.

---

🎯 Project Objectives

The main objectives of this project are:

- Analyze overall sales and profit performance.
- Understand customer purchasing behavior.
- Identify the best-performing product categories.
- Analyze sales performance across different states.
- Compare different marketing channels.
- Analyze payment methods and device usage.
- Study monthly and yearly sales trends.
- Analyze customer ratings and purchasing patterns.
- Identify high-performing and low-performing categories.
- Create an interactive dashboard using Streamlit.
- Provide filtering and sorting options for better data exploration.
- Present important business insights through KPIs and visualizations.

---

🛠️ Technologies Used

Technology| Purpose
Python| Programming and data analysis
Pandas| Data cleaning and manipulation
NumPy| Numerical operations
Matplotlib| Data visualization
Streamlit| Interactive dashboard
Jupyter Notebook| Data analysis and exploration
CSV| Dataset storage
GitHub| Project version control

---

📊 Dataset

The project uses a customer and sales analytics dataset containing transactional and customer-related information.

The dataset is used to analyze sales, profit, customer behavior, product performance, marketing channels, and regional trends.

Important Features

- Customer ID
- Customer Name
- Date
- Year
- Month
- State
- Gender
- Product Category
- Product
- Sales
- Profit
- Quantity
- Rating
- Payment Method
- Marketing Channel
- Device
- Order ID

«Note: The exact columns in the README should be updated to match the final CSV used in the project.»

---

🔄 Project Workflow

The project follows the following data analytics workflow:

Raw Dataset

↓

Data Loading

↓

Data Cleaning

↓

Data Formatting

↓

Feature Engineering

↓

Filtering & Sorting

↓

Group By & Aggregation

↓

Exploratory Data Analysis

↓

Data Visualization

↓

Streamlit Dashboard

↓

Business Insights

---

🧹 Data Cleaning & Preprocessing

The dataset was prepared before performing analysis.

The following preprocessing steps were performed:

- Checked dataset dimensions using "shape".
- Inspected the dataset using "head()" and "tail()".
- Checked data types using "info()".
- Generated statistical summaries using "describe()".
- Checked missing values.
- Checked duplicate records.
- Converted date columns into appropriate date formats.
- Standardized categorical values.
- Converted numerical columns into appropriate data types.
- Created additional features required for analysis.

---

⚙️ Feature Engineering

Feature engineering was performed to create useful analytical variables from the existing data.

Examples include:

- Year extraction from Date
- Month extraction from Date
- Profit-related calculations
- Sales categories
- Customer-related segments
- Order-related metrics

These features help improve the quality of analysis and visualization.

---

🔎 Data Analysis

The project performs several analytical operations using Pandas.

Filtering

The dataset can be filtered based on:

- Year
- Product Category
- State
- Gender
- Marketing Channel
- Device
- Payment Method

Sorting

Data can be sorted based on:

- Sales
- Profit
- Rating
- Quantity
- Date

Group By & Aggregation

Group-by analysis is used to calculate:

- Total Sales
- Total Profit
- Total Orders
- Average Sales
- Average Rating
- Sales by Category
- Profit by Category
- Sales by State
- Sales by Marketing Channel

---

📈 Dashboard KPIs

The Streamlit dashboard displays important Key Performance Indicators (KPIs):

🔥 Total Sales

Displays the overall sales generated from the dataset.

💰 Total Profit

Displays the total profit generated.

🛒 Total Orders

Displays the total number of orders.

💵 Average Sales per Order

Shows the average sales value generated per order.

⭐ Average Rating

Displays the average customer/product rating.

---

📊 Dashboard Visualizations

1. 📈 Monthly Sales Trend

A line chart is used to analyze how sales change over time.

This helps identify:

- Increasing sales
- Decreasing sales
- Seasonal patterns
- High-performing months

---

2. 🛍️ Sales by Product Category

A bar chart compares total sales across different product categories.

This helps identify the categories generating the highest revenue.

---

3. 💰 Profit by Product Category

A bar chart compares profitability across product categories.

This helps identify which categories contribute most to overall profit.

---

4. 📣 Sales by Marketing Channel

The dashboard compares sales generated through different marketing channels.

This helps determine which marketing channels perform better.

---

5. 📍 Top 10 States by Sales

The dashboard identifies the top-performing states based on total sales.

This provides insight into regional sales performance.

---

6. 🥧 Sales Distribution

Pie charts are used to visualize the distribution of sales across selected categories such as:

- Product Category
- Gender
- Marketing Channel
- Payment Method

---

7. 📊 Sales & Profit Distribution

Histograms are used to understand the distribution of numerical variables such as sales and profit.

---

8. 🔵 Relationship Analysis

Scatter plots are used to study relationships between variables such as:

- Sales vs Profit
- Rating vs Sales
- Quantity vs Sales

---

🎛️ Interactive Dashboard Filters

Users can interact with the dashboard using filters such as:

- 📅 Year
- 🛍️ Product Category
- 📍 State
- 👤 Gender
- 📣 Marketing Channel
- 💻 Device
- 💳 Payment Method

The dashboard updates the displayed analysis according to the selected filters.

---

📋 Raw Data

The dashboard also provides access to the underlying dataset so users can inspect the original records used for analysis.

---

💡 Key Business Insights

The project can be used to identify insights such as:

- Which product categories generate the highest sales?
- Which categories generate the highest profit?
- Which states contribute the most revenue?
- Which marketing channels perform best?
- Which months have the highest sales?
- Which payment methods are most commonly used?
- How does customer rating relate to sales?
- Which devices are most frequently used for purchases?
- Which customer segments contribute most to sales?

---

🚀 Project Features

📊 Data Analysis

Complete exploratory analysis using Python and Pandas.

🧹 Data Cleaning

Handling missing values, duplicates, data types, and formatting.

⚙️ Feature Engineering

Creating additional variables to improve analysis.

📈 Data Visualization

Multiple visualization techniques including:

- Bar Charts
- Pie Charts
- Histograms
- Line Charts
- Scatter Plots

🎛️ Interactive Filters

Users can dynamically filter dashboard data.

📱 Streamlit Dashboard

An interactive web-based dashboard for exploring the dataset.

📋 Raw Data View

Users can inspect the underlying dataset directly from the dashboard.

---

📁 Project Structure

Google-Data-Analytics-Dashboard/
│
├── google_data_analytics_dashboard.csv
│
├── Google.Data.Analytics.&Dashboard.ipynb
│
├── dashboard_google.py
│
├── README.md
│
└── requirements.txt

---

▶️ How to Run the Project

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_LINK

2. Open the Project Folder

cd Google-Data-Analytics-Dashboard

3. Install Required Libraries

pip install pandas numpy matplotlib streamlit

4. Run the Streamlit Dashboard

streamlit run dashboard_google.py

5. Open the Dashboard

Streamlit will provide a local URL such as:

http://localhost:8501

Open it in your browser to view the dashboard.

---

📌 Project Outcome

This project demonstrates the complete data analytics lifecycle, from raw data to an interactive business intelligence dashboard.

It combines:

Python → Data Cleaning → Feature Engineering → EDA → Visualization → Streamlit → Business Insights

The project provides an interactive way to understand customer, sales, product, marketing, and regional performance.

---

👩‍💻👨‍💻 Author

1. Mrunali Gorkhe
2. Atharva Bhavsar
Project: Google Data Analytics & Sales Intelligence Dashboard

Built using Python, Pandas, Matplotlib, Jupyter Notebook, and Streamlit.
