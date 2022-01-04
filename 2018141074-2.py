# 2018141074 김진영
# Python version 3.8.8
# 날짜별, 지역별, 기간별 코로나 확진자수 및 확진자 대비 사망자, 감염경로 조사자 확인에 대한 프로그램 


# 변수 설정
countlines_1 = 0
countlines_2 = 0
countlines_3 = 0
t=[]
r=[]
MM=['01','02','03','04','05','06','07','08','09','10','11','12']
answer = True


while True: # 파일 열기 및 날짜/지역 리스트, 총 건수, 감염경로 조사자, 사망자 추출 
    name = input('File :')
    try:
        f=open(name)
        while True:    
            line = f.readline()
            if len(line)==0:
                    break
            delimeter=","
            x = line.split(delimeter)
            t.append(x[1])
            r.append(x[5])
            if 'Y' in line:
               countlines_1 = countlines_1 + 1
            if '감염경로 조사중' in line:
                countlines_2 = countlines_2 + 1
            if '사망' in line:
                countlines_3 = countlines_3 + 1
        
        f.close
        break;
    
    except:
        print('올바르지 않은 파일이름입니다. 다시입력해주세요.')

# 리스트 정리 및 날짜 최대 최소 추출
r.remove('지역')
t.remove('확진일')
t.sort
small = min(t)
large = max(t)

# 날짜와 지역에 따른 확진자수를 세는 함수 설정
def year_month_region(x, z):
    res_1 = 0
    if menu == '1':
        for i in range(len(t)):
            if x == t[i][:7]:
                res_1 = res_1 + 1
        return res_1
    elif menu == '2':
        for i in range(len(t)):
            if x == t[i][:7] and z == r[i]: 
                res_1 = res_1 + 1
        return res_1

print()
print('불러오신 자료는 {} ~ {} 사이의 자료이며, 총{}건 입니다.'.format(small,large,countlines_1))

# 메뉴 선택목록 반복 시행
while answer:
    print('-'*80)
    print('메뉴')
    print('1. 년, 월을 입력받아 확진일이 해당 년, 월인 확진자수를 출력합니다.')
    print('2. 년, 월과 원하는 지역을 입력받아 해당 년, 월에 해당 지역의 확진자수를 출력합니다.')
    print('3. 시작-년-월과 마지막 년-월을 입력받아 확진일이 이 기간 중인 총 확진자수를 출력합니다.')
    print('4. 사망자수와 총 확진자수 대비 %를 출력합니다.')
    print('5. 감염경로 조사중인 확진자 수와 총 확진자수 대비 %를 출력합니다.')
    print('0. 프로그램을 종료합니다.')
    print('-'*80)
    
# 메뉴 선택오류 발생시 반복
    while True:
        menu = input('메뉴번호: ')
        number=['0','1','2','3','4','5']
        if menu in number:
            break;
        
        else:
            print('메뉴값을 다시 입력해 주십시오')
            
# 각 메뉴별 결과값 도출
    if menu == '0':
            print('-'*80)
            print('프로그램이 종료되었습니다.')
            answer = False
    elif menu=='1' or menu=='2':
        while True:
            year_month = input('년-월을 입력해 주십시오(YYYY-MM): ')
            if small[:7] <= year_month <= large[:7] and int(year_month[0:4]) >= 2019 and year_month[5:7] in MM and year_month[4]=='-':
                break
        if menu == '1':
            print('메뉴번호 1: {}명'.format(year_month_region(year_month,0)))
        elif menu == '2':
            while True:
                region = input('지역: ')
                if year_month_region(year_month,region) >= 1:
                    print('메뉴번호 2: {}명'.format(year_month_region(year_month,region)))
                    break;
                else:
                    print('정확한 지역을 다시입력해주십시오.')
    elif menu == '3':
        while True:
            try:
                while True:
                    start = input('시작하는 년-월을 입력해주십시오(YYYY-MM): ')
                    if int(start[0:4]) >= 2019 and start[5:7] in MM and start[4]=='-':
                        break
                while True:
                    finish = input('끝나는 년-월을 입력해주십시오(YYYY-MM): ')
                    if int(finish[0:4]) >= 2019 and finish[5:7] in MM and start[4]=='-':
                        break
                if small[:7] <= start <= finish <= large[:7]:
                    break
            except:
                print('년, 월을 숫자로 입력해주세요')
        res_1=0
        for i in range(len(t)):
            if start <= t[i][:7] <= finish:
                res_1 = res_1 + 1
        print('메뉴번호 3: {}명'.format(res_1))                
    elif menu == '4':
        print('메뉴번호 4: {}({:.1f}%)명'.format(countlines_3, countlines_3*100/countlines_1))
    elif menu == '5':
        print('메뉴번호 5: {}({:.1f}%)명'.format(countlines_2, countlines_2*100/countlines_1))
