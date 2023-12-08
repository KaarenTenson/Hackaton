import winreg

def get_installed_applications():
    try:
        # Open the registry key where installed applications are listed
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

        installed_apps = []

        # Iterate through subkeys (each subkey represents an installed application)
        for i in range(winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            subkey_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\\" + subkey_name

            try:
                # Open each subkey to retrieve information
                subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path)
                app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                installed_apps.append(app_name)

            except FileNotFoundError:
                # Some keys might not have the expected values, skip those
                pass

        winreg.CloseKey(key)

        return installed_apps

    except Exception as e:
        print(f"Error: {e}")
        return None

installed_apps = get_installed_applications()
if installed_apps:
    print("Installed Applications:")
    for app in installed_apps:
        print(app)