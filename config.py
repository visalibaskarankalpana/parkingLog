from colorama import Fore

DEFAULT_SLOTS = [1, 2, 3, 4, 5]

DEFAULT_VEHICLES = [
    {
        "vehicle_number": "MH01AB1234",
        "entry_time": "2025-05-17 08:00:00",
        "exit_time": "2025-05-17 10:00:00",
        "slot_number": 1
    },
    {
        "vehicle_number": "GJ05CD5678",
        "entry_time": "2025-05-17 09:00:00",
        "exit_time": "2025-05-17 11:00:00",
        "slot_number": 2
    },
    {
        "vehicle_number": "KA03EF9012",
        "entry_time": "2025-05-17 07:30:00",
        "exit_time": "2025-05-17 10:30:00",
        "slot_number": 3
    },
    {
        "vehicle_number": "DL04GH3456",
        "entry_time": "2025-05-17 10:00:00",
        "exit_time": "2025-05-17 12:00:00",
        "slot_number": 4
    },
    {
        "vehicle_number": "TN07IJ7890",
        "entry_time": "2025-05-17 08:00:00",
        "exit_time": "2025-05-17 09:30:00",
        "slot_number": 5
    }
]

SLOT_COLORS = {
    1: Fore.RED,
    2: Fore.GREEN,
    3: Fore.YELLOW,
    4: Fore.BLUE,
    5: Fore.MAGENTA
}
