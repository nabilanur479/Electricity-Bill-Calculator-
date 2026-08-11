# --- Electricity Bill Calculator App ---
import streamlit as st

st.set_page_config(page_title="Advanced Smart Bill Calculator", page_icon="⚡")
st.title("⚡ Advanced Smart Bill Calculator")
st.write("Your electricity bill accurately based on room appliance usage.")

# ডাটাবেসের মানগুলো একদম পরিষ্কার লিস্ট আকারে রাখা হয়েছে
rooms_data = {
    "Living/Bed": {
        "Fan": [75.0, 12.0],
        "Light": [20.0, 6.0],
        "AC": [1500.0, 5.0],
        "TV": [100.0, 4.0],
        "Router": [15.0, 24.0],
    },
    "Kitchen": {
        "Fridge": [200.0, 24.0],
        "Oven": [1200.0, 0.5],
        "Rice Cooker": [800.0, 1.0],
        "Blender": [500.0, 0.2],
    },
    "Bathroom/Other": {
        "Geyser": [2500.0, 1.0],
        "Washing Machine": [600.0, 1.0],
        "Water Pump": [750.0, 0.5],
        "Iron": [1000.0, 0.5],
    },
}

inputs = {}

tabs = st.tabs(list(rooms_data.keys()))

for index, (room_name, devices) in enumerate(rooms_data.items()):
    with tabs[index]:
        st.subheader(f"🏠 {room_name} Room")
        inputs[room_name] = {}
        
        col1, col2, col3 = st.columns(3)
        col1.markdown("**Device**")
        col2.markdown("**Watt**")
        col3.markdown("**Hours**")
        
        for device, defaults in devices.items():
            c1, c2, c3 = st.columns(3)
            c1.text(device)
            
            # এখানে defaults[0] (ওয়াট) এবং defaults[1] (ঘণ্টা) আলাদা করে ফিক্স করা হয়েছে
            w_val = float(defaults[0])
            h_val = float(defaults[1])
            
            w_input = c2.number_input("Watt", min_value=0.0, value=w_val, key=f"{room_name}_{device}_w", label_visibility="collapsed")
            h_input = c3.number_input("Hours", min_value=0.0, max_value=24.0, value=h_val, key=f"{room_name}_{device}_h", label_visibility="collapsed")
            inputs[room_name][device] = {"watt": w_input, "hours": h_input}

st.markdown("---")

if st.button("Calculate Bill", type="primary", use_container_width=True):
    try:
        total_wh = 0
        breakdown_text = "### 📋 Breakdown by Room\n"
        
        for room_name, devices in inputs.items():
            room_wh = 0
            room_breakdown = f"**[{room_name}]**\n"
            
            for device, entries in devices.items():
                watt = float(entries["watt"])
                hours = float(entries["hours"])
                device_wh = watt * hours
                room_wh += device_wh
                room_breakdown += f"* {device}: {watt}W × {hours}h = {device_wh:.1f} Wh\n"
                
            total_wh += room_wh
            breakdown_text += room_breakdown + "\n"
            
        # মাসিক ইউনিট (kWh) হিসাব
        monthly_units = (total_wh / 1000) * 30
        
        # বিদ্যুৎ বিল ট্যারিফ হিসাব
        if monthly_units <= 75:
            bill = monthly_units * 4.85
        elif monthly_units <= 200:
            bill = monthly_units * 6.63
        else:
            bill = monthly_units * 7.95
            
        total_bill = (bill + 40) * 1.05
        
        st.success("🎉 Calculation Successful!")
        st.metric(label="Total Units (Monthly)", value=f"{monthly_units:.2f} kWh")
        st.metric(label="Total Bill", value=f"{total_bill:.2f} BDT")
        st.markdown(breakdown_text)
        
    except Exception as e:
        st.error("Error in calculation. Please ensure all inputs are valid numbers.")
