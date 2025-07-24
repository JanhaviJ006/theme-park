🎢 Theme Park Price Optimization & Forecasting Dashboard

This project demonstrates how data science can be applied to optimize ticket pricing, forecast visitor demand, and identify pricing strategies using a simulated theme park dataset.

Files Included
theme_park_dashboard.py - Interactive Streamlit app to simulate pricing impact 
Theme_Park.ipynb - Jupyter notebook with EDA, forecasting, elasticity, clustering, and testing
Extended_Theme_Park_Dataset.csv - Simulated dataset from Jan 2023 to Apr 2025 

Features

- Visitor demand forecasting with Facebook Prophet
- Revenue modeling based on ticket price
- Price Elasticity of Demand (PED) analysis
- A/B testing of promotional impact
- Visitor segmentation using K-Means clustering
- Streamlit dashboard for live simulation & business strategy

How to Run the Streamlit App

1. Clone this repository** or [download the files manually](https://github.com/your-username/theme-park-price-optimization):
   ```bash
   git clone https://github.com/your-username/theme-park-price-optimization.git
   cd theme-park-price-optimization

2. Install all required packages:
pip install streamlit pandas numpy matplotlib seaborn prophet

3. Run the Streamlit app:
streamlit run theme_park_dashboard.py

What I Learned:
Built a forecasting model with Prophet to predict attendance
Calculated and visualized price elasticity for smarter pricing
Simulated promotions and evaluated their impact using A/B testing
Used clustering (K-Means) to segment customers based on behavior
Built an interactive dashboard with Streamlit to turn analysis into action
