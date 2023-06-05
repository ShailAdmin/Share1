import psutil
from openpyxl import Workbook

def collect_system_performance(server_list):
    wb = Workbook()
    ws = wb.active

    
    ws.append(["Server", "CPU Usage (%)", "Memory Usage (%)"])

    for server in server_list:
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_percent = psutil.virtual_memory().percent

      
        ws.append([server, cpu_percent, mem_percent])

    return wb

if __name__ == "__main__":
    servers = ["server1", "server2", "server3"]

    wb = collect_system_performance(servers)
    wb.save("system_performance.xlsx")
