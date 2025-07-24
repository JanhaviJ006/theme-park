import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from prophet import Prophet

# Load data
df = pd.read_csv("/Users/janhavijadhav/Downloads/Extended_Theme_Park_Dataset.csv")
df['Date'] = pd.to_datetime(df['Date'])

st.set_page_config(layout="wide")
st.title("🎢 Theme Park Pricing Strategy Simulator")

# Train Prophet model (place this BEFORE it's needed)
df_prophet = df[['Date', 'Visitors']].rename(columns={'Date': 'ds', 'Visitors': 'y'})
model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
model.fit(df_prophet)
future_df = model.make_future_dataframe(periods=90)
forecast = model.predict(future_df)

# 1. Price & Promotion Simulator
st.sidebar.header("🎯 Price & Promotion Simulator")

selected_price = st.sidebar.slider("Set Ticket Price ($)", 70.0, 100.0, 85.0, 0.5)
promo_flag = st.sidebar.checkbox("Apply Promotion?", value=False)
today_weather = st.sidebar.slider("Today's Weather Score (0–10)", 0, 10, 7)

# 🎯 Date-aware Estimated Impact
st.subheader("💡 Estimated Impact (based on selected date)")

# User selects forecast date
selected_date = st.date_input("Choose a future date:", dt.date(2023, 12, 1))
selected_datetime = pd.to_datetime(selected_date)

# Lookup forecasted visitors from Prophet
forecast_day = forecast[forecast['ds'] == selected_datetime]

if not forecast_day.empty:
    base_visitors = forecast_day['yhat'].values[0]

    # Adjust based on input
    adjusted_visitors = (
        base_visitors
        + (10 * (90 - selected_price))
        + (300 if promo_flag else 0)
        + (50 * today_weather)
    )

    estimated_revenue = adjusted_visitors * selected_price

    st.metric("Expected Visitors", f"{int(adjusted_visitors):,}")
    st.metric("Expected Revenue", f"${int(estimated_revenue):,}")
else:
    st.warning("This date is not in the forecast range. Try a date within the next 90 days.")

# 2. Forecast a Future Day
st.markdown("---")
st.subheader("📅 Forecast Visitors for a Future Date")

forecast_day = forecast[forecast['ds'] == pd.to_datetime(selected_date)]
if not forecast_day.empty:
    forecasted = int(forecast_day['yhat'].values[0])
    st.success(f"📈 Forecasted Visitors on {selected_date.strftime('%A, %b %d')}: **{forecasted:,}**")
else:
    st.warning("Please select a date within the next 90 days.")

# 3. Smart Insights
st.markdown("---")
st.subheader("🧠 Smart Pricing Insight")

if selected_price >= 85 and promo_flag:
    st.info("👍 Try this combo on weekends or holidays to maximize both revenue and volume!")
elif selected_price < 80 and not promo_flag:
    st.warning("⚠️ Low price without promotion may leave revenue on the table. Consider bundling.")
elif selected_price > 95:
    st.error("⚠️ High price — risk of losing visitors unless it's peak season!")
else:
    st.success("✅ Balanced strategy — monitor demand and adjust weekly.")
