# 2018141074 김진영
# Python version 3.8.8
# 각 근로자 형태에 맞는 급여 계산 및 그래프화하는 프로그램

# 변수 설정
t=[]
s=[]
v=[]
u=[]
w=[]
h=[]
k=0
p=-1

# 파일 오픈 및 파일 정보 리스트화
print('해당 근무자의 근무시간 입력시 직무에 맞는 급여가 출력됩니다.\n')
f = open('employee.txt', encoding="UTF-8-sig")
while True:
    line = f.readline()
    p += 1
    if not line:
        break
    delimeter=","
    x = line.split(delimeter)
    t.append(x[0])
    v.append(x[1])
    s.append(x[2])
    if x[1] == 'M':
        u.append(x[3][:2])
f.close

# 상위 class 설정
class employee:
    def __init__(self,name, worktime):
        self.name = name
        self.worktime = worktime
    
# 하위 class 설정
class hour(employee):
    def __init__(self, name, worktime, money_hour):
        employee.__init__(self, name, worktime)
        self.money = int(money_hour)

    def tell(self):
        if worktime >= 40:
            print('시급근로자 {} : 근무시간 = {} 주급 = {} 시급= {}'.format(self.name, self.worktime, int(40*self.money + (worktime - 40)*self.money*1.5), self.money))    
        else:
            print('시급근로자 {} : 근무시간 = {} 주급 = {} 시급= {}'.format(self.name, self.worktime, worktime*self.money, self.money))
        h.append(worktime*self.money)
        
class year(employee):
    def __init__(self, name, worktime, money_year):
        employee.__init__(self, name, worktime)
        self.money = int(money_year)

    def tell(self):
        print('시급근로자 {} : 근무시간 = {} 주급 = {} 연봉 = {}'.format(self.name, self.worktime, self.money//52, self.money))
        h.append(self.money//52)
        
class manager(year):
    def __init__(self, name, worktime, money_year, bonus):
        year.__init__(self, name, worktime, money_year)
        self.bonus = int(bonus)

    def tell(self):
        print('시급근로자 {} : 근무시간 = {} 주급 = {} 연봉 = {} 보너스 = {}' .format(self.name, self.worktime, self.money//52 + self.bonus, self.money, self.bonus))
        h.append(self.money//52 + self.bonus)

# 근무시간에 대한 근로자의 급여 측정
for i in range(p):
    while True:
        try:
            worktime = int(input('{}의 이번 주 근무시간: '.format(t[i])))
            if worktime >=1:
                w.append(worktime)
                break
            else:
                 print('※근무시간을 1이상의 정수로 입력해주십시오※')
        except:
            print('※근무시간을 1이상의 정수로 입력해주십시오※')
    if v[i] == 'H':
        e1 = hour(t[i],worktime, s[i])
    elif v[i] == 'S':
        e1 = year(t[i],worktime, s[i])
    elif v[i] == 'M':
        e1 = manager(t[i],worktime, s[i], u[k])
        k = k + 1
    members = [e1]
    for member in members:
        member = member.tell()

# 근무시간과 주급에 대한 histogram 출력
print('-'*90)
print('입력하신 근무 시간과 주급에 대한 histogram을 출력합니다')
import matplotlib.pyplot as plt_1
n, bins, patches = plt_1.hist(w, 6)
plt_1.title('Working Hours')
plt_1.show()
import matplotlib.pyplot as plt_2
n, bins, patches = plt_2.hist(h, 5)
plt_2.title('Weekly Salary')
plt_2.show()

# 근로자 이름 입력시 근무시간 및 급여 출력
print('-'*90)
print('근로자 이름 입력시 해당 근로자의 근무시간 및 급여정보를 재확인할 수 있습니다')
while True:
    print('※employee파일에 있는 근로자의 이름을 정확히 입력해 주십시오※(예시: Denise Alexander)')
    worker = input('근로자 이름: ')
    print()
    if worker in t:
        break
k=0
for i in range(p):
    if v[i] == 'H':
        e1 = hour(t[i],worktime, s[i])
    elif v[i] == 'S':
        e1 = year(t[i],worktime, s[i])
    elif v[i] == 'M':
        e1 = manager(t[i],worktime, s[i], u[k])
        k = k + 1
    if worker == t[i]:
        members = [e1]
        for member in members:
            member = member.tell()
print('-'*90)
print('프로그램이 종료되었습니다.')
