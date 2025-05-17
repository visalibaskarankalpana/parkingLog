from datetime import datetime
from colorama import Fore, Style, init
from tabulate import tabulate
import time
from config import DEFAULT_VEHICLES, DEFAULT_SLOTS, SLOT_COLORS

init(autoreset=True)

class ParkingApplication:
    def __init__(self):
        self.data = []
        self.slots = DEFAULT_SLOTS.copy()
        self.load_default()

    def load_default(self):
        for vehicle in DEFAULT_VEHICLES:
            self.create(vehicle["vehicle_number"], vehicle["entry_time"], vehicle["exit_time"], vehicle["slot_number"], default=True)

    def calculate_cost(self, entry, exit):
        fmt = "%Y-%m-%d %H:%M:%S"
        duration = (datetime.strptime(exit, fmt) - datetime.strptime(entry, fmt)).total_seconds() / 3600
        return round(duration * 50, 2)

# Adding a vehicle
    def create(self, vehicle_number, entry_time, exit_time, slot_number, default=False):
        if any(v["slot_number"] == slot_number for v in self.data) and not default:
            print(Fore.RED + f"Slot {slot_number} already occupied." + Style.RESET_ALL)
            return
        cost = self.calculate_cost(entry_time, exit_time)
        record = {
            "vehicle_number": vehicle_number.strip(),
            "entry_time": entry_time.strip(),
            "exit_time": exit_time.strip(),
            "slot_number": slot_number,
            "cost": cost
        }
        self.data.insert(0, record)
        if not default:
            print(Fore.GREEN + "Vehicle added successfully!" + Style.RESET_ALL)

    def read(self):
        if not self.data:
            print(Fore.RED + "No vehicles found.")
            return
        headers = ["No.", "Vehicle Number", "Entry", "Exit", "Slot", "Cost"]
        table = []
        for i, v in enumerate(self.data, start=1):
            color = SLOT_COLORS.get(v['slot_number'], Style.RESET_ALL)
            table.append([
                f"{color}{i}{Style.RESET_ALL}",
                f"{color}{v['vehicle_number']}{Style.RESET_ALL}",
                f"{color}{v['entry_time']}{Style.RESET_ALL}",
                f"{color}{v['exit_time']}{Style.RESET_ALL}",
                f"{color}{v['slot_number']}{Style.RESET_ALL}",
                f"{color}{v['cost']}{Style.RESET_ALL}"
            ])
        print(tabulate(table, headers=headers, tablefmt="pretty"))

# Update vehicle
    def update(self, index, exit_time):
        if 0 <= index < len(self.data):
            self.data[index]["exit_time"] = exit_time.strip()
            self.data[index]["cost"] = self.calculate_cost(self.data[index]["entry_time"], exit_time)
            print(Fore.YELLOW + "Vehicle updated successfully." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid index." + Style.RESET_ALL)

    def delete(self, index):
        if 0 <= index < len(self.data):
            removed = self.data.pop(index)
            print(Fore.RED + f"Vehicle '{removed['vehicle_number']}' deleted." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid index." + Style.RESET_ALL)

# filter
    def filter_by_number(self, vehicle_number):
        filtered = [v for v in self.data if v["vehicle_number"].lower() == vehicle_number.lower()]
        self.display_table(filtered)

    def display_table(self, items):
        if not items:
            print(Fore.RED + "No matching vehicles.")
            return
        headers = ["No.", "Vehicle Number", "Entry", "Exit", "Slot", "Cost"]
        table = []
        for i, v in enumerate(items, start=1):
            color = SLOT_COLORS.get(v['slot_number'], Style.RESET_ALL)
            table.append([
                f"{color}{i}{Style.RESET_ALL}",
                f"{color}{v['vehicle_number']}{Style.RESET_ALL}",
                f"{color}{v['entry_time']}{Style.RESET_ALL}",
                f"{color}{v['exit_time']}{Style.RESET_ALL}",
                f"{color}{v['slot_number']}{Style.RESET_ALL}",
                f"{color}{v['cost']}{Style.RESET_ALL}"
            ])
        print(tabulate(table, headers=headers, tablefmt="pretty"))
        
# sorting using insertion sort
    def insertion_sort(self, key):
        start = time.time()
        for i in range(1, len(self.data)):
            current = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j][key] > current[key]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = current
        end = time.time()
        print(Fore.GREEN + f"Sorted by {key} in {end - start:.6f} seconds." + Style.RESET_ALL)
        self.read()

def main():
    app = ParkingApplication()

    while True:
        print("\n--- Parking Logs ---")
        print("1. Add Vehicle")
        print("2. List All Vehicles")
        print("3. Update Exit Time")
        print("4. Delete Vehicle")
        print("5. Filter by Vehicle Number")
        print("6. Sort Vehicles")
        print("7. Exit")
        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            vno = input("Enter vehicle number: ")
            etime = input("Enter entry time (YYYY-MM-DD HH:MM:SS): ")
            xtime = input("Enter exit time (YYYY-MM-DD HH:MM:SS): ")
            try:
                slot = int(input("Enter slot number: "))
                app.create(vno, etime, xtime, slot)
            except ValueError:
                print(Fore.RED + "Invalid slot number." + Style.RESET_ALL)

        elif choice == "2":
            app.read()

        elif choice == "3":
            try:
                index = int(input("Enter index to update: ")) - 1
                xtime = input("Enter new exit time (YYYY-MM-DD HH:MM:SS): ")
                app.update(index, xtime)
            except ValueError:
                print(Fore.RED + "Invalid input." + Style.RESET_ALL)

        elif choice == "4":
            try:
                index = int(input("Enter index to delete:  ")) - 1
                app.delete(index)
            except ValueError:
                print(Fore.RED + "Invalid input." + Style.RESET_ALL)

        elif choice == "5":
            vno = input("Enter vehicle number: ")
            app.filter_by_number(vno)

        elif choice == "6":
            print("\nSort by:")
            print("1. Slot number")
            print("2. Cost")
            print("3. Entry time")
            sort_choice = input("Enter your choice (1–3): ")
            if sort_choice == "1":
                app.insertion_sort("slot_number")
            elif sort_choice == "2":
                app.insertion_sort("cost")
            elif sort_choice == "3":
                app.insertion_sort("entry_time")
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)

        elif choice == "7":
            print(Fore.YELLOW + "Exiting... thank you!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
