#일반코드
colors=["a","b","c","d","e"]
result = ""
for s in colors:
    result += s
print(result)


#Split 함수
#string type의 값을 나눠서 List 형태로 변환
items = 'zero one two three'.split() #빈칸을 기준으로 문자열 나누기
print(items)

example = 'python, query, javascript'
print(example.split(",")) #","을 기준으로 문자열 나누기

a, b, c = example.split(",") #리스트에 있는 각 값을 a,b,c 변수로 unpacking
print(a)


#Join 함수
#String List를 합쳐 하나의 String으로 반환할 때 사용
colors=["a","b","c","d","e"]
results = "".join(colors)
print(results)

results = " ".join(colors) #연결시 빈간 1칸으로 연결
print(results)

results = ",".join(colors) #연결시 ","으로 연결
print(results)

results = "-".join(colors) #연결시 "-"으로 연결
print(results)


#List comprehension
#기존 List 사용하여 간단히 다른 List를 만드는 기법
#포괄적인 List, 포함되는 리스트라는 의미로 사용됨
#파이썬에서 가장 많이 사용되는 기법 중 하나
#일반적으로 for + append 보다 속도가 빠름

#일반코드
result=[]
for i in range(10):
    result.append(i)
print(result)

#List comprehension(1/3)
result = [i for i in range(10)]
print(result)
result = [i for i in range(10) if i % 2 == 0]
print(result)

#List comprehension(2/3)
word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
print(result)
result = [i+j for i in word_1 for j in word_2 if not(i==j)] #i와 j가 같다면 추가하지 않음
print(result)

#List comprehension(3/3)
words = "The quick brown fox jumps over the lazy dog".split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)
for i in stuff:
    print(i)

case_1= ["A","B","C"]
case_2= ["D","E","F"]
result = [a+b for a in case_1 for b in case_2] #i_dimension
print(result)
result = [[a+b for a in case_1] for b in case_2] #2_dimension
print(result)

#Enumerate
#List의 element를 추출할 때 번호를 붙여서 추출
for i, v in enumerate(['tic', 'tac', 'toe']): #list의 있는 index와 값을 unpacking
    print(i,v)

mylist = ["a","b","c","d"]
a = list(enumerate(mylist)) #list의 있는 index와 값을 unpacking하여 list로 저장
print(a)
print(type(enumerate(mylist)))
a = {i:j for i,j in enumerate('Yonsei Univ is an academic institute located in South Korea'.split())}
print(a)

#Zip
#두 개의 list의 값을 병렬적으로 추출함
alist=['a1','a2','a3']
blist=['b1','b2','b3']
a = [zip(alist,blist)]
print(a)
a = {i:j for i,j in zip(alist,blist)}
print(a)

a,b,c = zip((1,2,3),(10,20,30),(100,200,300)) #각 tuple의 같은 index끼리 묶음
print(a,b,c)

a = [sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))] #각 Tuple 같은 index를 묶어 합을 list로 변환
print(a)
for x in zip((1,2,3), (10,20,30), (100,200,300)): #zip type은 Tuple
    print(x) 

#Enumerate & Zip
alist=['a1','a2','a3']
blist=['b1','b2','b3']
for i, (a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)
