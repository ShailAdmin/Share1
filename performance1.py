import psutil
import pandas as pd


servers = ['server1', 'server2', 'server3']


df = pd.DataFrame(columns=['Server', 'CPU Usage (%)', 'RAM Usage (%)', 'Disk Usage (%)', 'Network Usage (MB/s)'])


for server in servers:
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_usage = psutil.net_io_counters().bytes_sent / 1024 / 1024

  
    df = df.append({
        'Server': server,
        'CPU Usage (%)': cpu_usage,
        'RAM Usage (%)': ram_usage,
        'Disk Usage (%)': disk_usage,
        'Network Usage (MB/s)': network_usage
    }, ignore_index=True)


df.to_excel('system_performance.xlsx', index=False)
