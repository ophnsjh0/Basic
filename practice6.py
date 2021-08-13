# 모듈
# import theater_module
# theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5)

# from 기본학습.theater_module import price, price_morning, price_soldier
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning


# 패키지
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# import travel.vietnam
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# trip_to = travel.vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# 내장함수
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 좋은 언어입니다.".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# import random
# import pickle
# print(dir())
# print(dir())

# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))
# name = "JIM"
# print(dir(name))


# 외장함수
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)

# import glob
# print(glob.glob("*.py"))  # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는", datetime.date.today())

# # timedelta : 두 날짜 사이의 간견
# today = datetime.date.today()  # 오늘 날짜 저장
# td = datetime.timedelta(days=100)  # 100일 저장
# print('우리가 만난지 100일은', today + td)  # 오늘부터 100일 후


# def caculator():
#     a = int(input("1숫자입력:"))
#     b = int(input("2숫자입력:"))
#     c = input("연산자 입력")
#     if c == "+":
#         d = print(a+b)
#         retrun d


# caculator()
