import operator

student={} # 학생 데이터를 저장할 딕셔너리 생성
studenth={} # 정렬하기 위한 딕셔너리 생성
sstudent=[] # 정렬된 딕셔너리를 저장할 리스트 생성

def menu() :
    print("메뉴 생성")
    print("1. 데이터 추가")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 정렬")
    print("0. 종료\n")

def stdinput() :
    print("학생 정보 입력")

    major = input("학과 : ")
    hakbun = input("학번 : ")
    name = input("이름 : ")
    kor = int(input("국어 : "))
    eng = int(input("영어 : "))
    math = int(input("수학 : "))
    avg = (kor + eng + math) / 3  ## 3과목 평균계산
    print("평균 : %d" % avg)

    if avg >= 95:  # 학점계산
        hakjum = 'A+'
    elif avg < 95 and avg >= 90:
        hakjum = 'A0'
    elif avg < 90 and avg >= 85:
        hakjum = 'B+'
    elif avg < 85 and avg >= 80:
        hakjum = 'B0'
    elif avg < 80 and avg >= 75:
        hakjum = 'C+'
    elif avg < 75 and avg >= 70:
        hakjum = 'C0'
    elif avg < 70 and avg >= 65:
        hakjum = 'D+'
    elif avg < 65:
        hakjum = 'F'
    print("학점 : " + hakjum)

    student[name] = [major, hakbun, name, kor, eng, math, avg, hakjum]  # name을 키값으로 학생 데이터 저장
    student[hakbun] = [major, hakbun, name, kor, eng, math, avg, hakjum]  # hakbun을 키값으로 학생 데이터 저장
    studenth[hakbun] = [major, hakbun, name, kor, eng, math, avg, hakjum]  # hakbun을 키값으로 학생 데이터 저장
    print('\n')

def searchstd(inputstd) :
    if(inputstd in student) == True : # 입력값이 student 함수안에 있을때
        print('학생 정보 \n')
        print(student.get(inputstd))  # 해당 학생 정보 출력
    else:
        print("해당하는 정보가 없습니다.")  # 없을 경우
    print('\n')

def deletestd(iptname, ipthakbun) :
    if (iptname in student) == True:  # student안에 입력한 값과 동일한 값이 있으면
        student.pop(ipthakbun)  # 해당 학생의 학번을 키로하는 딕셔너리 삭제
        student.pop(iptname)  # 해당 학생의 이름을 키로하는 딕셔너리 삭제
        studenth.pop(ipthakbun) # 정렬할 딕셔너리의 해당 정보 삭제

    else:
        print("해당하는 정보가 없습니다.")

    print('\n')

def sortstd() :
    i = 0
    sstudent = sorted(studenth.items(), key=operator.itemgetter(1, 0))  # 학과를 1순위 학번을 2순위로 정렬

    while i < len(sstudent):  # sstudent의 크기만큼
        print(sstudent[i][1])  # 딕셔너리의 value들만 출력
        i += 1
    print('\n')


while(1) :
    menu()
    task=int(input("원하는 업무입력 : "))
    print('\n')

    if task==1 : # 학생 정보 입력
        stdinput() # 정보 입력 함수

    elif task==2 : # 학생 정보 출력
        search=input("검색할 학생의 학번 또는 이름 입력 : ")
        searchstd(search) # 입력한 학생 정보 출력 함수

    elif task==3 : # 학생 정보 삭제
        print("삭제할 학생의 학번과 이름 입력")
        deletehakbun=input("학번 : ")
        deletename=input("이름 : ")
        deletestd(deletename, deletehakbun) # 해당하는 정보 삭제 함수 호출


    elif task==4 :
        sortstd() # 정렬


    elif task==0 :
        break # 프로그램 종료