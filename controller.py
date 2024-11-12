import os
import tkinter as tk
import underground


ROUTE = 'A'
feed = underground.SubwayFeed.get(ROUTE)

data = feed.extract_stop_dict()
global list_of_date_objects

for key in data.keys():
    if key == 'A':
        print(key)
        sub_dict = data.get(key)
        for sub_key in sub_dict.keys():
            if sub_key == 'A38N':
                print(sub_key)
                list_of_date_objects = sub_dict.get(sub_key)
                # for date in list_of_date_objects:
                #     print(date)

for date in list_of_date_objects:
    print(date)

import tkinter as tk
from datetime import datetime, timedelta



x=6
from datetime import datetime, timezone

def get_minutes_until(dt):
    # Make `now` timezone-aware by setting it to UTC or the local timezone
    now = datetime.now(timezone.utc)  # or replace `timezone.utc` with the relevant timezone if needed
    return int((dt - now).total_seconds() / 60)


root = tk.Tk()
root.title("A Train Departures from Fulton Street")
root.geometry("400x300")

# Title Label
title_label = tk.Label(root, text="Upcoming 'A' Train Departures from Fulton Street", font=("Arial", 14))
title_label.pack(pady=10)

# Create frame for table
table_frame = tk.Frame(root)
table_frame.pack(pady=10)

# Table headers
header_time = tk.Label(table_frame, text="Departure Time", font=("Arial", 12, "bold"))
header_time.grid(row=0, column=0, padx=10)
header_minutes = tk.Label(table_frame, text="Minutes Until Departure", font=("Arial", 12, "bold"))
header_minutes.grid(row=0, column=1, padx=10)

# Populate table
for i, dt in enumerate(list_of_date_objects, start=1):
    # Format time
    time_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    minutes_left = get_minutes_until(dt)

    time_label = tk.Label(table_frame, text=time_str, font=("Arial", 10))
    time_label.grid(row=i, column=0, padx=10)

    minutes_label = tk.Label(table_frame, text=str(minutes_left), font=("Arial", 10))
    minutes_label.grid(row=i, column=1, padx=10)

# Run the GUI
root.mainloop()

