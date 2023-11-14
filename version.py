from os.path import exists as oldExists
import exist
import json

import network

def get(versionID, outputPath, offlineMode=False):
    versionPath = outputPath + 'data.json'
    if offlineMode and oldExists(versionPath):
        versions = json.loads(open(versionPath, 'r').read())
    else:
        try:
            versions = network.get('https://launchermeta.mojang.com/mc/game/version_manifest.json')['versions']
            open(versionPath, 'w').write(json.dumps(versions))
        except:
            print('Failed to get version list!')
            exit()
               
    for version in versions:
        if version['id'] == versionID:
            path = outputPath + version['id'] + '/'
                
            configPath = path + version['id'] + '.json'
            clientPath = path + version['id'] + '.jar'

            if not oldExists(configPath):
                config = network.downloadFile(configPath, version['url'], returnJson=True)
            else:
                config = json.loads(open(configPath, 'r').read())

            if not exist.check(clientPath, config['downloads']['client']['sha1']):
                network.downloadFile(clientPath, config['downloads']['client']['url'])

            return config, clientPath,  path + '/natives'