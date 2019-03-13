import requests
from bs4 import BeautifulSoup
import time
import random

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

def getDownload(url, param=None, retries=3):
    resp = None
    try:
        resp = requests.get(url, params=param, headers=header)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= resp.status_code < 600 and retries > 0:
            print('Retries : {0}'.format(retries))
            return getDownload(url, param, retries - 1)
        else:
            print(resp.status_code)
            print(resp.reason)
            print(resp.request.headers)

    return resp

url = 'http://example.webscraping.com/places/default/index'
html = getDownload(url)
dom = BeautifulSoup(html.text,'lxml')

# 검색하기 (Find)
results = dom.find('', {'id':'results'})
for tag in results.find_all('a'):
    print(tag.text)

# 선택하기 (Select)
for tag in dom.select('#results a'):
    print(tag.text)

# 이미지 긁기
for tag in dom.select('#results a > img'):
    if tag.has_attr('src'):
        print(requests.compat.urljoin(url, tag['src']))

html = getDownload('http://example.webscraping.com/places/static/images/flags/af.png')
html.headers['Content-Type'] # 'image/png'


# 코드가 있는 경로에 이미지 생성하기
imgSrc = 'http://example.webscraping.com/places/static/images/flags/af.png'

imgName = imgSrc.split('/')[-1]
with open(imgName, 'wb') as f:
    f.write(html.content)


for tag in dom.select('#results a > img'):
    if tag.has_attr('src'):
        src = requests.compat.urljoin(url, tag['src'])

        time.sleep(random.randint(1, 3))

        html = getDownload(src)
        if html.headers['Content-Type'].split('/')[0] == 'image':
            with open(src.split('/')[-1], 'wb') as f:
                f.write(html.content)


# 작성중(0313)...