import psutil
import platform
import pandas as pd

def collect_system_performance():
    system_data = []
    
   
    system_info = {
        'OS': platform.system(),
        'Hostname': platform.node()
    }
    
    
    cpu_info = {
        'CPU Usage (%)': psutil.cpu_percent(interval=1),
        'CPU Cores': psutil.cpu_count(logical=False)
    }
    
    
    ram_info = {
        'Total RAM (GB)': round(psutil.virtual_memory().total / (1024 ** 3), 2),
        'RAM Usage (%)': psutil.virtual_memory().percent
    }
    
   
    disk_info = {
        'Total Disk Space (GB)': round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        'Disk Usage (%)': psutil.disk_usage('/').percent
    }
    
   
    network_info = {
        'Sent (MB)': round(psutil.net_io_counters().bytes_sent / (1024 ** 2), 2),
        'Received (MB)': round(psutil.net_io_counters().bytes_recv / (1024 ** 2), 2)
    }
    
    system_data.append({**system_info, **cpu_info, **ram_info, **disk_info, **network_info})
    
    return system_data


def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel('system_performance.xlsx', index=False)


if __name__ == '__main__':
    servers = ['server1', 'server2', 'server3']  
    
    all_system_data = []
    
    for server in servers:
        with psutil.remote_connection(server):
            system_data = collect_system_performance()
            all_system_data.extend(system_data)
    
    save_to_excel(all_system_data)
    print('System performance data saved to system_performance.xlsx')
