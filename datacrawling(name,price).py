  
#########################
# 프로그램명 : 상품 이름, 가격 크롤링
# 작성자 : 이준재
# 조(팀명) : 파이썬 클라쓰(4조)
# 작성일 : 2020. 05. 24.
# 프로그램 설명 : 옥션에서 남성 의류 카테고리의 상품의 가격과 이름을 크롤링 한다.
#########################

import requests
from bs4 import BeautifulSoup

url = 'http://www.auction.co.kr/category/category13.html' # 옥션 남성 의류 상품 페이지의 상품정보와 가격을 크롤링해옴.

r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')



titles_html = soup.select('.product-list div.content') # 상품 이름 가격

for i in range(30): # 상품 30개 출력
     print(titles_html[i].text)
