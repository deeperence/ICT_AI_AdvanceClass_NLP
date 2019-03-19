from konlpy.corpus import kolaw, kobill
from nltk import Text
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import math # 로그 함수를 사용하기 위해 임포트
import os

path = "C:/windows/fonts/HMKMRHD.ttf" # matplot의 폰트를 지정하기 위한 경로 설정
font = font_manager.FontProperties(fname=path).get_name() # 폰트매니저 객체 생성
rc("font", family=font) # 폰트 변경



# --------------------- 긁어온 네이버 뉴스 기사로 corpus만든 후 분석해보기 -----------------------------
txtfilespath = "./0314_DownloadedNewstxts" # 긁어왔던 기사가 저장되어 있는 폴더
corpus = '' # 뉴스 기사들을 모두 합치기 위한 객체

# FileList = [file for file in os.listdir(txtfilespath) # 14일에 수집한 네이버 뉴스기사 임포트
# for file in os.listdir(txtfilespath):
#     if file.endswith(".txt"):
#         with open("{0}/{1}".format(txtfilespath, file), encoding='UTF-8') as fp: # 파일 한개만 열어서 corpus에 담기
#             corpus.join(fp.read()) # 네이버 뉴스기사 하나가 담긴 corpus 생성
#         tokens = word_tokenize(corpus)
#         textObj = Text(tokens)
#         print(textObj.vocab().most_common(50)) # 자주 나오는 상위 50개 단어를 출력

# corpus = gutenberg.open(gutenberg.fileids()[0]).read() # nltk -> 'Emma' 소설을 받는 corpus 객체
# corpus =kolaw.open(kolaw.fileids()[0]).read() # konlpy -> kolaw를 받는 corpus 객체

# plot을 그리기 위한 변수 정의
# x = range(1, 51) # tuple이기 때문에 range함수를 사용
# y = [row[1] for row in textObj.vocab().most_common(50)]
# logy = [math.log10(_) for _ in y]
#
# 단어의 빈도에 따른 그래프 확인
# plt.plot(x, y, "b-")
# plt.plot(x, logy, "r-")
# plt.xlabel("단어의 순위") # x축 제목 정하기
# plt.ylabel("단어의 빈도") # y축 제목 정하기
# plt.show()

# 로그를 씌운 그래프 출력(zipf's law에 따르면 자기의 순위에 반비례하므로, 거의 리니어한 선이 나와야 한다.)
# 중요도를 기준으로 중요하지 않은 단어(. 등등)를 삭제하고 중요한 단어들을 확인하기 위해 그래프를 그려 보는 것.
# plt.plot(x, logy, "r-")
# plt.xlabel("단어의 순위") # x축 제목 정하기
# plt.ylabel("단어의 빈도(log)") # y축 제목 정하기
# plt.show()
# --------------------- 긁어온 네이버 뉴스 기사로 corpus만든 후 분석해보기 -----------------------------


k = 50 # 10~100
b = 0.5 # 0.4~0.6
x = []
y = []
yy = []
logX = []
logY = []
logYY = []

corpus = "" # 계속 내용을 덧붙이기 위한 빈 객체

# # kobill corpus 분석해보기
# for file in kobill.fileids():
#     corpus += kobill.open(file).read()
#     tokens = word_tokenize(corpus)
#     textObj = Text(tokens)
#
#     x.append(len(textObj))
#     y.append(k * len(textObj)**b)
#     yy.append(len(set(textObj)))
#     logX.append(math.log10(len(textObj)))
#     logY.append(math.log10(k) + math.log10(len(textObj)*b))
#     logYY.append(math.log10(len(set(textObj))))

# 크롤링한 뉴스기사 분석해보기
for file in os.listdir(txtfilespath):
    if file.endswith(".txt"):
        with open("{0}/{1}".format(txtfilespath, file), encoding='utf-8') as f:
            corpus += f.read()

        tokens = word_tokenize(corpus)
        textObj = Text(tokens)

        x.append(len(textObj))
        y.append(k * len(textObj) ** b)
        yy.append(len(set(textObj)))
        logX.append(math.log10(len(textObj)))
        logY.append(math.log10(k) + math.log10(len(textObj) * b))
        logYY.append(math.log10(len(set(textObj))))

plt.plot(x,y, "r-")
plt.plot(x,yy, "b-")
plt.xlabel("전체 단어의 수")
plt.ylabel("고유 단어의 수")
plt.show()

plt.plot(logX,logY, "r-")
plt.plot(logX,logYY, "b-")
plt.xlabel("전체 단어의 수(log)")
plt.ylabel("고유 단어의 수(log)")
plt.show()