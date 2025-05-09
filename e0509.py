# class Dog:
#     kind = 'border collie'
#     def __init__(self, name):
#         self.name = name
#         self.tricks = set()
#
#     def add_trick(self, trick):
#         self.tricks.add(trick)
#
# a = Dog('하나')
# b = Dog('둘')
#
# a.add_trick('앉아')
# a.add_trick('손')
# b.add_trick('물어')
#
# print(f'a의 종: {a.kind}, 이름: {a.name}, 기술: {a.tricks}')
# print(f'b의 종: {b.kind}, 이름: {b.name}, 기술: {b.tricks}')

class Student:

    def __init__(self, ko, en, ma):
        self.ko = ko
        self.en = en
        self.ma = ma

    def average(self):
        self.sum = ko + en + ma
        self.ave = self.sum/3


n = int(input('학생 수 입력 (N):'))

for i in range(n):
    for j in range(n):
        ko = int(input(f'{j+1}번째 학생의 국어 성적 입력:'))
        en = int(input(f'{j+1}번째 학생의 영어 성적 입력:'))
        ma = int(input(f'{j+1}번째 학생의 수학 성적 입력:'))
        i = Student(ko, en, ma)
        i.average()
        print(f'{j+1}번째 학생 평균 점수: {i.ave}')
    break
