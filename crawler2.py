################################################
#프로그램명: 데이터 베이스 구축
#작성자 : 이준재
#수정일 : 2020-06-12
#팀명 : 파이썬클라스 (4조)
#프로그램 설명: 데이터 크롤링 후 쿼리셋 형태로 저장
################################################

import requests
import urllib.request
from bs4 import BeautifulSoup
import json
import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Main.settings")
import django
django.setup()
import random

from products.models import Product

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 남자 아우터 블레이저  https://store.musinsa.com/app/items/lists/002003
# 남자 상의 반팔        https://store.musinsa.com/app/items/lists/001001    
# 남자 상의 긴팔        https://store.musinsa.com/app/items/lists/001010
# 남자 상의 셔츠        https://store.musinsa.com/app/items/lists/001002
# 남자 하의 조거팬츠    https://store.musinsa.com/app/items/lists/003004/?tag=%EC%A1%B0%EA%B1%B0%ED%8C%AC%EC%B8%A0
# 여자는 종목만 정해주세욥

def parse_crawl():
    r = requests.get('https://store.musinsa.com/app/items/lists/003004/?tag=%EC%A1%B0%EA%B1%B0%ED%8C%AC%EC%B8%A0')

    html = r.content
    soup = BeautifulSoup(html, 'html.parser')

    title_html = soup.select('.li_inner')

    result = []
    
    
    
    for title in title_html:
        nprice = str(title.find_all("span", class_="txt_price_member"))
        nprice = re.sub('<.+?>', '', nprice, 0).strip()
        nprice1 = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', nprice, 0).strip()
        nprice2 = re.sub('\n\n', '', nprice1)

        nbrand = str(title.find_all("p", class_="item_title"))
        nbrand = re.sub('<.+?>', '', nbrand, 0).strip()
        nbrand = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', nbrand, 0).strip()
        nbrand = re.sub('\n\n', '', nbrand, 0).strip()

        ndescription = str(title.find_all("p", class_="list_info"))
        ndescription = re.sub('<.+?>', '', ndescription, 0).strip()
        ndescription = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', ndescription, 0).strip()
        ndescription = re.sub('\n\n', '', ndescription, 0).strip()
        ndescription = re.sub('\n', '', ndescription, 0).strip()

        nimageURL = title.find("img")['data-original']
      
        nitem_num = random.randint(1, 50)

        ncategory1 = "men"
        ncategory2 = "bottom"
        ncategory3 = "jogger-pants"

        print(nimageURL)

        data={
            'price' : nprice2,
            'brand' : nbrand,
            'description' : ndescription,
            'imageURL' : nimageURL,
            'item_num' : nitem_num,
            'category1' : ncategory1,
            'category2' : ncategory2,
            'category3' : ncategory3,
        }
        result.append(data)

    return result

if __name__=='__main__':
    data_dict = parse_crawl()
    for i in data_dict :
        Product(
            price=str(i['price']).replace('[', '').replace(']',''), 
            brand=str(i['brand']).replace('[', '').replace(']',''), 
            description=str(i['description']).replace('[', '').replace(']',''), 
            imageURL=i['imageURL'],
            item_num=i['item_num'],
            category1=i['category1'],
            category2=i['category2'],
            category3=i['category3'],
        ).save()