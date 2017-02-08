import requests
import urllib
r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')
r.encoding = 'utf-8'
arr = r.json()['result']['tracks']
for x in range(3):
    name = arr[x]['name'] + '.mp3'
    link = arr[x]['mp3Url']
    urllib.request.urlretrieve(link,'music/' + name)
