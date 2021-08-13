# 11. 리스트
#  지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30
# subway = [10, 20, 30]
# print(subway)
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))
# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)
# # 정형돈씨를 유재서/ 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)
# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
# # print(subway.pop())
# # print(subway)
# # print(subway.pop())
# # print(subway)
# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
# 정렬도 가능
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)
# # 순서 뒤지기 가능
# num_list.reverse()
# print(num_list)
# #  모두 지우기
# num_list.clear()
# print(num_list)
# # 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)
# # 리스트 확장
# num_list = [10, 20, 30]
# num_list.extend(mix_list)
# print(num_list)

# 12. 사전
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용불가"))
print("hi")
print(3 in cabinet)  # True
print(5 in cabinet)  # False
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
# # 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)
# 간 손님
del cabinet["A-3"]
print(cabinet)
#  key 들만 출력
print(cabinet.keys())
#  value만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())
# 목욕탕 패점
cabinet.clear()
print(cabinet)

# 13.튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# # menu.add("생선까스")
# (name, age, hobby) = ("신정훈", "40", "게임")
# print(name, age, hobby)

# 14.세트
# 중복 안됨, 순서 없음
# my_set = {1, 2, 3, 3, 3}
# print(my_set)
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# # 교집합 (java 와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))
# # 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))
# # 차집합 (java 할 수 있지만 python은 할 수 없는 개발자)
# print(java - python)
# print(java.difference(python))
# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
# # java를 할수 없어짐
# python.remove("김태호")
# print(python)

# 15.자료구조의 변경
# # 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))
# menu = dict(menu)
# print(menu, type(menu))

# 16. IF (1:57분)
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")
# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# 17. for
# print("대기번호 :1")
# print("대기번호 :2")
# print("대기번호 :3")
# print("대기번호 :4")

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))
# # range
# for waiting_no in range(1, 100):
#     print("대기번호 : {0}".format(waiting_no))
# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

# 18.while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}.커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index +=

# customer = "토르"
# person = "unknown"
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름?")

# # 19. conrinue or break
# absent = [2, 5]  # 결석
# no_book = [7]  # 책이 없음
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 20. 한줄 for
# student = [1, 2, 3, 4, 5]
# student = [i+100 for i in student]
# print(student)
# student = ["batman", "shinjunghun", "shinbi"]
# student = [len(i) for i in student]
# print(student)
# student = ["batman", "shinjunghun", "shinbi"]
# student = [i.upper() for i in student]
# print(student)

# 21. 함수
# def open_account():
#     print("안녕하세요")


# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money


# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance


# def withdraw_night(balance, money):
#     commission = 100
#     print("수수료 {0} 원이며, 잔액은 {1} 원 입니다.".format(
#         commission, balance - money - commission))
#     return commission, balance - money - commission


# open_account()
# balance = 100000
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 1000000)
# balance = withdraw(balance, 3000)
# commision, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원 입니다.".format(commision, balance))
# balance = 100000
# deposit(balance, 1000)
# # withdraw_night(balance, 1000)
# # commision, balance = withdraw_night(balance, 500)
# commision, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원 입니다.".format(commision, balance))
# balance = withdraw_night(balance, 500)
# withdraw_night(balance, 1000)
# deposit(balance, 1000)
