class setup():
    def __init__(self):
        with open("setup.txt","r",encoding="UTF-8") as file:
            data = file.readlines()
            if data[0] == "0\n":
                data[0] = "1\n"
                data[1] = installed_apps
                with open("setup.txt","w",encoding="UTF-8") as file:
                    file.writelines(data)


    def welcome(self):
        print("Welcome to Distracto!")

installed_apps = "['Brackets.app', 'Microsoft Teams classic.app', 'Visual Studio Code.app', 'Steam.app', 'Google Chrome.app', 'Numbers.app', 'Sleep Alarm Clock.app', 'Notion.app', 'Day One.app', 'OneDrive.app', 'Spotify.app', 'PyCharm.app', 'iMovie.app', 'Microsoft Word.app', 'Zulip.app', 'EdrawMind.app', 'Safari.app', 'Kindle.app', 'Microsoft Excel.app', 'Utilities', 'zoom.us.app', 'Python 3.11', 'Microsoft Outlook.app', 'Roblox.app', 'Keynote.app', 'Pages.app', 'GarageBand.app', 'Kivy.app', 'Microsoft OneNote.app', 'GlobalProtect.app', 'Messenger.app', 'Final Video Player.app', 'Thonny.app', 'CrystalFetch.app', 'OBS.app', 'Microsoft PowerPoint.app']"
s = setup()
s.welcome()