#2018141074김진영
#남자 유도선수의 정해진 정보를 입력받아 세계기록 정보 및 달성여부를 출력하는 프로그램

print('남자 유도선수의 정보를 입력하면 세계기록 정보를 확인할 수 있습니다.')
print()

answer = True #변수설정
num1 = 1
num2 = 0

while answer: #선수별 투입값 정보 입력
    while True: #선수이름 미기제시 반복
        name = input('선수이름: ')
        if len(name) >= 1:
            break
    while True: #체중 0초과 아닐경우 반복
        weight = float(input('체중(kg): '))
        if weight > 0:
            break    
    while True: #인상 0초과 아닐경우 반복
        인상 = float(input('인상(kg): '))
        if 인상 > 0:
            break
    while True: #용상 0초과 아닐경우 반복
        용상 = float(input('용상(kg): '))
        if 용상 > 0:
            break

    if weight <= 55: #몸무게별 체급 구별
        standard = 55
        a = 135
        b = 166
        c = 294

    elif weight <= 61:
        standard = 61
        a = 145
        b = 174
        c = 318
        
    elif weight <= 67:
        standard = 67
        a = 155
        b = 188
        c = 339
        
    elif weight <= 73:
        standard = 73
        a = 169
        b = 198
        c = 364

    elif weight <= 81:
        standard = 81
        a = 175
        b = 207
        c = 378

    elif weight <= 89:
        standard = 89
        a = 179
        b = 216
        c = 387

    elif weight <= 96:
        standard = 96
        a = 186
        b = 231
        c = 416

    elif weight <= 102:
        standard = 102
        a = 191
        b = 231
        c = 412

    elif weight <= 109:
        standard = 109
        a = 200
        b = 241
        c = 435
               
    elif weight > 109:
        standard = '+109'
        a = 223
        b = 265
        c = 488

    
    print('_________________________________________________________________________')
    print('{}선수의 체급은 {}kg 입니다.'.format(name, standard))
    print('{}kg급의 남자 역도 세계기록은 다음과 같습니다.'.format(standard))
    print('  인상: {}kg, 용상: {}kg, 종합: {}kg'.format(a, b, c))
    print()
    if 인상 > a: #인상 신기록 조건 달성시 출력
        print('!! {}선수는 인상에서 세계신기록을 기록하였습니다.'.format(name))
        
    if 용상 > b: #용상 신기록 조건 달성시 출력
        print('!! {}선수는 용상에서 세계신기록을 기록하였습니다.'.format(name))
        
    if 인상 + 용상 > c: #종합 신기록 조건 달성시 출력
        print('!! {}선수는 종합에서 세계신기록을 기록하였습니다.'.format(name))
        
    if 인상 > a or 용상 > b or 인상 +용상 > c: #조건 달성시 세계 신기록 총계 증가
        num2 = num2 + 1
        
    print()
    print()
    while True: #미기제 또는 다른 문자값 기입시 반복
        answer = input('계속하시겠습니까?(예/아니오)')
        if answer == '예':
            break
        elif answer == '아니오' :
            break
    if answer == '예':
        print('_________________________________________________________________________')
        num1 = num1 + 1 #조건 달성시 선수 기록 확인값 총계 증가
    elif answer == '아니오':
        answer = False

else : #'아니오' 응답시 while문 종료 및 총계확인
    print('=========================================================================')
    print('총 {}인의 선수 기록을 확인했습니다.'.format(num1))
    print('총 {}인의 선수가 세계 신기록을 기록하였습니다.'.format(num2))
    print('=========================================================================')
