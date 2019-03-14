# 직접 네이버 뉴스 사이트에서 10개 카테고리로부터 각각 60개씩 기사를 긁어와보기

"""
1. 뉴스 사이트 (https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001) 으로부터 requests로 긁기
2. '가장 많이 본 뉴스'의 하위 6개 카테고리 찾기 (자바스크립트때문에 눈에 보이는것이 다가 아님에 유의, 소스보기를 통해 확인해야 함.)
3. '가장 많이 본 뉴스'의 각 카테고리별 10개의 뉴스 링크 확인 (상대주소로 들어옴)
4. 뉴스링크 주소를 절대주소로 정규화 (0312_main.py 참고)
5. 각 뉴스 다운로드
6. 뉴스 본문 영역 추출
7. 텍스트만 저장
8. 파일 이름 규칙 : '카테고리-고유번호.txt' -> 고유번호는 뉴스 링크에서 확인 가능. (ex. aid=0010695577)
    get방식 파라미터 중 'aid'를 찾아서 넣으면 됨.
총 6개의 카테고리로부터 60개의 기사 수집.

"""

import requests
from bs4 import BeautifulSoup
import re
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

url_naverNewsMain = "https://news.naver.com/"
param_naverNewsMain = {"id":"category_ranking"}
html_naverNewsMain = getDownload(url_naverNewsMain, param_naverNewsMain)
dom_naverNewsMain = BeautifulSoup(html_naverNewsMain.text, 'html.parser')
# NewsCategories = {100:"정치", 101:"경제", 102:"사회", 103:"생활/문화", 104:"세계", 105:"IT'과학"}

NaverHotNewsList = [] # 가장 많이 본 뉴스를 저장하기 위한 빈 리스트
aidNum = [] # 뉴스의 고유번호를 저장하기 위한 빈 리스트
CurrentNewsNum = 0

for tag in dom_naverNewsMain.select('ul.section_list_ranking'):
    for tag2 in tag.find_all('a'):
        if tag2.has_attr('href'):
            aidNum.append(re.findall("aid=([0-9]{10})", tag2['href']))
            # print(tag2['href'])
            NaverHotNewsList.append(requests.compat.urljoin(url_naverNewsMain, tag2['href']))
print(len(aidNum))
# print(NaverHotNewsList) # 절대경로로 변환된 네이버 핫뉴스 목록(60개)
# print(len(NaverHotNewsList[0]))

def txtFileIO(CurrentNewsNum, categoryname):
    f = open("./0314_DownloadedNewstxts/" + categoryname + "-" + str(aidNum[CurrentNewsNum][0]) + ".txt", 'w', encoding='UTF-8')
    f.write(data)
    f.close()
    # print(type(aidNum[CurrentNewsNum]))
    print("file has been created! : " + "./0314_DownloadedNewstxts/" + categoryname + "-" + str(aidNum[CurrentNewsNum][0]) + ".txt" )

for title in NaverHotNewsList:
    html_naverHotNews = getDownload(title)
    dom_naverHotNews = BeautifulSoup(html_naverHotNews.text, 'html.parser')
    data = dom_naverHotNews.find("", {"id":"articleBodyContents"}).text

    if CurrentNewsNum < 10:
        txtFileIO(CurrentNewsNum, "정치")
    elif 10 <= CurrentNewsNum < 20:
        txtFileIO(CurrentNewsNum, "경제")
    elif 20 <= CurrentNewsNum < 30:
        txtFileIO(CurrentNewsNum, "사회")
    elif 30 <= CurrentNewsNum < 40:
        txtFileIO(CurrentNewsNum, "생활문화")
    elif 40 <= CurrentNewsNum < 50:
        txtFileIO(CurrentNewsNum, "세계")
    elif 50 <= CurrentNewsNum < 60:
        txtFileIO(CurrentNewsNum, "IT과학")
    else:
        NotImplementedError()
        break
    CurrentNewsNum = CurrentNewsNum + 1