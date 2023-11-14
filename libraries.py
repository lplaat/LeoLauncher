import network
import random
import exist
import threading

#downloads file in threads
def downloadThread(files):
    for file in files:
        print('downloading: ' + file['name'])
        network.downloadFile(file['path'], file['url'])

#checks and download all the libraries that are need to launch minecraft
def check(config, system, arch, outputPath, threadsAmount=1):
    paths = []

    librariesList = config['libraries']

    toDownload = []
    for lib in librariesList:
        allowed = False
        if 'rules' in lib.keys():
            for rule in lib['rules']:
                if 'os' in rule.keys():
                    if rule['os']['name'] == system:
                        allowed = rule['action'] == 'allow'
                else:
                    allowed = rule['action'] == 'allow'
        else:
            allowed = True

        if allowed:
            found = False
            if 'natives' in lib:
                for native in lib['natives']:
                    if native == system:
                        found = True
                        libData = lib['downloads']['classifiers'][lib['natives'][system].replace('${arch}', str(arch))]

            if not found:
                libData = lib['downloads']['artifact']
                
            path = outputPath + libData['path']
                        
            paths.append(path)
            if not exist.check(path, libData['sha1']):
                toDownload.append({'url': libData['url'], 'path': path, 'name': lib['name']})

    random.shuffle(toDownload)

    n = len(toDownload) // threadsAmount
    threadsDownloads = []
    if not n == 0:
        threadsDownloads = [toDownload[i:i+n] for i in range(0, len(toDownload), n)]

    if not len(toDownload) == 0 and n == 0:
        threadsDownloads = [toDownload]

    if not len(threadsDownloads) == 0:
        threads = []
        for list in threadsDownloads:
            threads.append(threading.Thread(target=downloadThread, args=(list, )))
            threads[len(threads)-1].start()

        for thread in threads:
            thread.join()

    return paths