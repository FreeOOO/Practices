import requests
from bs4 import BeautifulSoup
import re
def getAllTimeLinks(url):
    res = requests.get(url)
    m = re.search(r'content="text/html;charset=(.{3,10})">',res.text)
    res.encoding = m.group(1)
    soup = BeautifulSoup(res.text,'html.parser')
    arr = soup.select('.time a')
    for qishu in arr[-1:0:-1]:
        getEveryPhaseArticles(url + '/' + qishu['href'])
        #print(url + '/' + qishu['href'])
    #print(res.text)

def getEveryPhaseArticles(url):
    res = requests.get(url)
    m = re.search(r'content="text/html;charset=(.{3,10})">',res.text)
    res.encoding = m.group(1)
    #if url.rfind('/') == url.find('/',7):   #从右边第7位查找
    #    res.encoding = 'gb2312'
    #else:
    #    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    arr = soup.select('.title a')
    for titleLink in arr:
        print(titleLink.text,url[:url.rfind('/') + 1] + titleLink['href'])

def getArticleDetail(url):
    res = requests.get(url)
    m = re.search(r'content="text/html;charset=(.{3,10})">',res.text)
    res.encoding = m.group(1)
    soup = BeautifulSoup(res.text,'html.parser')
    m = re.search('(\d{4})_(\d{1,2})/',url)
    year = int(m.group(1))
    times = int(m.group(2))
    if year > 2013 or (year == 2013 and times >= 3):
        arr = soup.select('.blkContainerSblkCon p')        #2013年第3期及之后的格式
        for p in arr:
            print(p.text)
    elif year > 2011 or (year == 2011 and times >= 13) or \
            (year == 2010 and times <= 20 and times >= 2):
        arr = soup.select('.article div')       #2013第二期及之前
        for p in arr[1:2]:
            #if p.text.find('BAIDU_CLB_') != -1:
            #    continue
            print(p.text)
    else:
        arr= soup.select('.article div div')    #2011第12期及之前的格式
        for p in arr[1:]:
            print(p.text)

    #print(arr[0].contents[5])
    #print('-------------')
    #for temp in arr[0]:
    #    print('-----------------------' + str(temp))
   # print(arr[0].contents)

if __name__ == '__main__':
    url = 'http://www.52duzhe.com'
    getArticleDetail('http://www.52duzhe.com/2012_21/shiershou.html')
    #getAllTimeLinks(url)
    #getEveryPhaseArticles('http://www.52duzhe.com/1_2010_24.html')
