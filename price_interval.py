#################################################
#프로그램명: 가격구간 설정 기능
#작성자 : 이준재
#수정일 : 2020-06-14
#팀명 : 파이썬클라스 (4조)
#프로그램 설명: 원하는 가격대의 상품만 쿼리셋에 저장
#################################################
from django.shortcuts import render
from django.db.models import F
from products.models import Product

def men(request):
    products = Product.objects.all()
    price1 = request.GET.get('price1','')
    if(price1==''):
        price1='0'
    price2 = request.GET.get('price2','')
    if(price2==''):
        price2='1000000'

    men = []
    for i in products :
        if (i.category1 == "men") :
            preplace=i.price.replace(",","")
            preplace=preplace.replace("원","")
            if (int(price1) < int(preplace)) and (int(preplace) < int(price2)):
               men.append(i)
    return render(request, "men.html", {'products' : men})