import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/s/wh/2017-02-07/doc-ifyafcyx7282218.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
temp = soup.select('.time-source')
print(temp[0].contents)
#print(res.text)
