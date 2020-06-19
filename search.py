################################################
#프로그램명: 상품검색
#작성자 : 이준재
#수정일 : 2020-06-19
#팀명 : 파이썬클라스 (4조)
#프로그램 설명: 기존 검색기능에 검색필터 기능 추가
################################################



from django.shortcuts import render
from django.db.models import F
from products.models import Product

def search(request):
    login = Check_user()
    products = Product.objects.all()
    sdata = request.GET.get('sdata','')
    gender = request.GET.get('gender','')
    clothes_type = request.GET.get('clothes_type','')


    if (sdata==''):
        sdata ='default'

    search = []
    if sdata == 'default':
        if gender == '전체' :
            if clothes_type == '전체':
                for i in products :
                    search.append(i)
            elif clothes_type == '아우터':
                for i in products :
                    if i.category2 == "아우터" :
                        search.append(i)
            elif clothes_type == '상의':
                for i in products :
                    if i.category2 == "상의" :
                        search.append(i)
            elif clothes_type == '하의':
                for i in products :
                    if i.category2 == "하의" :
                        search.append(i)

        elif gender == '남자' :            
            if clothes_type == '전체':
                for i in products :
                    if i.category1 == '남자':
                        search.append(i)
            elif clothes_type == '아우터':
                for i in products :
                    if i.category2 == "아우터" and i.category1 == '남자':
                        search.append(i)
            elif clothes_type == '상의':
                for i in products :
                    if i.category2 == "상의" and i.category1 == '남자' :
                        search.append(i)
            elif clothes_type == '하의':
                for i in products :
                    if i.category2 == "하의" and i.category1 == '남자' :
                        search.append(i)

        elif gender == '여자' :            
            if clothes_type == '전체':
                for i in products :
                    if i.category1 == '여자':
                     search.append(i)
            elif clothes_type == '아우터':
                for i in products :
                    if i.category2 == "아우터" and i.category1 == '여자':
                        search.append(i)
            elif clothes_type == '상의':
                for i in products :
                    if i.category2 == "상의" and i.category1 == '여자':
                        search.append(i)
            elif clothes_type == '하의':
                for i in products :
                    if i.category2 == "하의" and i.category1 == '여자':
                        search.append(i)    
    
    else:
        if gender == '전체' :
            if clothes_type == '전체':
                for i in products :
                    if sdata == i.brand :
                        search.append(i)
                    elif sdata == i.category3 :
                        search.append(i)
            elif clothes_type == '아우터':
                for i in products :
                    if i.Category2 == "아우터" :
                        if sdata == i.brand :
                            search.append(i)
                        elif sdata == i.category3:
                            search.append(i)
            elif clothes_type == '상의':
                for i in products :
                    if i.category2 == "상의" :
                        if sdata == i.brand :
                            search.append(i)
                        elif sdata == i.category3:
                           search.append(i)
            elif clothes_type == '하의':
                for i in products :
                    if i.category2 == "하의" :
                        if sdata == i.brand :
                            search.append(i)
                        elif sdata == i.category3:
                            search.append(i)

        elif gender == '남자' :
                if clothes_type == '전체':
                    for i in products :
                        if i.category1 == '남자' : 
                            if sdata == i.brand :
                                search.append(i)
                            elif sdata == i.category3 :
                                search.append(i)
                elif clothes_type == '아우터':
                    for i in products :
                        if i.category2 == "아우터" and i.category1 == '남자' :
                            if sdata == i.brand :
                                search.append(i)
                            elif sdata == i.category3:
                                search.append(i)
                elif clothes_type == '상의':
                    for i in products :
                        if i.category2 == "상의" and i.category1 == '남자' :
                            if sdata == i.brand :
                                search.append(i)
                            elif sdata == i.category3:
                                search.append(i)
                elif clothes_type == '하의':
                    for i in products :
                        if i.category2 == "하의" and i.category1 == '남자' :
                            if sdata == i.brand :
                                search.append(i)
                            elif sdata == i.category3:
                                search.append(i)

        elif gender == '여자' :
                if clothes_type == '전체':
                    for i in products :
                        if i.category1 == '여자':
                            if sdata == i.brand :
                                search.append(i)
                            elif sdata == i.category3 :
                                search.append(i)
                elif clothes_type == '아우터':
                    for i in products :
                        if i.category2 == "아우터" and i.category1 == '여자':
                            if sdata == i.brand :
                                search.append(i)
                            elif sdata == i.category3:
                                search.append(i)
                elif clothes_type == '상의':
                    for i in products :
                        if i.category2 == "상의" and i.category1 == '여자':
                            if sdata == i.brand :
                                search.append(i)
                            elif sdata == i.category3:
                                search.append(i)
                elif clothes_type == '하의':
                    for i in products :
                        if i.category2 == "하의" and i.category1 == '여자':
                            if sdata == i.brand :
                                search.append(i)
                            elif sdata == i.category3:
                                search.append(i)        

    

    return render(request, 'search.html', {'products':search, 'login':login})