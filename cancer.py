import os

def get_installed_apps():
    # Specify the directory where you want to search for .exe files
    target_directory = "C:\\Program Files"  # You can change this to the desired directory

    # Initialize an empty set to store application names
    app_names = set()

    try:
        # Traverse through the specified directory
        for root, dirs, files in os.walk(target_directory):
            for file in files:
                # Check if the file ends with .exe
                if file.endswith(".exe"):
                    # Extract the application name by removing the .exe extension
                    app_name = os.path.splitext(file)[0]
                    app_names.add(app_name)

    except Exception as e:
        print(f"An error occurred: {e}")

    return app_names

# Call the function and print the result
installed_apps = get_installed_apps()
print("Installed Applications:")
for app in installed_apps:
    print(app)
