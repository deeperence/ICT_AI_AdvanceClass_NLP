import requests

# --------------------------------- requests 모듈을 사용하여 리스폰스 받아오는 함수 만들기 ----------------------------------------------
# Get 방식을 통해 리스폰스를 받아오는 함수
def getDownload(url, param=None, retries = 3):
    resp = None
    try:
        # 주피터 노트북에서는 shift + tab을 누르면 파라미터 설명들이 나옴.
        resp = requests.get(url, param, headers={"user-agent":"Mozilla/5.0"}) # 서버를 속이기 위해 headers에 "user-agent":"Mozilla/5.0"를 넣음. (Mozilla/5.0 까지만 넣어도 대부분 ok)
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

# print(getDownload("http://www.google.com/search?q=python"))
# print(postDownload("http://pythonscraping.com/pages/files/form.html"))
# ----------------------------------------------------------------------------------------------------------------------------------------




# --------------------------------- requests 모듈의 get, post, head 키워드로 리스폰스 받아오기 --------------------------------------------

# http://httpbin.org/get 페이지에서 get방식으로 HTTP 리스폰스 받아보기
# resp = requests.get("http://httpbin.org/get") # key-value 쌍을 딕셔너리로 넣어야 함.
# print(resp.text)
# print(resp.request.headers) # get방식은 body가 header에 들어가 있다. maximum length가 있기 때문에 전부 다 받아올 수가 없음.
# print(resp.request.body)

# http://httpbin.org/get 페이지에서 post방식으로 HTTP 리스폰스 받아보기
# resp = requests.post("http://httpbin.org/post") # post방식으로 리스폰스를 받아옴
# print(resp.text)
# print(resp.request.headers)
# print(resp.request.body)

# http://httpbin.org/get 페이지에서 head방식으로 HTTP 리스폰스 받아보기
# resp = requests.head("http://httpbin.org/head") # head만 읽어온다.
# print(resp.text)
# print(resp.request.headers) #
# print(resp.request.body)
# -----------------------------------------------------------------------------------------------------------------------------------------

# getDownload()가 에러를 잘 걸러내는지 테스트하기
# url_getDownloadtest = "http://www.crawler-test.com/status_codes/status_" # retries가 3번 출력된 후 500을 반환함.
# html = getDownload(url_getDownloadtest+"500", {"q":"test"})
# print(html.url)

# postDownload()를 이용해서 pythonscraping 받아오기
# url_postDownloadtest = "http://pythonscraping.com/pages/files/processing.php" # 서버에서 처리되서 돌아오는 값을 받아야 하므로 html이 아닌 php로 보내고 받아온다.
# 국내 소규모 사이트는 대부분 이런식으로 구성되어 있다.
# data = {"firstname":"1234", "lastname":"TEST"} # Firstname과 lastname에 각각 값을 넘겨줌.
# html = postDownload(url_postDownloadtest, data) # postDownload함수를 이용해 1234와 TEST를 보내고 리스폰스를 받아옴.
# print(html.text) # http://pythonscraping.com/pages/files/processing.php로부터 받은 결과 출력
# print(html.request.body)
# print(html.status_code)
# print(html.request.headers)

#get으로 login.html을 받아보면 Your browser must be able to use cookies in order to view our site!에러가 뜸.
# url_logintest = "http://pythonscraping.com/pages/cookies/login.html"
# html_logintest = getDownload(url_logintest)
# print(html_logintest.text)

url_logintest = "http://pythonscraping.com/pages/cookies/welcome.php"
logintest_data = {"username":"asdf", "password":"password"}
html_logintest = postDownload(url_logintest, logintest_data) # 쿠키를 받아오려면 post를 한번은 날려 줘야 함.
print(html_logintest.status_code)
print(html_logintest.text)
print(html_logintest.cookies.get_dict())

# 위에서 ID와 PW를 넘겨줄 땐 안되지만, cookie를 넘겨줄때는 로그인이 잘 됨. (쿠키 안에 들어 있는 로그인정보를 이용해 로그인이 된 결과 페이지 접근)
html_logintest = requests.post(url_logintest, cookies = html_logintest.cookies.get_dict(), headers={"user-agent":"Mozilla/5.0"})
print(html_logintest.text)





