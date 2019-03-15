# 이 코드에서는 한국어 형태소 분석기를 응용하는 방법에 대해 알아봅니다.

from konlpy.tag import Kkma

ma = Kkma()
print(ma.pos("오늘은 불금입니다.")) # 테스트