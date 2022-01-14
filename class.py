#Note를 정리하는 프로그램
#사용자는 Note에 뭔가를 적을 수 있다.
#Note에는 Content가 있고, 내용을 제거할 수 있다.
#두 개의 노트북을 합쳐 하나로 만들 수 있다.
#Note는 Notebook에 삽입된다.
#Notebook은 Note가 삽일 될 때 페이지를 생성하며,
#최고 300페이지까지 저장 가능하다
#300 페이지가 넘으면 더 이상 노트를 삽입하지 못한다.

class Note(object):
    def __init__(self, content = None):
        self.content = content

    def write_content(self, content):
        self.content = content

    def remove_all(self):
        self.content = ""

    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return "노트에 적힌 내용입니다 : {}".format(self.content)

class Notebook(object):
    def __init__(self, title):
      self.title = title
      self.page_number = 1
      self.notes = dict()

    def add_note(self, note, page = 0): #page를 안넣어줄 경우는 차례대로
        if self.page_number < 300:
            if page == 0:
                 self.notes[self.page_number] = note
                 self.page_number += 1
            else:
                self.notes[page] = note
                self.page_number += 1
        else:
            print("Page가 모두 채워졌습니다.")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())

#-------------------------------------------- class 선언

my_notebook = Notebook("팀랩 강의노트")

new_note = Note("class는 처음입니다.")
print(new_note)

new_note_2 = Note("파이썬 강의")
print(new_note_2) 

my_notebook.add_note(new_note.content, 1)

my_notebook.add_note(new_note_2.content, 100)
print(my_notebook.notes[1])
print(my_notebook.notes[100]) #dict의 keys가 page number임

print(my_notebook.get_number_of_pages())


#------------------------------------------- class 상속
#부모클래스로 부터 속성과 Method를 물려받은 자식 클래스를 생성 하는 것

class Person(object):

    def __init__(self, name, age, gender):
        self.name = name #속성 값 선언
        self.age = age
        self.gender = gender

    def about_me(self): #메소드 선언
        print("저의 이름은 {} 입니다. 나이는 {} 입니다.".format(self.name, self.age))

    def __str__(self):
        return "저의 이름은 {} 입니다. 나이는 {} 입니다.".format(self.name, self.age)

class Korean(Person): #부모클래스 Persin으로 부터 상속
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender) #부모객체 사용
        self.salary = salary
        self.hire_date = hire_date #속성값 추가 선언

    def do_work(self): #새로운 메소드 추가
        print("열심히 일을 합니다.")

    def about_me(self):
        super().about_me()
        print("제 급여는 {}원 이구요. 제입사일은 {}입니다.".format(self.salary, self.hire_date))


first_korean = Korean("Jinyeong", 24, "남자", 300, "2021/12/31")
print(first_korean.about_me())

#----------------------------------------------polymorphism code(다형성)
#같은 이름의 메소드의 내부로직을 다르게 작성

class Animal:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'),Cat("Kitty"),Dog("Mong")]
print(animals)


for i in animals:
    print(i.name + ':' + i.talk())

#------------------------------------------------Visibility overview(가시성)
#객체의 정보를 볼 수 있는 레벨을 조절하는 것
#누구나 객체 안에 모든 변수를 볼 필요가 없음


#decorate
def squre(x):
    return x*x
f = squre
print(f(5))  #First-class obfect

def print_msg(msg): #inner function
    def printer():
        print(msg)
    printer()

print_msg("Hello, Python")

def print_msg(msg):
    def printer():
        print(msg)
    return printer
another = print_msg("Hello")
another()

#closure example

def tag_func(tag, text):
    text = text
    tag = tag

    def inner_func():
        return '{0}{1}{0}',format(tag, text)
    
    return inner_func
h1_func = tag_func("title", "This is Python Class")
p_func = tag_func('p', "Data Academy")


def star(func):
    def inner(*args):
        print(args[1]*30,'1')
        func(*args)
        print(args[1]*30,'2')
    return inner

@star
def printer(msg,mark):
    print(msg)
printer("Hello", '*')

def generate_power(exponent):
    def wrapper(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return wrapper

@generate_power(2)
def raise_two(n):
    return n**2
print(raise_two(7))










