import tkinter as tk
from tkinter import messagebox, ttk

# ডাটাব্যাস (রুম ও ডিভাইসের ওয়াট এবং ডিফল্ট ঘন্টা)
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


def calculate_bill():
    try:
        total_wh = 0
        breakdown_text = "📋 Breakdown by Room\n" + "=" * 30 + "\n"

        for room_name, devices in inputs.items():
            room_wh = 0
            room_breakdown = f"\n[{room_name} Room]\n"

            for device, entries in devices.items():
                watt = float(entries["watt"].get())
                hours = float(entries["hours"].get())
                device_wh = watt * hours
                room_wh += device_wh
                room_breakdown += (
                    f"• {device}: {watt}W × {hours}h = {device_wh:.1f} Wh\n"
                )

            total_wh += room_wh
            breakdown_text += room_breakdown

        # মাসিক ইউনিট হিসাব
        monthly_units = (total_wh / 1000) * 30

        # বিদ্যুৎ বিল ট্যারিফ হিসাব
        if monthly_units <= 75:
            bill = monthly_units * 4.85
        elif monthly_units <= 200:
            bill = monthly_units * 6.63
        else:
            bill = monthly_units * 7.95

        total_bill = (bill + 40) * 1.05

        # রেজাল্ট বক্সে আউটপুট দেখানো
        result_text = (
            f"🎉 Calculation Successful!\n\n"
            f"Total Units (Monthly): {monthly_units:.2f} kWh\n"
            f"Total Bill: {total_bill:.2f} BDT\n\n" + breakdown_text
        )

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result_text)

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please ensure all inputs contain valid numeric values.",
        )


# উইন্ডো তৈরি
root = tk.Tk()
root.title("Advanced Smart Bill Calculator")
root.geometry("500x650")

# ট্যাব কন্ট্রোল
notebook = ttk.Notebook(root)
notebook.pack(pady=10, fill="both", expand=True)

for room_name, devices in rooms_data.items():
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=room_name)

    inputs[room_name] = {}

    # হেডার লেবেল
    ttk.Label(frame, text="Device", font=("Arial", 10, "bold")).grid(
        row=0, column=0, padx=10, pady=5, sticky="w"
    )
    ttk.Label(frame, text="Watt", font=("Arial", 10, "bold")).grid(
        row=0, column=1, padx=10, pady=5
    )
    ttk.Label(frame, text="Hours", font=("Arial", 10, "bold")).grid(
        row=0, column=2, padx=10, pady=5
    )

    for row_idx, (device, defaults) in enumerate(devices.items(), start=1):
        ttk.Label(frame, text=device).grid(
            row=row_idx, column=0, padx=10, pady=5, sticky="w"
        )

        watt_entry = ttk.Entry(frame, width=10)
        watt_entry.insert(0, str(defaults[0]))
        watt_entry.grid(row=row_idx, column=1, padx=10, pady=5)

        hours_entry = ttk.Entry(frame, width=10)
        hours_entry.insert(0, str(defaults[1]))
        hours_entry.grid(row=row_idx, column=2, padx=10, pady=5)

        inputs[room_name][device] = {"watt": watt_entry, "hours": hours_entry}

# ক্যালকুলেট বাটন
calc_btn = ttk.Button(root, text="Calculate Bill", command=calculate_bill)
calc_btn.pack(pady=10, fill="x", padx=20)

# আউটপুট এরিয়া
output_box = tk.Text(root, height=12, width=55)
output_box.pack(pady=10, padx=20)

root.mainloop()
