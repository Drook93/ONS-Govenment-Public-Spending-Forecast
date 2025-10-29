import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="ONS Consumer Spending Forecast Dashboard", layout="wide")

st.title("ONS Consumer Spending Forecast Dashboard")
st.markdown("Visualize consumer spending forecasts by quarter and sector, with inflation metrics.")


@st.cache_data
def load_data():
   
    consumer_spend = pd.read_excel("Forecasting Final.xlsx")

     

    consumer_spend = consumer_spend[consumer_spend['Time Period'] <= '2026-01-01']
    consumer_spend['Time Period'] = pd.to_datetime(consumer_spend['Time Period'])
    

    consumer_spend['Time Period'] = pd.to_datetime(consumer_spend['Time Period'])
    consumer_spend['Time Period'] = consumer_spend['Time Period'].dt.to_period('Q').astype(str).str.replace('Q', ' Q')
    
    return consumer_spend

consumer_spend = load_data()


sectors = [
    'Food And Drink', 'Alcohol, Tobacco And Narcotics', 'Clothing And Footwear', 
    'Housing', 'Furniture, Household Equipment And Maintenance',
    'Health', 'Transport', 'Communication', 'Recreation And Culture', 
    'Education', 'Restaurants And Hotels', 'Miscellaneous'
]


total_spending = consumer_spend.groupby('Time Period')[sectors].sum().sum(axis=1).reset_index()
total_spending.columns = ['Time Period', 'Total Expenditure']


st.sidebar.header("Filters")
quarters = sorted(total_spending['Time Period'].unique())
selected_quarters = st.sidebar.multiselect("Select Quarters", quarters, default=quarters[:4])
selected_sectors = st.sidebar.multiselect("Select Sectors", sectors, default=sectors)

filtered_spend = consumer_spend[consumer_spend['Time Period'].isin(selected_quarters)]



st.subheader("Total Consumer Spending by Quarter (Millions)")
fig_line = go.Figure()
fig_line.add_trace(
    go.Scatter(
        x=total_spending['Time Period'],
        y=total_spending['Total Expenditure'],
        mode='lines',
        text=[f"{x:,.0f}" for x in total_spending['Total Expenditure']],
        textposition="top center",
        name="Total Spending"
    )
)
fig_line.update_layout(
    xaxis_title="Quarter",
    yaxis_title="Total Expenditure (£M)",
    template="plotly_white",
    height=400
)
st.plotly_chart(fig_line, use_container_width=True)

st.subheader("Expenditure By Sector (Millions)")
fig_line = go.Figure()

numeric_cols = consumer_spend.columns[1:13]

for col in numeric_cols:
    fig_line.add_trace(
        go.Scatter(
            x=consumer_spend['Time Period'],
            y=consumer_spend[col],
            mode='lines+markers',
            name=col
        )
    )

y_min = consumer_spend[numeric_cols].min().min()
y_max = consumer_spend[numeric_cols].max().max()

fig_line.update_layout(
    xaxis_title="Quarter",
    yaxis_title="Expenditure (£M)",
    template="plotly_white",
    height=400,
    yaxis=dict(
        range=[y_min * 0.95, y_max * 1.05]
    )
)


st.plotly_chart(fig_line, use_container_width=True)


st.subheader("Spending by Sector (Millions)")
melted_data = pd.melt(
    filtered_spend,
    id_vars=['Time Period'],
    value_vars=selected_sectors,
    var_name='Sector',
    value_name='Expenditure'
)
fig_bar = px.bar(
    melted_data,
    x='Time Period',
    y='Expenditure',
    color='Sector',
    barmode='group',
    title="Spending by Sector for Selected Quarters"
)
fig_bar.update_layout(
    xaxis_title="Quarter",
    yaxis_title="Expenditure (£M)",
    template="plotly_white",
    height=500
)
st.plotly_chart(fig_bar, use_container_width=True)

forecast_data = consumer_spend.iloc[-4:, 1:13].sum()

fig = go.Figure()
fig.add_trace(go.Bar(
    x=forecast_data.index,
    y=forecast_data.values,
    text=forecast_data.values,
    textposition='outside',
    texttemplate='%{text:.0f}'
))

fig.update_layout(
    title="Total Forecasted Spending by Sector (2025 Q1 - 2026 Q1)",
    xaxis_title="Spending Sector",
    yaxis_title="Total Spending (£M)",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Inflation Metrics (Lag 3)")
st.dataframe(consumer_spend[['Inflation_Acceleration_lag3']].head())


st.subheader("Model Evaluation")
st.image("OLS_Model.png", caption="OLS Model Results", use_column_width=True)