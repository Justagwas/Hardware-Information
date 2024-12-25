
import os
import platform
import psutil
import wmi
import winreg


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def format_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def fetch_gpu_info_from_registry():
    gpu_info = []
    try:
        video_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DEVICEMAP\VIDEO")
        device_path, _ = winreg.QueryValueEx(video_key, r"\Device\Video0")
        device_key_path = device_path.split(r"\Registry\Machine\\")[1]
        
        device_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, device_key_path)
        for i in range(winreg.QueryInfoKey(device_key)[0]):
            try:
                subkey_name = winreg.EnumKey(device_key, i)
                subkey = winreg.OpenKey(device_key, subkey_name)
                
                try:
                    name, _ = winreg.QueryValueEx(subkey, "Device Description")
                    memory_size, _ = winreg.QueryValueEx(subkey, "HardwareInformation.qwMemorySize")
                    gpu_info.append({
                        "Name": name,
                        "Dedicated Memory": format_bytes(memory_size)
                    })
                except FileNotFoundError:
                    continue
            except OSError:
                break
    except Exception as e:
        return f"Error fetching GPU information: {e}"
    
    return gpu_info

def system_info():
    clear_screen()
    c = wmi.WMI()

    print("=== System Information ===")
    for os_info in c.Win32_OperatingSystem():
        print(f"OS: {os_info.Caption} {os_info.OSArchitecture}")
        print(f"Version: {os_info.Version}")
        print(f"Build Number: {os_info.BuildNumber}")
        print(f"Registered User: {os_info.RegisteredUser}")
        print(f"Driver Version: {os_info.CSDVersion or 'N/A'}")

    for system in c.Win32_ComputerSystem():
        print(f"\nManufacturer: {system.Manufacturer}")
        print(f"Model: {system.Model}")
        print(f"System Type: {system.SystemType}")
        print(f"Total Physical Memory: {int(system.TotalPhysicalMemory) // (1024 ** 3)} GB")

    print("\n=== Python Details ===")
    print(f"Python Version: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

    input("\nPress Enter to return to the main menu.")

def cpu_info():
    clear_screen()
    c = wmi.WMI()
    print("=== CPU Information ===")
    for processor in c.Win32_Processor():
        print(f"Name: {processor.Name}")
        print(f"Cores: {processor.NumberOfCores}")
        print(f"Threads: {processor.NumberOfLogicalProcessors}")
        print(f"Max Clock Speed: {processor.MaxClockSpeed} MHz")
        print(f"Architecture: {processor.Architecture}")
    input("\nPress Enter to return to the main menu.")

def memory_info():
    clear_screen()
    c = wmi.WMI()
    print("=== Memory Information ===")
    for memory in c.Win32_PhysicalMemory():
        print(f"Capacity: {int(memory.Capacity) // (1024 ** 3)} GB")
        print(f"Speed: {memory.Speed} MHz")
        print(f"Manufacturer: {memory.Manufacturer}")
    input("\nPress Enter to return to the main menu.")

def storage_info():
    clear_screen()
    c = wmi.WMI()
    print("=== Storage Information ===")
    for disk in c.Win32_DiskDrive():
        print(f"Model: {disk.Model}")
        print(f"Size: {int(disk.Size) // (1024 ** 3)} GB")
        print(f"Interface Type: {disk.InterfaceType}")
    input("\nPress Enter to return to the main menu.")

def gpu_info():
    clear_screen()
    print("=== GPU Information ===")

    c = wmi.WMI()
    gpus = c.Win32_VideoController()
    for index, gpu in enumerate(gpus):
        print(f"\nGPU {index + 1}:")
        print(f"  Name: {gpu.Name}")
        print(f"  Driver Version: {gpu.DriverVersion}")
        try:
            memory = gpu.AdapterRAM // (1024 ** 3) if gpu.AdapterRAM else "Unknown"
            if memory <= 0:
                print(f"  Adapter RAM: N/A")
            else:print(f" Adapter RAM: {memory} GB")
        except Exception:
            print(f"  Adapter RAM: Unable to fetch")
    input("\nPress Enter to return to the main menu.")

def network_info():
    clear_screen()
    c = wmi.WMI()
    print("=== Network Adapter Information ===")
    for adapter in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        print(f"Description: {adapter.Description}")
        print(f"MAC Address: {adapter.MACAddress}")
        print(f"IP Address: {adapter.IPAddress[0]}")
    input("\nPress Enter to return to the main menu.")

def main_menu():
    while True:
        clear_screen()
        print("=== Hardware Information Menu ===")
        print("1. System Information")
        print("2. CPU Information")
        print("3. Memory Information")
        print("4. Storage Information")
        print("5. GPU Information")
        print("6. Network Information")
        print("7. Exit")
        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            system_info()
        elif choice == "2":
            cpu_info()
        elif choice == "3":
            memory_info()
        elif choice == "4":
            storage_info()
        elif choice == "5":
            gpu_info()
        elif choice == "6":
            network_info()
        elif choice == "7":
            clear_screen()
            print("Terminating.")
            break
        else:
            input("\nInvalid, Press Enter to try again.")

if __name__ == "__main__":
    main_menu()
