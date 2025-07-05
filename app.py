# app.py
import streamlit as st
import plotly.express as px
from scraper import generate_mock_data

st.set_page_config(page_title="Airline Demand Insights", layout="wide")

st.title("✈ Airline Market Demand Dashboard")

df = generate_mock_data()

# Filters
st.sidebar.header("Filter Options")
origins = st.sidebar.multiselect("Select Origin City", options=df['Origin'].unique(), default=None)
destinations = st.sidebar.multiselect("Select Destination City", options=df['Destination'].unique(), default=None)

filtered_df = df.copy()
if origins:
    filtered_df = filtered_df[filtered_df['Origin'].isin(origins)]
if destinations:
    filtered_df = filtered_df[filtered_df['Destination'].isin(destinations)]

# Show Table
st.subheader("📊 Filtered Data")
st.dataframe(filtered_df)

# Show Charts
st.subheader("📈 Price Trends")
fig = px.line(filtered_df, x='Date', y='Price', color='Origin', title="Average Prices Over Time")
st.plotly_chart(fig, use_container_width=True)

# Insights Summary
st.subheader("💡 Insights")
if not filtered_df.empty:
    max_route = filtered_df.groupby(['Origin', 'Destination']).size().idxmax()
    st.markdown(f"*Most popular route:* {max_route[0]} → {max_route[1]}")
    avg_price = filtered_df['Price'].mean()
    st.markdown(f"*Average price:* ${avg_price:.2f}")
else:
    st.warning("No data for selected filters.")
