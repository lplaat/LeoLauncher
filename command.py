import os
from dotenv import load_dotenv

#load configs config
load_dotenv()

#creates minecraft launch command(very ugly)
def generate(config, librariesPaths, assetsPath, profilePath, clientPath, javaLibraryPath):
    command = ['java']

    command += ['-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump']
    command += ['-Dos.name=Windows 10']
    command += ['-Dos.version=10.0']

    command += ['-Djava.library.path=' + os.path.abspath(javaLibraryPath)]

    command += ['-Dminecraft.launcher.brand=LeoLauncher']
    command += ['-Dminecraft.launcher.version=5.3']

    command += ['-cp']
    libs = ''
    for librariesPath in librariesPaths:
        libs += os.path.abspath(librariesPath) + ';'
    command.append(libs + os.path.abspath(clientPath))

    command += [config['mainClass']]
    command += ['--username', os.getenv('MINECRAFT_USERNAME')]
    command += ['--uuid', os.getenv('MINECRAFT_UUID')]
    command += ['--accessToken', os.getenv('MINECRAFT_TOKEN')]
    command += ['--userType', os.getenv('MINECRAFT_TYPE')]

    command += ['--versionType', config['type']]

    command += ['--assetsDir', os.path.abspath(assetsPath)]
    command += ['--version', config['id']]
    command += ['--assetIndex', config['assets']]
    command += ['--xuid', '${auth_xuid}']
    command += ['--gameDir', os.path.abspath(profilePath)]
    command += ['--clientId', '${clientid}']

    return command