import subprocess
import re


def get_installed_applications():
    try:
        # Query user-specific uninstall registry
        user_result = subprocess.run(['reg', 'query', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall', '/s'], capture_output=True, text=True)

        # Query system-wide uninstall registry
        system_result = subprocess.run(['reg', 'query', 'HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall', '/s'], capture_output=True, text=True)

        # Check if both commands were successful
        if user_result.returncode == 0 and system_result.returncode == 0:
            # Use regular expression to extract program names from both outputs
            user_apps = set(re.findall(r'\s+DisplayName\s+REG_SZ\s+(.*)', user_result.stdout))
            system_apps = set(re.findall(r'\s+DisplayName\s+REG_SZ\s+(.*)', system_result.stdout))

            # Combine both sets to get a comprehensive list
            app_names = user_apps.union(system_apps)

            return app_names
        else:
            print(f"Error: Unable to retrieve installed applications. Command returned {user_result.returncode} and {system_result.returncode}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
installed_apps = get_installed_applications()

if installed_apps:
    print("Installed Applications:")
    for app in installed_apps:
        print(app)
else:
    print("No applications found.")
