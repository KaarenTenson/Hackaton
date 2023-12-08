import os
import winreg

def list_installed_programs():
    try:
        # Open the registry key containing information about installed programs
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_32KEY)

        # Iterate through subkeys and retrieve program names
        print("List of Installed Programs:")
        for i in range(winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            subkey_path = os.path.join(key_path, subkey_name)
            subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path)
            
            try:
                program_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                print(program_name)
            except FileNotFoundError:
                # Some subkeys may not have DisplayName, ignore them
                pass

            winreg.CloseKey(subkey)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_installed_programs()
