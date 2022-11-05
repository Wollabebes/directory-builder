import os
import time

# Ask for root directory
rootDir = input("Enter root directory:").replace('"','')
# Enter folder name
projectName = input("Enter project name:").replace('"','')
# Ask for template folders
dirTemplate = input("Enter directory template (.txt):").replace('"','')

print(f"Creating directory to ==> {rootDir}")
os.chdir(rootDir)

f = open(dirTemplate, "r")
dirTemps = f.readlines()

for dir in dirTemps:
    dir = dir.replace("\n", '').format(projectName)
    if not os.path.isdir(dir):
        print(f"Created: {dir}...")
        os.makedirs(dir)
    else:
        print("Folder already existed.")

print("Quitting in 5 seconds...")
time.sleep(5)