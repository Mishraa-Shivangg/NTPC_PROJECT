During my internship at NTPC's IT Department, I developed a Python-based GUI using Tkinter to monitor network devices. Key achievements include:

1) GUI Development : Designed and implemented an interactive and user-friendly GUI with Tkinter to enhance network monitoring capabilities.
2) Device Monitoring : Enabled real-time display of device names along with their status (up or down), downtime, and uptime, providing immediate insights into the health and performance of network components.
3) Enhanced Visibility : Provided clear and detailed information about each device’s operational status, which facilitated quicker identification of issues and more efficient network management.

This project significantly improved the department’s ability to monitor network infrastructure, leading to increased operational efficiency and reliability.



This project consists of scripts to monitor device availability and display their statuses in a Tkinter-based GUI.
Files Description
1) monitor.py
  The monitor.py script monitors the availability of devices based on their IP addresses and logs the downtime. Here is a summary of what it does:
  i) Reads the list of devices from devices.csv.
  ii) Defines a check_availability function to ping each device.
  iii) Logs the status (up/down) of each device into downtime_log.csv.
  iv) Schedules the check_availability function to run every 10 seconds.
2) gui.py
   The gui.py script creates a Tkinter-based GUI to display device statuses. Here's what it does:
   i) Reads the downtime_log.csv to load device status data.
   ii) Populates a Tkinter Treeview widget with the device information.
   iii) Updates the GUI every 10 seconds to reflect the latest data.
3) devices.csv
   devices.csv` is a CSV file containing the list of devices to be monitored. 
   i) The devices.csv contains the name of the devices along with it's IP address.
   ii) The content of devices.csv acts as an input for monitor.py
4) main.py
   main.py is a script that runs both monitor.py and gui.py simultaneously using the multiprocessing module.
   i) Runs monitor.py in one process to handle device monitoring.
   ii) Runs gui.py in another process to handle the GUI display.
   iii) Ensures both scripts run concurrently.
