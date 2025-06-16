import os
import time

import platform

'''
June 15, 2025
Mac App Opening and Closing Script
Sample Usage of some of the defined functions in main()
'''

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

def get_downloaded_apps():
    splitpath=os.getcwd().split('/')
    beginning_of_path=f'/{splitpath[0]}/{splitpath[1]}'
    appsdir=os.path.join(beginning_of_path,'/Applications')
    # print(firsthalf)
    #  get a list of all apps in the users folder
    downloadedapps=os.listdir(appsdir)
    # now format to remove .app    
    downloadedapps_formatted=[]

    for app in downloadedapps:
        formatted_app=os.path.splitext(app)[0]
        downloadedapps_formatted.append(formatted_app)
    return downloadedapps_formatted

print(f'Downloaded apps function:\n{get_downloaded_apps()}')

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


def main():
    # open a fourth of all the apps, then close them
    downloaded_apps=get_downloaded_apps()
    for app_index in range(len(downloaded_apps)):
        if (app_index+1)%4==0:
            open_app(downloaded_apps[app_index])
            time.sleep(3)
            close_app(downloaded_apps[app_index])
        
