import urllib.request
import urllib
import json
import os
import os.path
import webbrowser
pathCWD = os.getcwd()
images = []
if os.path.isfile(f'{pathCWD}/deps.cfg') == False:
    apiKey = input('APIKEY: ')
    seed = input('SEED: ')
    dictonary = {'apikey': apiKey,'seed':seed}
    f = open('deps.cfg','w')
    f.write(str(dictonary))
    f.close()
failed = False
f = open(f'{pathCWD}/deps.cfg', 'r')
r = f.read()
f.close()
d = eval(r)
seed = d['seed']
apiKey = d['apikey']
txt = urllib.request.urlopen(f'https://api.curator.io/v1/feeds/{seed}/posts/?api_key={apiKey}').read()
my_json = txt.decode('utf-8')
data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
f = open(f'{pathCWD}/jsontext.txt', 'w')
f.write(s)
f.close()
jsonFile = open(f'{pathCWD}/jsontext.txt', 'r', encoding='utf-8')
json_File = json.load(jsonFile)
jsonFile.close()
os.remove(f'{pathCWD}/jsontext.txt')
index = 0
x = 0
f = 0
while x < 9:
    try:
        urlText = json_File['posts'][index]['images'][0]['url']
        images.append(urlText)
        x += 1
    except IndexError:
        f += 1
        if f > 200:
            failed = True
            break
    index += 1
if failed == False:
    index = 0
    for x in images:
        f = open(f'{pathCWD}/images/image{index}.jpg', 'wb')
        f.write(urllib.request.urlopen(images[index]).read())
        f.close()
        index += 1
