import subprocess

def close_application(application_name):
    try:
        subprocess.run(['pkill', '-f', application_name])
        print(f"{application_name} closed successfully.")
    except Exception as e:
        print(f"Error: {e}")

currently_running_applications = ['Microsoft Excel.app', 'Google Chrome.app', 'GlobalProtect.app', 'Microsoft Word.app', 'Microsoft Outlook.app', 'Day One.app', 'Notion.app', 'Zulip.app', 'Safari.app', 'OneDrive.app']
for app in currently_running_applications:
    close_application(app)