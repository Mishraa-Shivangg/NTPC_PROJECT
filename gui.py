import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

def load_data():
    if not os.path.exists('downtime_log.csv'):
        return []

    data = pd.read_csv('downtime_log.csv')
    devices = {}

    # ✅ Always pick the latest row for each device
    for _, row in data.iterrows():
        device = row['device']
        ip = row['ip_address']
        timestamp = row['timestamp']
        status = row['status']

        devices[ip] = {
            'device': device,
            'ip_address': ip,
            'down_time': devices[ip]['down_time'] if ip in devices else '',
            'up_time': devices[ip]['up_time'] if ip in devices else '',
            'current_status': status
        }

        if status == 'down':
            devices[ip]['down_time'] = timestamp
        elif status == 'up':
            devices[ip]['up_time'] = timestamp

    return list(devices.values())

def update_table(data):
    for i in tree.get_children():
        tree.delete(i)

    for row in data:
        tree.insert('', tk.END, values=(
            row['device'],
            row['ip_address'],
            row['down_time'],
            row['up_time'],
            row['current_status']
        ))

# GUI setup
root = tk.Tk()
root.title('Device Monitor')

columns = ('Device Name', 'IP Address', 'Down Time', 'Up Time', 'Current Status')
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill=tk.BOTH, expand=True)

def refresh_data():
    new_data = load_data()
    update_table(new_data)
    root.after(10000, refresh_data)  # refresh every 10 sec

refresh_data()
root.mainloop()

