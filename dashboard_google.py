import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# 🌐 GOOGLE DATA ANALYTICS DASHBOARD


st.set_page_config(
    page_title="Google Data Analytics Dashboard",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD DATA

@st.cache_data
def load_data():
    df = pd.read_csv("google_data_analytics_dashboard.csv")
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    # Keep the same terminology used in the analysis
    if "Total_Sales" in df.columns and "Sales" not in df.columns:
        df["Sales"] = df["Total_Sales"]

    df["Profit_Margin"] = (
        df["Profit"] / df["Total_Sales"].replace(0, pd.NA) * 100
    ).fillna(0)

    df["Year"] = df["Order_Date"].dt.year
    df["Month_Name"] = df["Order_Date"].dt.strftime("%b")
    df["Month_Number"] = df["Order_Date"].dt.month

    return df


try:
    data = load_data()
except FileNotFoundError:
    st.error(
        "❌ google_data_analytics_dashboard.csv was not found. "
        "Keep the CSV file in the same folder as dashboard.py."
    )
    st.stop()

# SIDEBAR

st.sidebar.title("🌐 Google Analytics")
st.sidebar.caption("Customer • Sales • Profit • Marketing")

years = sorted(data["Year"].dropna().unique())
if len(years) > 1:
    year_range = st.sidebar.slider(
        "📅 Choose Year",
        min_value=int(min(years)),
        max_value=int(max(years)),
        value=(int(min(years)), int(max(years)))
    )
else:
    year_range = (int(years[0]), int(years[0]))
    st.sidebar.info(f"📅 Year: {years[0]}")

category_options = sorted(data["Product_Category"].dropna().unique())
state_options = sorted(data["State"].dropna().unique())
gender_options = sorted(data["Gender"].dropna().unique())
channel_options = sorted(data["Marketing_Channel"].dropna().unique())
device_options = sorted(data["Device"].dropna().unique())

category = st.sidebar.multiselect(
    "🛍️ Product Category",
    category_options
)

state = st.sidebar.multiselect(
    "📍 State",
    state_options
)

gender = st.sidebar.multiselect(
    "👤 Gender",
    gender_options
)

channel = st.sidebar.multiselect(
    "📣 Marketing Channel",
    channel_options
)

device = st.sidebar.multiselect(
    "📱 Device",
    device_options
)

# FILTER DATA 

filtered_df = data[
    (data["Year"] >= year_range[0]) &
    (data["Year"] <= year_range[1])
].copy()

if category:
    filtered_df = filtered_df[
        filtered_df["Product_Category"].isin(category)
    ]

if state:
    filtered_df = filtered_df[
        filtered_df["State"].isin(state)
    ]

if gender:
    filtered_df = filtered_df[
        filtered_df["Gender"].isin(gender)
    ]

if channel:
    filtered_df = filtered_df[
        filtered_df["Marketing_Channel"].isin(channel)
    ]

if device:
    filtered_df = filtered_df[
        filtered_df["Device"].isin(device)
    ]

st.sidebar.divider()
st.sidebar.caption(
    "Google Data Analytics Project\n"
    "Interactive Streamlit Dashboard"
)

# HEADER

st.title("🌐 Google Data Analytics Dashboard")
st.markdown(
    "### 📊 Customer & Sales Performance Intelligence"
)
st.caption(
    "Explore sales, profit, customers, products, marketing channels, "
    "payment methods and regional performance."
)

# KPI CARDS 

total_sales = filtered_df["Total_Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order_ID"].nunique()
avg_sales = filtered_df["Total_Sales"].mean()
avg_rating = filtered_df["Customer_Rating"].mean()
total_quantity = filtered_df["Quantity"].sum()

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
c2.metric("📈 Total Profit", f"₹{total_profit:,.0f}")
c3.metric("🧾 Total Orders", f"{total_orders:,}")
c4.metric("🛒 Avg. Sales / Order", f"₹{avg_sales:,.0f}")
c5.metric("⭐ Avg. Rating", f"{avg_rating:.2f}")

st.divider()

# TABS

tab1, tab2, tab3 = st.tabs(
    ["🏠 Dashboard", "💡 Insights", "📋 Raw Data"]
)

# TAB 1 — DASHBOARD
with tab1:

    # Monthly Sales Trend
    
    st.subheader("📈Monthly Sales Trend")

    monthly_sales = (
        filtered_df
        .groupby(["Year", "Month_Number", "Month_Name"])["Total_Sales"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Month_Number"])
    )

    monthly_sales["Period"] = (
        monthly_sales["Month_Name"] + " " +
        monthly_sales["Year"].astype(str)
    )

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(
        monthly_sales["Period"],
        monthly_sales["Total_Sales"],
        marker="o",
        color = "#901E3E"
    )
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales")
    ax.set_title("Monthly Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    col1, col2 = st.columns(2)

    # Sales by Product Category
    with col1:
        st.subheader("🛍️ Sales by Product Category")

        colors = ["#D6336C","#FF4081","#FFB6C1","#FFCEE3","#FFF5F8"]
        category_sales = (
            filtered_df
            .groupby("Product_Category")["Total_Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.barh(category_sales.index, category_sales.values, color=colors)
        ax.set_xlabel("Total Sales")
        ax.set_ylabel("Product Category")
        ax.set_title("Sales by Product Category")
        ax.invert_yaxis()
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    # Profit by Product Category
    with col2:
        st.subheader("💰 Profit by Product Category")
        colors = ["#15173D","#982598","#F375C2","#E491C9","#F1E9E9"]
        category_profit = (
            filtered_df
            .groupby("Product_Category")["Profit"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(category_profit.index, category_profit.values,color=colors)
        ax.set_xlabel("Product Category")
        ax.set_ylabel("Profit")
        ax.set_title("Profit by Product Category")
        plt.xticks(rotation=35)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    col1, col2 = st.columns(2)

    # Marketing Channel
    with col1:
        st.subheader("📣 Sales by Marketing Channel")
        colors = ["#000000","#1F150C","#412D15","#715A5A","#EBD5AB","#E1DCC9"]
        channel_sales = (
            filtered_df
            .groupby("Marketing_Channel")["Total_Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(channel_sales.index, channel_sales.values, color=colors)
        ax.set_xlabel("Marketing Channel")
        ax.set_ylabel("Total Sales")
        ax.set_title("Sales by Marketing Channel")
        plt.xticks(rotation=35)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    # State Performance
    with col2:
        st.subheader("📍 Top 10 States by Sales")
        colors = ["#60241E","#95271D","#E73F1E","#FB6C00","#F9B637","#FED24F","#FFF449","#FFDE4E","#E1DCC9"]
        state_sales = (
            filtered_df
            .groupby("State")["Total_Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.barh(state_sales.index, state_sales.values,color=colors)
        ax.set_xlabel("Total Sales")
        ax.set_ylabel("State")
        ax.set_title("Top 10 States by Sales")
        ax.invert_yaxis()
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    col1, col2 = st.columns(2)

    # Payment Method
    with col1:
        st.subheader("💳 Payment Method Distribution")
        colors = ["#5D3140","#CF4173","#F39399","#F5CBCB","#F6D8BD"]
        payment_counts = filtered_df["Payment_Method"].value_counts()

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.pie(
            payment_counts.values,
            labels=payment_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors
        )
        ax.set_title("Payment Method Distribution")
        st.pyplot(fig)
        plt.close(fig)

    # Gender Distribution
    with col2:
        st.subheader("👥 Customer Distribution by Gender")
        colours = ["#2BBBD7","#F599C6"]
        gender_counts = filtered_df["Gender"].value_counts()

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.pie(
            gender_counts.values,
            labels=gender_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=colours
        )
        ax.set_title("Customer Distribution by Gender")
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    col1, col2 = st.columns(2)

    # Sales vs Profit
    with col1:
        st.subheader("🔵 Sales vs Profit")
        colors = "#EF88AD"
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(
            filtered_df["Total_Sales"],
            filtered_df["Profit"],
            alpha=0.6,
            color=colors
        )
        ax.set_xlabel("Total Sales")
        ax.set_ylabel("Profit")
        ax.set_title("Total Sales vs Profit")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    # Discount vs Profit
    with col2:
        st.subheader("🏷️ Discount vs Profit")
        colors = "#6A1E55"
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(
            filtered_df["Discount"],
            filtered_df["Profit"],
            alpha=0.6,
            color=colors
        )
        ax.set_xlabel("Discount (%)")
        ax.set_ylabel("Profit")
        ax.set_title("Discount vs Profit")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    # Top Products
    st.subheader("🏆 Top 10 Products by Sales")
    colors = ["#760031", "#E73F1E", "#D51C39", "#FB6C00", "#F9B637", "#FEEC41", "#FFDA62", "#FFDD9C", "#FEF2A0", "#F5E7C6"]
    top_products = (
        filtered_df
        .groupby("Product_Name")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.bar(top_products.index, top_products.values,color=colors)
    ax.set_xlabel("Product")
    ax.set_ylabel("Total Sales")
    ax.set_title("Top 10 Products by Total Sales")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# TAB 2 — INSIGHTS

with tab2:

    st.subheader("💡 Key Business Insights")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
    else:
        top_product = (
            filtered_df.groupby("Product_Name")["Total_Sales"]
            .sum()
            .idxmax()
        )

        top_category = (
            filtered_df.groupby("Product_Category")["Total_Sales"]
            .sum()
            .idxmax()
        )

        top_channel = (
            filtered_df.groupby("Marketing_Channel")["Total_Sales"]
            .sum()
            .idxmax()
        )

        top_state = (
            filtered_df.groupby("State")["Total_Sales"]
            .sum()
            .idxmax()
        )

        top_payment = filtered_df["Payment_Method"].value_counts().idxmax()

        best_month = (
            filtered_df.groupby("Month_Name")["Total_Sales"]
            .sum()
            .sort_values(ascending=False)
            .index[0]
        )

        top_profit_product = (
            filtered_df.groupby("Product_Name")["Profit"]
            .sum()
            .idxmax()
        )

        avg_margin = filtered_df["Profit_Margin"].mean()

        st.success(
            f"🏆 **Top Product:** {top_product} generated the highest sales."
        )

        st.info(
            f"🛍️ **Leading Category:** {top_category} is the highest-sales "
            f"product category."
        )

        st.info(
            f"📣 **Best Marketing Channel:** {top_channel} generated the "
            f"highest sales."
        )

        st.info(
            f"📍 **Top State:** {top_state} recorded the highest sales."
        )

        st.info(
            f"💳 **Most Used Payment Method:** {top_payment}."
        )

        st.info(
            f"📅 **Strongest Sales Month:** {best_month}."
        )

        st.success(
            f"💰 **Most Profitable Product:** {top_profit_product}."
        )

        st.metric(
            "📊 Average Profit Margin",
            f"{avg_margin:.2f}%"
        )

        st.divider()

        st.subheader("📌 Project Summary")

        st.write(
            "This dashboard presents the major findings from the Google "
            "Data Analytics project. It brings together customer behavior, "
            "product performance, sales, profit, marketing channels, "
            "payment methods and regional trends into one interactive view."
        )

        st.write(
            "The dashboard is designed to make the analysis easier to "
            "explore by allowing users to filter the results by year, "
            "product category, state, gender, marketing channel and device."
        )


# TAB 3 — RAW DATA

with tab3:

    st.subheader("📋 Filtered Raw Data")

    st.write(
        f"Showing **{len(filtered_df):,}** records after applying filters."
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="⬇️ Download Filtered Data",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="google_filtered_data.csv",
        mime="text/csv"
    )
