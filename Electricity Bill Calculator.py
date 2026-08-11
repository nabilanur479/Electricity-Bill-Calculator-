 import streamlit as st

st.set_page_config(page_title="Advanced Smart Bill Calculator", page_icon="⚡", layout="wide")

st.title("⚡ Advanced Smart Bill Calculator")
st.write("Calculate your electricity bill accurately based on room appliances.")

rooms_data = {
    "Living/Bed": {"Fan": ("75", "12"), "Light": ("20", "6"), "AC": ("1500", "5"), "TV": ("100", "4"), "Router": ("15", "24")},
    "Kitchen": {"Fridge": ("200", "24"), "Oven": ("1200", "0.5"), "Rice Cooker": ("800", "1"), "Blender": ("500", "0.2")},
    "Bathroom/Other": {"Geyser": ("2500", "1"), "Washing Machine": ("600", "1"), "Water Pump": ("750", "0.5"), "Iron": ("1000", "0.5")}
}

inputs = {}

tabs = st.tabs(list(rooms_data.keys()))

for index, (room_name, devices) in enumerate(rooms_data.items()):
    with tabs[index]:
        st.subheader(f"🏠 {room_name} Appliances")
        inputs[room_name] = {}
        
        col_dev, col_watt, col_hours = st.columns(3)
        col_dev.markdown("**Device**")
        col_watt.markdown("**Watt**")
        col_hours.markdown("**Hours**")
        
        for device, defaults in devices.items():
            c1, c2, c3 = st.columns(3)
            c1.write(device)
            w_input = c2.number_input(f"Watt ({device})", min_value=0.0, value=float(defaults), step=5.0, label_visibility="collapsed")
            h_input = c3.number_input(f"Hours ({device})", min_value=0.0, max_value=24.0, value=float(defaults), step=0.5, label_visibility="collapsed")
            
            inputs[room_name][device] = {"watt": w_input, "hours": h_input}

st.markdown("---")

if st.button("Calculate Bill", type="primary", use_container_width=True):
    try:
        total_wh = 0
        breakdown_text = "### 📋 Breakdown by Room\n"
        
        for room_name, devices in inputs.items():
            room_wh = 0
            breakdown_text += f"\n#### 🏠 {room_name}\n"
            
            for device, entries in devices.items():
                watt = float(entries["watt"])
                hours = float(entries["hours"])
                device_wh = watt * hours
                room_wh += device_wh
                
                breakdown_text += f"- **{device}**: {watt}W × {hours}h = **{device_wh:.1f} Wh**\n"
                
            total_wh += room_wh
            
        monthly_units = (total_wh / 1000) * 30
        
        if monthly_units <= 75:
            bill = monthly_units * 4.85
        elif monthly_units <= 200:
            bill = monthly_units * 6.63
        else:
            bill = monthly_units * 7.95
            
        total_bill = (bill + 40) * 1.05
        
        st.success("### 🎉 Bill Summary")
        col_res1, col_res2 = st.columns(2)
        col_res1.metric(label="Total Units Used", value=f"{monthly_units:.2f} kWh")
        col_res2.metric(label="Total Estimated Bill", value=f"{total_bill:.2f} BDT")
        
        st.markdown("---")
        st.markdown(breakdown_text)
        
    except ValueError:
        st.error("Error: Please enter valid numbers in all fields!")
        
