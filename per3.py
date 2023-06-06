import psutil
from openpyxl import Workbook

# Server details
servers = [
    {"name": "Linux_Server_1", "ip": "192.168.1.1"},
    {"name": "Windows_Server_1", "ip": "192.168.1.2"},
]

# Excel file
output_file = "system_performance.xlsx"

# Create Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "System Performance"

# Write headers
headers = ["Server Name", "CPU (%)", "RAM (%)", "Disk Usage (%)", "Network Usage (%)"]
ws.append(headers)

for server in servers:
    server_name = server["name"]
    ip = server["ip"]

    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # RAM usage
    ram_usage = psutil.virtual_memory().percent

    # Disk usage
    disk_usage = psutil.disk_usage('/').percent

    # Network usage
    network_usage = psutil.net_io_counters().percent

    # Write data to Excel
    row = [server_name, cpu_usage, ram_usage, disk_usage, network_usage]
    ws.append(row)

# Save Excel file
wb.save(output_file)
print(f"Data saved to {output_file}")
