import re, nltk
from string import  punctuation
from konlpy.corpus import kolaw, kobill
from nltk import Text
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords # 불용어 사전 임포트
# nltk.download('stopwords') # 1회만 실행
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import math # 로그 함수를 사용하기 위해 임포트
import os

# sentence = "I'd like to lean more something."
# sentence = "I Love you"
# sentence_kor = "파이썬, 자연어처리, 화요일, 힘듦!"
# sentence = "어머님 은 짜장면 이 싫다고 하셨어, 어머님 은 짜장면 이 싫다 어머님"
# sentence = re.sub("[{0}]".format(punctuation), "", sentence)
#
# pattern = re.compile(r"[{0}]".format(re.escape(punctuation))) # 이 중에 하나라도 포함되어 있으면 whitespace로 replace하기 위한 패턴 정의
# threshold = 2
# # stop = stopwords.open("english").read() # 불용어 사전 오픈
# stop = ["은", "는", "이", "가", "을", "를", "에게", "께서"] # 한국어 불용어 사전 정의

# 정규식을 이용하여 마침표(.), 느낌표(!)와 같이 쓸데없는 요소들을 제거
# 단, 신조어와 같이 축약어나 .이 들어가서 구분되는 단어들은 주의해야 한다.
# result = []
# for term in word_tokenize(sentence): # 또는 sentence_kor
#     new = pattern.sub("", term)
#     if new not in stop: # ?)) 구두점이 stop에 들어있지 않을 경우
#         result.append(new)

# print(sentence)
# print(sentence.split()) # ["I'd", 'like', 'to', 'lean', 'more', 'something.']
# print(pattern.sub("", sentence)) # sentence에서 정규식대로 쓸데없는 문자 제거 후 반환 (Id like to lean more something)
# print(result) # ['I', 'd', 'like', 'to', 'lean', 'more', 'something']

# print(sentence_kor)
# print(sentence_kor.split()) # ['파이썬,', '자연어처리,', '화요일,', '힘듦!']
# print(pattern.sub("", sentence_kor)) # sentence에서 정규식대로 쓸데없는 문자 제거 후 반환 (파이썬 자연어처리 화요일 힘듦)
# print(result) # ['파이썬', '자연어처리', '화요일', '힘듦']

# print(len(stopwords.fileids()), stopwords.fileids())
# print(sentence.split(), word_tokenize(sentence))

# for token in word_tokenize(sentence):
#     if token in stop: # stopword인지 검사
#         print("Skipped")
#     else:
#         if len(token) > threshold: # 길이가 threshold를 넘어가는 케이스만 출력
#             print(token)
#             result.append(token)
# print(result)
#
# textObj = Text(word_tokenize(sentence))
# for token in Text(word_tokenize(sentence)).vocab():
#     if token in stop: # stopword인지 검사
#         print("Skipped")
#     else:
#         new = pattern.sub("", token)
#         if new:
#             print(new)
#             result.append(token)
# print(result)
#
# # # print("I".lower()) # 소문자로 변형.
# # for k in textObj.vocab():
# #     print(k, textObj.count(k))
#
# pattern = re.compile(r"\b\w{1,%d}\b") # 짧은 길이의 단음절을 검색하는 정규식 패턴 정의


def ngramUmheol(sentence, n=2):  # 음절 단위로 구분하는 함수. sentence를 받아 2개(n=2)씩 쪼갠다.
    result = []
    tokens_ngram = sentence.split()

    for i in range(len(tokens_ngram) - n + 1):
        # result.append(tokens_ngram[i:i+n]) # 방법1
        # result.append(tuple(tokens_ngram[i:i+n])) # 방법2(튜플로 반환 시 키값을 쓸 수 있음)
        result.append(" ".join(tokens_ngram[i:i + n]))  # 방법3
    return result


# 욕설 필터링을 위한 사전 정의 (반대로 응용하면 중요한 단어를 뽑는 데에도 사용 가능)
stop = ["시발", "씨발"]
result = []
sentence = "시123발 짜증나네 2씨발12323213"
sentence = re.sub("[{0}]".format(punctuation), "", sentence)

for term in sentence.split():
    if term in stop:
        # print("skipped")
        result.append("*"*len(term))
    else:
        flag = True
        # term = re.sub(r"[0-9]+", "", term)

        if pattern.search("w"+term+</w>)
            term = re.sub(r"\B[0-9]+\B", "", term)
        for ngram in ngramUmheol(term):
            if ngram in stop:
                flag=False
                break

        if flag: # true이면
            result.append(term)
        else:
            result.append("*"*len(term))
print(" ".join(result))


'''
* 한글 욕설 필터링 방법 두 가지
1. 한글만 뽑거나 ([가-힣]+)
2. 단어라고 하는 영역 안에 있는 다른 글자를 제거 \w[0-9]+\w

'''
# byte-pair encoding을 활용한 한글 욕설 필터링
def makeTerm(sentence):
    terms = sentence.split() # 3번과정(공백문자가 나오면 '_'으로 치환
    result = []

    for term in terms:
        result.append(" ".join(["<\w"] + ["</w>"])) # 4번과정(term을 list에 넣어 조각낸 후 공백을 삽입한 다음 문장의 끝을 나타내는 태그를 삽입)

    return "_".join(result)
