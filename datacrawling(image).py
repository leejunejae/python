#########################
# 프로그램명 : 상품 사진 크롤링
# 작성자 : 이준재
# 조(팀명) : 파이썬 클라쓰(4조)
# 작성일 : 2020. 05. 24.
# 프로그램 설명 : 옥션에서 남성 의류 카테고리 상품 이미지를 크롤링 한다.
#########################

import requests
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup



# 저장할 이미지 경로 및 이름 (data폴더에 face0.jpg 형식으로 저장)
imageNum = 0
imageStr = "data/face"


url = "https://store.musinsa.com/app/"


r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('img')

a=[]
for m in data:
    b=m.get('src')
    a.append(b)

for i in a:
    print(i)
    # 이미지 경로를 받아 로컬에 저장한다.
#for i in a:
#    imageNum += 1
#    urllib.request.urlretrieve(i, 'data' + str(imageNum) + ".jpg")






