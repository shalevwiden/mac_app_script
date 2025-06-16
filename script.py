import os
import time

import platform

def detect_os():
    if platform.system() == "Darwin":  # macOS
        print('Using MacOS')
    elif platform.system() == "Windows":
        print('Using MacOS')
    else:
        print("Unsupported OS")

# a single app
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
# or use this to get appl;ist from a file
def get_app_list(filename):
    applist=[]
    with open(filename, 'r') as appfile:
        for line in appfile:
            applist.append(line.strip().title())
    return applist

# print(get_app_list('applist.txt'))

# Loop through and open apps
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
