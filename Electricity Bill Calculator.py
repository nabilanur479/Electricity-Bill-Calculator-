import tkinter as tk
from tkinter import ttk

def calculate_bill():
    try:
        total_wh = 0
        breakdown_text = "--- Breakdown by Room ---\n"
        
        for room_name, devices in inputs.items():
            room_wh = 0
            breakdown_text += f"\n[{room_name}]\n"
            
            for device, entries in devices.items():
                watt = float(entries["watt"].get())
                hours = float(entries["hours"].get())
                device_wh = watt * hours
                room_wh += device_wh
                
                breakdown_text += f"  • {device}: {watt}W × {hours}h = {device_wh:.1f} Wh\n"
            
            total_wh += room_wh
            
        monthly_units = (total_wh / 1000) * 30
        
        if monthly_units <= 75:
            bill = monthly_units * 4.85
        elif monthly_units <= 200:
            bill = monthly_units * 6.63
        else:
            bill = monthly_units * 7.95
            
        total_bill = (bill + 40) * 1.05
        
        summary_text = f"Total Units: {monthly_units:.2f} kWh\nTotal Bill: {total_bill:.2f} BDT\n\n"
        
        text_output.config(state="normal")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, summary_text + breakdown_text)
        text_output.config(state="disabled")
        
    except ValueError:
        text_output.config(state="normal")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Error: Please enter valid numbers in all fields!")
        text_output.config(state="disabled")

root = tk.Tk()
root.title("Advanced Smart Bill Calculator")
root.geometry("500x700")

rooms_data = {
    "Living/Bed": {"Fan": ("75", "12"), "Light": ("20", "6"), "AC": ("1500", "5"), "TV": ("100", "4"), "Router": ("15", "24")},
    "Kitchen": {"Fridge": ("200", "24"), "Oven": ("1200", "0.5"), "Rice Cooker": ("800", "1"), "Blender": ("500", "0.2")},
    "Bathroom/Other": {"Geyser": ("2500", "1"), "Washing Machine": ("600", "1"), "Water Pump": ("750", "0.5"), "Iron": ("1000", "0.5")}
}

notebook = ttk.Notebook(root, height=280)
notebook.pack(fill="both", expand=False, padx=10, pady=5)

inputs = {}

for room_name, devices in rooms_data.items():
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=room_name)
    
    tk.Label(frame, text="Device", font=("Arial", 9, "bold")).grid(row=0, column=0, padx=15, pady=5)
    tk.Label(frame, text="Watt", font=("Arial", 9, "bold")).grid(row=0, column=1, padx=15, pady=5)
    tk.Label(frame, text="Hours", font=("Arial", 9, "bold")).grid(row=0, column=2, padx=15, pady=5)
    
    inputs[room_name] = {}
    
    for r_idx, (device, defaults) in enumerate(devices.items(), start=1):
        tk.Label(frame, text=device, anchor="w", width=15).grid(row=r_idx, column=0, padx=15, pady=3)
        
        w_entry = ttk.Entry(frame, width=8)
        w_entry.grid(row=r_idx, column=1, padx=15, pady=3)
        w_entry.insert(0, defaults[0])
        
        h_entry = ttk.Entry(frame, width=8)
        h_entry.grid(row=r_idx, column=2, padx=15, pady=3)
        h_entry.insert(0, defaults[1])
        
        inputs[room_name][device] = {"watt": w_entry, "hours": h_entry}

btn = tk.Button(root, text="Calculate Bill", command=calculate_bill, bg="darkgreen", fg="white", font=("Arial", 11, "bold"))
btn.pack(pady=10)

text_output = tk.Text(root, font=("Courier", 10), wrap="word", height=18)
text_output.pack(fill="both", expand=True, padx=15, pady=5)
text_output.config(state="disabled")

root.mainloop()