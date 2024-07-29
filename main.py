import multiprocessing
import subprocess

def run_monitor():
    subprocess.run(["python", "monitor.py"])

def run_gui():
    subprocess.run(["python", "gui.py"])

if __name__ == "__main__":
    monitor_process = multiprocessing.Process(target=run_monitor)
    gui_process = multiprocessing.Process(target=run_gui)

    monitor_process.start()
    gui_process.start()

    monitor_process.join()
    gui_process.join()
