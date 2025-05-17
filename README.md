

# Parking Lot Management System (Terminal-Based)

A clean and interactive terminal-based Python application for managing vehicle entries in a parking lot.  
It allows users to add, view, update, delete, filter, and sort vehicle records — complete with color-coded outputs and formatted table.

---

## 🚀 Features

- **Add Vehicle**: Input vehicle number, entry/exit times, and assign parking slot.
- **Read Vehicles**: Display all records in a color-coded table based on slot number.
- **Update Exit Time**: Modify the exit time of a parked vehicle and auto-recalculate cost.
- **Delete Vehicle**: Remove a vehicle from the parking lot by index.
- **Filter by Vehicle Number**: Search for vehicles using their number.
- **Sort Records**: Sort all vehicles using insertion sort by:
  - Slot Number
  - Parking Cost
  - Entry Time
- **Cost Calculation**: Automatically computed at ₹50/hour based on entry/exit duration.
- **Color Coding**: Each slot number has a unique color for better visibility.

---

## 🧾 Technologies Used

- Python 3
- `colorama` – for terminal text colors
- `tabulate` – for clean table outputs

---

## 📁 File Structure

```
parking-lot/
│
├── config.py            # Contains default vehicle records and color mappings
├── parkingLogs.py       # Main application logic
```

---

## 🛠️ Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install colorama tabulate
   ```

2. **Run the application**:
   ```bash
   python parkingLogs.py
   ```

---

## 🧠 Example Use

```
--- Parking Logs ---
1. Add Vehicle
2. List All Vehicles
3. Update Exit Time
4. Delete Vehicle
5. Filter by Vehicle Number
6. Sort Vehicles
7. Exit
Enter your choice (1–7):
```

---
