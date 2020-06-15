################################################
#프로그램명: 검색 기능
#작성자 : 이준재
#수정일 : 2020-06-13
#팀명 : 파이썬클라스 (4조)
#프로그램 설명: 검색 대상에 해당하는 쿼리셋 저장
################################################
from django.shortcuts import render
from django.db.models import F
from products.models import Product

def search(request):
    products = Product.objects.all()
    sdata = request.GET.get('sdata','')

    search = []
    for i in products :
        if sdata == i.brand :
            search.append(i)
        elif sdata == i.category2:
            search.append(i)
        elif sdata == i.category3:
            search.append(i)

    return render(request, 'search.html', { 'products': search})
