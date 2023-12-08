import os
def get_installed_applications():
    try:
        applications_directory = "/Applications"
        files = os.listdir(applications_directory)
        executable_files = [file for file in files if os.access(os.path.join(applications_directory, file), os.X_OK)]
        return executable_files
    except Exception as e:
        print(f"Error: {e}")
        return None

installed_apps = get_installed_applications()
if installed_apps:
    print("Installed Applications:")
    for app in installed_apps:
        print(app)