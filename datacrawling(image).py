#########################
# 프로그램명 : 상품 사진 크롤링
# 작성자 : 이준재
# 조(팀명) : 파이썬 클라쓰(4조)
# 작성일 : 2020. 05. 24.
# 프로그램 설명 : 옥션에서 남성 의류 카테고리 상품 이미지를 크롤링 한다.
#########################

import requests
from bs4 import BeautifulSoup

url = 'http://www.auction.co.kr/category/category13.html'

r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
eee = soup.find_all("img", class_="line")


# '리스트 a'에 이미지 링크를 담아서 a에 담긴 이미지 주소를 for문으로 출력시
a = []
for m in eee:
    if 'itemimage' in m.get('src'):
        b = m.get('src')
        a.append(b)  # 이미지인것만 리스트에 삽입

for i in a:
    print(i)
