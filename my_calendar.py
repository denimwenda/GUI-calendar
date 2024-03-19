import calendar
import tkinter as tk
from tkinter import ttk

def show_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())
    cal_data = calendar.monthcalendar(year, month)
    month_str.set(calendar.month_name[month])
    year_str.set(year)
    
    for i in range(6):
        for j in range(7):
            cal_labels[i][j].configure(text=str(cal_data[i][j]))

root = tk.Tk()
root.title("GUI Calendar")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Year entry
ttk.Label(frame, text="Year:").grid(column=0, row=0)
year_str = tk.StringVar()
year_entry = ttk.Entry(frame, textvariable=year_str, width=6)
year_entry.grid(column=1, row=0)
year_entry.insert(0, str(calendar.datetime.datetime.now().year))

# Month entry
ttk.Label(frame, text="Month:").grid(column=2, row=0)
month_str = tk.StringVar()
month_entry = ttk.Entry(frame, textvariable=month_str, width=6)
month_entry.grid(column=3, row=0)
month_entry.insert(0, str(calendar.datetime.datetime.now().month))

# Show calendar button
show_button = ttk.Button(frame, text="Show Calendar", command=show_calendar)
show_button.grid(column=4, row=0)

# Calendar display
cal_labels = [[None]*7 for _ in range(6)]
for i in range(6):
    for j in range(7):
        cal_labels[i][j] = ttk.Label(frame, text="", width=4, relief="groove")
        cal_labels[i][j].grid(column=j, row=i+1, padx=5, pady=5)

# Initialize calendar with current month
show_calendar()

root.mainloop()