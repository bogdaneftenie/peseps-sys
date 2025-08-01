import time
import os
import platform
from datetime import timedelta

try:
    import psutil
except ImportError:
    print("❌ Modulul 'psutil' nu este instalat.")
    print("🔧 Instalează-l cu: pip install psutil")
    exit(1)

def format_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return str(timedelta(seconds=int(uptime_seconds)))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage(psutil.disk_partitions()[0].mountpoint)
    uptime = get_uptime()
    sys = f"{platform.system()} {platform.release()}"

    print("🖥️  System Monitor (Live View)")
    print("=" * 40)
    print(f"🧠 CPU Usage:        {cpu_percent:.1f}%")
    print(f"💾 RAM Usage:        {ram.percent:.1f}% ({format_bytes(ram.used)} / {format_bytes(ram.total)})")
    print(f"🗂️  Disk Usage:       {disk.percent:.1f}% ({format_bytes(disk.used)} / {format_bytes(disk.total)})")
    print(f"⏱️  Uptime:           {uptime}")
    print(f"🧩 System:           {sys}")
    print("=" * 40)
    print("⏳ Press Ctrl+C to stop")

if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            print_stats()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped.")
