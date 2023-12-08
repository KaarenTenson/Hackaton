import os
import subprocess

# READING APPS FROM '/applications' DIRECTORY
def get_installed_applications():
    try:
        applications_directory = "/Applications"
        files = os.listdir(applications_directory)
        executable_files = [file for file in files if os.access(os.path.join(applications_directory, file), os.X_OK)]
        return executable_files
    except Exception as e:
        print(f"Error: {e}")
        return None

app_count = 0
installed_apps_array = list()
installed_apps = get_installed_applications()
if installed_apps:
    for app in installed_apps:
        installed_apps_array.append(app)
        app_count += 1

print("There are "+str(app_count)+" apps installed on your computer.\nYour installed apps are:")
print(installed_apps_array)

# FUNCTION FOR OPENING APPS
def open_application(application_name):
    try:
        subprocess.run(['open', '-a', application_name])
        print(f"{application_name} opened successfully.")
    except Exception as e:
        print(f"Error: {e}")

open_application("")