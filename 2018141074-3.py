# 2018141074 김진영
# Python version 3.8.8
# 두개의 파일에 있는 문자를 탐색하고 이를 바탕으로 파일끼리의 문자 빈도값에 대하여 비교하는 프로그램 


# 탐색할 문자값 입력

print('※각 문자의 길이는 1로 해주시고 문자들은 ,로 연결해주시기 바랍니다※(예시: a,c,d)')
while True:
    qwe = 0
    print('-'*80)
    search = input('탐색하려는 문자들을 입력해주십시오: ')
    delimeter = ','
    search_list = search.split(delimeter)
    for i in search_list:
        if len(i) != 1:
            qwe += 1
    if qwe >= 1:
        print()
        print('※각 문자의 길이는 1로 해주시고 문자들을 ,로 연결해주시기 바랍니다※(예시: a,c,d)')
    elif qwe == 0:
        break
       
a = set(search_list)

def store_str(x): #파일에 대한 탐색할 문자값의 dictionary생성
    d = dict()
    while True:
        try:
            f=open(x, encoding="UTF-8-sig")
            break
        except:
            print('탐색하고자 하는 파일.형식 이름을 정확히 입력해주십시오\n')
            x = input('File name: ')
    for line in f:
        for c in line:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    f.close
    return d

def make_list(ditny): #dictionary의 빈도값을 기준으로한 list생성
    list_1 = []
    for i in ditny.keys():
        if i in a:
            list_1.append([i,ditny[i]])
            list_1.sort(key=lambda x:x[1])
            list_1 = list_1[::-1]
    return list_1

def no_words(x): #파일에 포함되지 않은 문자 list의 출력
    if len(x) == 0:
        return '없음'
    if len(x) != 0:
        x.sort()
        return x
            
print()
print('※비교할 두개의 파일.형식 이름을 정확히 입력해 주십시오※(예시: Yonsei.txt)')
print('-'*80)

# 비교할 파일값 입력, 총 문자개수 출력, 파일에 포함되지 않은 문자 list생성
name_1 = input('File name: ')
e_1 = store_str(name_1)
b = 0
c = []
for keys in a:
    try:
        b += e_1[keys]
    except:
        c.append(keys)

print('총 {}자, 포함되지 않은 문자 : {}'.format(b,no_words(c)))
sort_dict_1 = make_list(e_1)

name_2 = input('File name: ')
e_2 = store_str(name_2)
d = 0
e= []
for keys in a:
    try:
        d += e_2[keys]
    except:
        e.append(keys)

print('총 {}자, 포함되지 않은 문자 : {}'.format(d,no_words(e)))
sort_dict_2 = make_list(e_2)

# 출력 상위 빈도 순위에 대한 범위 설정
freq = len(a) - max(len(c),len(e))
print()
print('※알고자하는 문자별 출현 상위 빈도의 마지막 순위를 정해진 범위 내의 숫자로 입력해주십시오※')
print('-'*80)
while True:
    try:
        answer = int(input('출현 상위 빈도를 입력해 주십시오(1~{}): '.format(freq)))
        if answer <= freq:
            break
        print('정해진 범위내로 입력해주십시오\n')
    except:
        print('숫자로 입력해주십시오\n')
    

compare_1=[]
compare_2=[]
res=[]

# 탐색할 문자에 대한 각각 파일의 빈도값 및 양쪽파일 모두에 포함된 문자 출력
for i in range(0,answer):
    print('{} {} {} {:.2f}% {} {} {:.2f}%'.format(i+1, sort_dict_1[i][0], sort_dict_1[i][1], 100*sort_dict_1[i][1]/b, sort_dict_2[i][0], sort_dict_2[i][1], 100*sort_dict_2[i][1]/d))
    compare_1 += sort_dict_1[i][0]
    compare_2 += sort_dict_2[i][0]
for s in compare_1:
    if s in compare_2:
        res.append(s)

res.sort()
print()
print('{}위까지 양쪽 파일 모두에 포함된 문자 :{}'.format(answer,(res)))
