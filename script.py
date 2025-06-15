import os
import time

def open_app(app):
    os.system(f'open -a "{app}"')
def close_app(app):
    os.system(f'osascript -e \'quit app "{app}"\'')
    # heres the command
    # osascript -e 'quit app "app"'


# List of apps to open
apps_to_open = [
    "Messages",
    "Google Chrome",
    "Safari",
    "FaceTime",
    "Notes"
]
# or use this
def get_app_list(filename):
    return applist

# Loop through and open each one
def openapps(apps,delay=1.5):
    for app in apps:
        # this command is run in terminal
        os.system(f'open -a "{app}"')
        time.sleep(delay)
# os.system runs things in the terminal




garageband='GarageBand'
open_app(garageband)
print('Opened')
# sleep 3 seconds
time.sleep(3)
close_app(garageband)
print('Closed')
