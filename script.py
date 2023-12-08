import subprocess

def get_installed_applications():
    try:
        result = subprocess.check_output(["wmic", "product", "get", "name"])
        applications = result.decode("utf-8").split('\n')[1:-1]
        return applications
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

installed_apps = get_installed_applications()
if installed_apps:
    print("Installed Applications:")
    for app in installed_apps:
        print(app.strip())