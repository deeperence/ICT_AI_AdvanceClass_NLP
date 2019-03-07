import requests

# --------------------------------- requests 모듈을 사용하여 리스폰스 받아오는 함수 만들기 ----------------------------------------------

# def getDownload(url, param=None, retries = 3):
#     resp = None
#     try:
#         주피터 노트북에서는 shift + tab을 누르면 파라미터 설명들이 나옴.
        # resp = requests.get(url, param, headers={"user-agent":"Mozilla/5.0"}) # 서버를 속이기 위해 headers에 "user-agent":"Mozilla/5.0"를 넣음. (Mozilla/5.0 까지만 넣어도 대부분 ok)
        # resp.raise_for_status() # 에러를 담고 있음.
    # except requests.exceptions.HTTPError as e: # e라는 변수에 에러들을 담을 예정.
    #     if 500 <= resp.status_code < 600 and retries > 0 : # 500<=resp.status_code < 600이고 최소 0번보다 클때만 반복.
    #         return getDownload(url, param, retries-1) # 자기 자신을 리턴한 후 retries의 횟수를 줄여줌.
    #     else: # 만약 500대 에러가 아니고 다른 에러라면 print문 실행
    #         print(resp.status_code)
    #         print(resp.reason)
    #         print(resp.request.headers)
    # 아무 문제가 없을경우 resp 객체 반환
    # return resp
#
# print(getDownload("http://www.google.com/search?q=python"))
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
resp = requests.head("http://httpbin.org/head") # head만 읽어온다.
print(resp.text)
print(resp.request.headers) #
print(resp.request.body)
# -----------------------------------------------------------------------------------------------------------------------------------------