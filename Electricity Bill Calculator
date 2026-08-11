import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Electricity Bill Calculator", 
    page_icon="⚡", 
    layout="centered"
)

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1e7e34;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #dc3545;
        color: white;
        width: 100%;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #bd2130;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1>⚡ Electricity Bill Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6c757d;'>A free web application developed for CSE 102 Lab Project</p>", unsafe_allow_html=True)
st.divider()

# 4. User Input Section (Split into 2 Columns)
col1, col2 = st.columns(2)

with col1:
    st.subheader("💡 Fan Configuration")
    fan_watt = st.number_input("Total Fan Wattage (W):", min_value=0.0, value=75.0, step=1.0)
    fan_hours = st.number_input("Usage Hours/Day:", min_value=0.0, max_value=24.0, value=12.0, step=0.5)

with col2:
    st.subheader("💡 Light Configuration")
    light_watt = st.number_input("Total Light Wattage (W):", min_value=0.0, value=20.0, step=1.0)
    light_hours = st.number_input("Usage Hours/Day:", min_value=0.0, max_value=24.0, value=6.0, step=0.5)

st.divider()

# 5. Calculation and Logic Section
if st.button("Calculate Bill"):
    # Core Mathematical Logic
    total_wh = (fan_watt * fan_hours) + (light_watt * light_hours)
    monthly_units = (total_wh / 1000) * 30
    total_bill = monthly_units * 6.0
    
    # Results Display
    st.markdown("<h3 style='color: #2c3e50;'>📊 Calculation Results:</h3>", unsafe_allow_html=True)
    
    st.success(f"**Monthly Energy Consumption:** {monthly_units:.2f} kWh (Units)")
    st.info(f"**Estimated Monthly Bill:** {total_bill:.2f} BDT (Taka)")
    st.caption("Note: This calculation is based on a flat rate of 6.00 BDT per unit.")
