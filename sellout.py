#################################################
#프로그램명: 매진임박상품
#작성자 : 이준재
#수정일 : 2020-06-19
#팀명 : 파이썬클라스 (4조)
#프로그램 설명: 수량이 10개 미만인 상품만을 진열
#################################################

from django.shortcuts import render
from django.db.models import F
from products.models import Product

def app_sellout(request):
    products = Product.objects.all()

    psellout = []
    for i in products :
        if (i.item_num < 10) :
            psellout.append(i)

    return render(request, 'app_sellout.html', { 'products' : psellout})