# ICT_AI_AdvanceClass_NLP
* KOIPA의 ICT 인공지능 고급반(NLP class) 수업 코드 정리용 리포지토리입니다.<br>
* 스터디 중 필사한 코드이기 때문에 설명용 주석이 난잡하게 달려 있으며, 실습 위주로 진행되었기 때문에 특정 기능을 확인하실 땐 새 .py를 만들어서 테스트를 진행하시기 바랍니다. (수정 없이 run하실 경우 에러가 발생할 수 있습니다.) <br>
* 실제 응용 시에는 본인 프로젝트에 맞게 리팩토링하신 후 사용하시기 바랍니다.<br>

1. 3월 5일 : 비정형 HTTP 데이터를 다루는 기초적인 방법에 대해 배웠습니다. (HTTP, Urllib, Requests)
2. 3월 7일 : 웹 크롤링 - requests모듈을 사용해 웹 페이지로부터 리스폰스를 받고 cookie와 session 방식으로 로그인을 시도해 보았습니다. 또, 공공데이터포털로부터 대기오염지수를 .json으로 불러와 파싱하는 방법에 대해 배웠습니다. (requests, json)
3. 3월 8일 : DOM tree를 구성하고 태그와 키워드를 통해 원하는 정보를 스크랩하는 방법에 대해 배웠습니다. (requests, BeautifulSoup)
4. 3월 11일 : Selector를 사용한 웹 크롤링 방법(CSS 정보로부터 탐색)에 대해 배웠습니다. (requests, BeautifulSoup)
5. 3월 12일 : BeautifulSoup을 이용해 정적 컨텐츠(ex. 뽐뿌 사이트)를 긁어오는 방법에 대해 알아봅니다. (BeautifulSoup)
6. 3월 13일 : selenium을 이용해 동적 컨텐츠(ex. 네이버 스팸메일함)를 긁어오는 방법에 대해 알아봅니다. (selenium)
7. 3월 14일 : 다음과 KT 사이트에 로그인해보고(Selenium) 네이버 뉴스 사이트에서 핫한 기사 60개를 카테고리별로 긁어오는 프로젝트를 수행했습니다. 
8. 3월 15일 : NLTK, Konlpy 형태소 분석기를 응용하여 문단, 문장, 어절, 정규식, Ngram 단위로 Tokenize를 수행해 보고 불용어를 처리해 봅니다. 
9. 3월 18일 : 텍스트를 분석하는 다양한 기법들에 대해 알아보고(concordance, similar 등), 14일에 긁은 뉴스 기사들을 실제로 분석해 봅니다. 