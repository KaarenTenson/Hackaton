import psutil
import subprocess
import winreg

def get_running_processes():
    # Get a set of all running processes
    running_processes = {process.name().lower() for process in psutil.process_iter(['pid', 'name'])}
    return running_processes

def get_installed_applications():
    installed_apps = set()

    try:
        # Access the Windows Registry to get a list of installed applications
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall") as key:
            for i in range(winreg.QueryInfoKey(key)[0]):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        display_name, _ = winreg.QueryValueEx(subkey, 'DisplayName')
                        installed_apps.add(display_name.lower())
                except Exception as e:
                    pass
    except Exception as e:
        print(f"Error: {e}")

    return installed_apps

def main():
    # Get the sets of running processes and installed applications
    running_processes = get_running_processes()
    installed_apps = get_installed_applications()

    # Check for partial matching and find the intersection
    intersection_set = {process_name for process_name in running_processes if any(app_name in process_name for app_name in installed_apps)}

    # Print the result
    print("Running Processes:", running_processes)
    print("Installed Applications:", installed_apps)
    print("Intersection Set:", intersection_set)

if __name__ == "__main__":
    main()
