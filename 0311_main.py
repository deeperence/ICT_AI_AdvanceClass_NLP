# Selector를 사용하여 웹 크롤링하기

from bs4 import BeautifulSoup
import requests


# Get 방식을 통해 리스폰스를 받아오는 함수
def getDownload(url, param=None, retries = 3):
    resp = None
    try:
        # 서버를 속이기 위해 headers에 "user-agent":"Mozilla/5.0"를 넣음. (Mozilla/5.0 까지만 넣어도 대부분 ok)
        resp = requests.get(url, param, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"})
        resp.raise_for_status() # 에러를 담고 있음.
    except requests.exceptions.HTTPError as e: # e라는 변수에 에러들을 담을 예정.
        if 500 <= resp.status_code < 600 and retries > 0 : # 500<=resp.status_code < 600이고 최소 0번보다 클때만 반복.
            print("Retries : " + str(retries)) # 현재 몇번 반복되었는지 출력하기 위한 print문
            return getDownload(url, param, retries-1) # 자기 자신을 리턴한 후 retries의 횟수를 줄여줌.
        else: # 만약 500대 에러가 아니고 다른 에러라면 print문 실행
            print(resp.status_code) # 현재 상태를 코드값으로 알려줌. 200:정상, 404:접근금지됨 등등.
            print(resp.reason) # 에러에 대한 상세한 메시지 출력
            print(resp.request.headers) # 에러가 발생했을때의 헤더 출력
    # 아무 문제가 없을경우 resp 객체 반환
    return resp



# Post 방식을 통해 리스폰스를 받아오는 함수
def postDownload(url, param=None, retries = 3):
    resp = None
    try:
        # 주피터 노트북에서는 shift + tab을 누르면 파라미터 설명들이 나옴.
        resp = requests.post(url, param, headers={"user-agent":"Mozilla/5.0"}) # 서버를 속이기 위해 headers에 "user-agent":"Mozilla/5.0"를 넣음. (Mozilla/5.0 까지만 넣어도 대부분 ok)
        resp.raise_for_status() # 에러를 담고 있음.
    except requests.exceptions.HTTPError as e: # e라는 변수에 에러들을 담을 예정.
        if 500 <= resp.status_code < 600 and retries > 0 : # 500<=resp.status_code < 600이고 최소 0번보다 클때만 반복.
            print("Retries : " + str(retries)) # 현재 몇번 반복되었는지 출력하기 위한 print문
            return postDownload(url, param, retries-1) # 자기 자신을 리턴한 후 retries의 횟수를 줄여줌.
        else: # 만약 500대 에러가 아니고 다른 에러라면 print문 실행
            print(resp.status_code) # 현재 상태를 코드값으로 알려줌. 200:정상, 404:접근금지됨 등등.
            print(resp.reason) # 에러에 대한 상세한 메시지 출력
            print(resp.request.headers) # 에러가 발생했을때의 헤더 출력
    # 아무 문제가 없을경우 resp 객체 반환
    return resp



# ----------------------------------------------- selector 사용하기 ----------------------------------------------
# Selector 사용해서 구글로부터 'python' 검색결과의 제목만 10페이지정도 긁어오기
# htmlGoogleSearch = getDownload("https://www.google.com/search", {"q":"파이썬"})
# domGoogleSearch = BeautifulSoup(htmlGoogleSearch.text, "lxml")
# for tag in domGoogleSearch.select(".r h3"): # r 클래스 하위의 모든 h3 태그가 달린 10개를 들고옴.
#     print(tag.text)
#     print(tag.find_parent()["href"])


# Selector 사용해서 네이버로부터 'python' 검색결과의 제목만 10페이지정도 긁어오기
# htmlNaverSearch = getDownload("https://search.naver.com/search.naver", {"query":"파이썬"})
# domNaverSearch = BeautifulSoup(htmlNaverSearch.text, "lxml")
# for tag in domNaverSearch.select(".blog dt > a"):
#     print(tag.text)
#     print(tag["href"])


# 네이트에서 'python' 블로그 검색결과의 제목 가져오기
# htmlNateSearch = getDownload("https://search.daum.net/nate?thr=sbma&w=tot", {"q":"파이썬"})
# domNateSearch = BeautifulSoup(htmlNateSearch.text, "html.parser")
# nodeNateSearch = domNateSearch.find_all("", {"id" : "blogColl"}) # 테스트를 위한 임시 print문
# 사이트 검색 부분의 유일한 key-value쌍인 "disp-attr":"IVR"으로 find한 후 find_all을 통해 해당 트리 아래에 있는 모든 "class":"wrap_tit"를 가져옴.
# for tag in domNateSearch.select("#blogColl a.f_link_b"):
#     print(tag.text)
#     print(tag["href"])
# ---------------------------------------------------------------------------------------------------------------



# ----------------------------------------- Crawling -----------------------------------------------------