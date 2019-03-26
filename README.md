# ICT_AI_AdvanceClass_NLP
* KOIPA의 ICT 인공지능 고급반(NLP class) 수업 코드 정리용 리포지토리입니다.<br>
* 스터디 중 필사한 코드이기 때문에 설명용 주석이 난잡하게 달려 있으며, 실습 위주로 진행되었기 때문에 특정 기능을 확인하실 땐 새 .py를 만들어서 테스트를 진행하시기 바랍니다. (수정 없이 run하실 경우 에러가 발생할 수 있습니다.) <br>
* 실제 응용 시에는 본인 프로젝트에 맞게 리팩토링하신 후 사용하시기 바랍니다.<br>
* 3월 19일 이후 코드부터는 유지보수 편의를 위해 Jupyter notebook으로 작성되어 있습니다.<br>

1. 3월 5일 : 비정형 HTTP 데이터를 다루는 기초적인 방법에 대해 배웠습니다. (HTTP, Urllib, Requests)
2. 3월 7일 : 웹 크롤링 - requests모듈을 사용해 웹 페이지로부터 리스폰스를 받고 cookie와 session 방식으로 로그인을 시도해 보았습니다. 또, 공공데이터포털로부터 대기오염지수를 .json으로 불러와 파싱하는 방법에 대해 배웠습니다. (requests, json)
3. 3월 8일 : DOM tree를 구성하고 태그와 키워드를 통해 원하는 정보를 스크랩하는 방법에 대해 배웠습니다. (requests, BeautifulSoup)
4. 3월 11일 : Selector를 사용한 웹 크롤링 방법(CSS 정보로부터 탐색)에 대해 배웠습니다. (requests, BeautifulSoup)
5. 3월 12일 : BeautifulSoup을 이용해 정적 컨텐츠(ex. 뽐뿌 사이트)를 긁어오는 방법에 대해 알아봅니다. (BeautifulSoup)
6. 3월 13일 : selenium을 이용해 동적 컨텐츠(ex. 네이버 스팸메일함)를 긁어오는 방법에 대해 알아봅니다. (selenium)
7. 3월 14일 : 다음과 KT 사이트에 로그인해보고(Selenium) 네이버 뉴스 사이트에서 핫한 기사 60개를 카테고리별로 긁어오는 프로젝트를 수행했습니다. 
8. 3월 15일 : NLTK, Konlpy 형태소 분석기와 간단한 정규식을 사용하여 토큰화를 수행해 봅니다. (Konlpy, NLTK, re, sent_tokenize)
9. 3월 18일 : 텍스트를 분석하는 다양한 기법들에 대해 알아보고(concordance, similar 등), 14일에 긁은 뉴스 기사들을 실제로 분석해 봅니다. N-gram 기법을 통해 빈도수를 기반으로 어근을 분리해 봅니다. 
10. 3월 19일 : 말뭉치로부터 최빈 단어를 그래프로 시각화하고(matplotlib) 다양한 불용어(구두점, Stopwords)를 처리하는 방법에 대해 알아봅니다.(punctuation)
11 : 3월 20일 : 다양한 방법을 사용하여 Text로부터 형태소 분석을 수행해 봅니다. (English : nltk.pos_tag, Kor : Hannanum, Kkma, Komoran, Okt)
12. 3월 21일 : 구문 분석을 수행한 후 형태소를 분석하여(POS Taggers) 시각화(ParseTree, WordCloud)하는 방법에 대해 알아봅니다. 
13. 3월 22일 : 주어진 텍스트 데이터를 이용해 정보 검색(색인)을 수행하는 방법에 대해 알아보았습니다. (collections.defaultdict 사용, Document-Term Matrix, invertedDocument)

| 사용한 Package | Version | 
|:-------:|:-------:|
|   beautifulsoup4    |   4.7.1    |
|   JPype1    |   0.6.3    |
|   Keras    |   2.2.4   |
|   konlpy      |   0.5.1   |
|   lxml    |   4.3.2    |
|   matplotlib    |   3.0.3    |
|   nltk      |   3.4    |
|   numpy      |   1.16.2    |
|   requests    |  2.21.0    |
|   scipy     |   1.2.1   |
|   seaborn     |   0.9.0   |
|   selenium     |   3.141.0   |
|   soupsieve     |   1.8   |
|   urllib3      |   1.24.1   |

<br>* 3월 19일 이후 코드부터 유지보수 진행중

