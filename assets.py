import network
import json
import threading
import random
import time
import exist

#a thread that downloads assets
def downloadThread(files):
    for file in files:
        print('downloading: ' + file['name'])
        try:
            network.downloadFile(file['path'], file['url'])
        except:
            try:
                time.sleep(1)
                network.downloadFile(file['path'], file['url'])
            except:
                print('failded: ', file['url'])

#checks that all the resources are downloaded
def check(config, outputPath, threadsAmount=1):
    path = outputPath + 'indexes/' + config['assets'] + '.json'
    if not exist.check(path, config['assetIndex']['sha1']):
        network.downloadFile(path, config['assetIndex']['url'])

    objects = json.loads(open(path, 'r').read())['objects']
    
    toDownload = []
    for object in objects:
        objectData = objects[object]
        path = outputPath + 'objects/' + objectData['hash'][0:2] + '/' + objectData['hash']
        if not exist.check(path, objectData['hash']):
            url = 'https://resources.download.minecraft.net/' + objectData['hash'][0:2] + '/' + objectData['hash']
            toDownload.append({'path': path, 'url': url, 'name': object})

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