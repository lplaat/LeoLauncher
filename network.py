import requests
import json
import os

#makes a get requests with provided url
def get(url, noJson=False):
    content = requests.get(url).text
    if noJson:
        return content
    else:
        return json.loads(content)

#creates inter path that is provided
def createDirTree(path):
    finalPath = './'
    splittedPath = path.split('/')
    for dirName in splittedPath[1:len(splittedPath)-1]:
        finalPath += dirName + '/'
        try: os.mkdir(finalPath)
        except: pass

#safely downloads a file
def downloadFile(path, url, returnJson=False):
    createDirTree(path)

    with requests.get(url, stream=True, timeout=10) as r:
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

    if returnJson:
        return get(url)