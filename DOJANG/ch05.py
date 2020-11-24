# 클래스와 객체
# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

#     def sub(self, num):
#         self.result -= num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))
# print(cal2.sub(5))
# print(cal2.sub(2))

# 사칙연산 클래스 만들기

# class FourCal:
#     def __init__(self, first, second):    #생성자(Constructor)
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result 
#     def sub(self):
#         result = self.first - self.second
#         return result     
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# b = FourCal()

# a.setdata(4, 2)
# b.setdata(3, 8)

# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())

# a = FourCal(3, 5) #생성자에 초기값 부여
# b = FourCal(7, 9)

# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())

#클래스의 상속
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

# a = MoreFourCal(2, 5)
# print(a.add())
# print(a.pow())

# class SafeFourCal(FourCal):
#     def div(self):            # 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드오브라이딩 이라고 한다. 
#         if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
#             return 0
#         else:
#             return self.first / self.second

# a = SafeFourCal(4, 0)
# print(a.div())

# # 클래스 변수
# class Family:
#     lastname = "김" # lastname이 클래스 변수임

# print(Family.lastname)

# a = Family()
# b = Family()
# print(a.lastname)
# print(b.lastname)

# Family.lastname = "박"
# print(a.lastname)
# print(b.lastname)

# print(id(Family.lastname))
# print(id(a.lastname))
# print(id(b.lastname))


# import time
# import threading

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working : %s \n" %i)

# print("Start")

# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task)
#     threads.append(t)

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# print("End")


import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
print(result)














