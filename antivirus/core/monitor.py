import time
import psutil
from antivirus.core.scanner import scan_file

def monitor_system(signatures):
    """Monitor the system for new processes."""
    print("Starting real-time monitoring... Press Ctrl+C to stop.")
    observed_processes = set()  # Track processes already checked

    try:
        while True:
            for proc in psutil.process_iter(['pid', 'name', 'exe']):
                try:
                    process_info = proc.info
                    process_exe = process_info['exe']
                    process_name = process_info['name']
                    process_pid = process_info['pid']

                    if process_exe and process_pid not in observed_processes:
                        print(f"New process detected: {process_name} (PID: {process_pid})")
                        if scan_file(process_exe, signatures):
                            print(f"ALERT: Malicious process found! {process_name} (PID: {process_pid})")
                        observed_processes.add(process_pid)

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            time.sleep(5)  # Check every 5 seconds

    except KeyboardInterrupt:
        print("Monitoring stopped.")
