import subprocess
import os

base_names = []
all_installed_apps = ['Brackets.app', 'Microsoft Teams classic.app', 'Visual Studio Code.app', 'Steam.app', 'Google Chrome.app', 'Numbers.app', 'Sleep Alarm Clock.app', 'Notion.app', 'Day One.app', 'OneDrive.app', 'Spotify.app', 'PyCharm.app', 'iMovie.app', 'Microsoft Word.app', 'Zulip.app', 'EdrawMind.app', 'Safari.app', 'Kindle.app', 'Microsoft Excel.app', 'Utilities', 'zoom.us.app', 'Python 3.11', 'Microsoft Outlook.app', 'Roblox.app', 'Keynote.app', 'Pages.app', 'GarageBand.app', 'Kivy.app', 'Microsoft OneNote.app', 'GlobalProtect.app', 'Messenger.app', 'Final Video Player.app', 'Thonny.app', 'CrystalFetch.app', 'OBS.app', 'Microsoft PowerPoint.app']
def get_running_processes():
    try:
        result = subprocess.run(['ps', 'axo', 'comm'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')[1:]
        processes_list = []

        for line in output_lines:
            if line:
                name = line.strip()
                processes_list.append(name)

        return processes_list
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_processes_with_string(processes, target_string):
    return [process for process in processes if target_string in process]

def extract_base_name(process_name):
    return os.path.basename(process_name)

def main():
    global base_names
    running_processes = get_running_processes()
    processes_with_app = get_processes_with_string(running_processes, ".app")
    base_names = [extract_base_name(process) for process in processes_with_app]

if __name__ == "__main__":
    main()

base_names_with_extensions = list()
for names in base_names:
    base_names_with_extensions.append(names + ".app")

print(base_names_with_extensions)

print("All installed apps on your computer:")
print(all_installed_apps)
print("\n")

currently_running_apps = list(set(base_names_with_extensions) & set(all_installed_apps))
print("Currently running apps:")
print(currently_running_apps)
print("\n")

currently_not_running_apps = list(set(all_installed_apps) - set(currently_running_apps))
print("Currently not running apps:")
print(currently_not_running_apps)