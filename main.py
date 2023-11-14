import version
import libraries
import assets
import command
import network
import subprocess
import os
from dotenv import load_dotenv

#load configs config
load_dotenv()

#paths
profilesPath = './profiles/'
assetsPath = './assets/'
versionsPath = './versions/'
librariesPath = './libraries/'

#creates paths
os.makedirs(profilesPath, exist_ok=True)
os.makedirs(assetsPath, exist_ok=True)
os.makedirs(versionsPath, exist_ok=True)
os.makedirs(librariesPath, exist_ok=True)

#setting up
config, clientPath, javaLibraryPath = version.get(os.getenv('MINECRAFT_VERSION'), versionsPath, offlineMode=bool(os.getenv('FULLY_OFFLINE')))

librariesPaths = libraries.check(config, os.getenv('SYSTEM'), os.getenv('SYSTEM_ARCH'), librariesPath, threadsAmount=int(os.getenv('DOWNLOAD_THREADS')))
assets.check(config, assetsPath, threadsAmount=int(os.getenv('DOWNLOAD_THREADS')))

network.createDirTree(profilesPath + os.getenv('MINECRAFT_PROFILE'))

#generate launch command
newCommand = command.generate(config, librariesPaths, assetsPath, profilesPath + os.getenv('MINECRAFT_PROFILE'), clientPath, javaLibraryPath)
subprocess.call(newCommand)
