import subprocess

def disable_application_windows(process_name):
    try:
        subprocess.run(["taskkill", "/IM", process_name, "/F"], check=True)
        print(f"{process_name} successfully disabled.")
    except subprocess.CalledProcessError as e:
        print(f"Error disabling {process_name}: {e}")

# Example: Disable Notepad
while True:
    disable_application_windows("discord.exe")
