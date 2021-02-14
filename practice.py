
# 1. 참 / 거짓
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))


# 2. 애완동물을 소개해 주세요~
# animal = "호랑이"
# name = "연탄이"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3
# print("우리집 " + animal + "의 이름은 " + name + "에요")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))


# # 3. 연산
# print(1+1)  # 2
# print(3-1)  # 1
# print(5*2)  # 10
# print(6/3)  # 2
# print(2**3)  # 8
# print(5 % 3)  # 2
# print(10 % 3)  # 1
# print(6//3)  # 2
# print(10//3)  # 3
# print(10 > 3)  # True
# print(4 >= 7)  # False
# print(3 == 3)  # True
# print(3 != 3)  # False
# print(not(3 != 3))  # False
# print(2 + 3 * 4)  # 14
# print((2 + 3) * 4)  # 20
# number = 2 + 3 * 4  # 14
# print(number)
# number = number + 2  # 16
# print(number)
# number += 2  # 18
# print(number)
# number *= 2  # 36
# print(number)
# number /= 2  # 18
# print(number)
# number -= 2  # 16
# print(number)
# number %= 5  # 1
# print(number)

# 4.숫자처리함수
# from math import *
# print(abs(-5))  # 5
# print(pow(4, 2))  # 4^2 = 4*4 = 16
# print(max(5, 12))  # 12
# print(min(5, 12))  # 5
# print(round(3.14))  # 3 반올림
# print(round(4.99))  # 5
# print(floor(4.99))  # 내림. 4
# print(ceil(3.14))  # 올림. 4
# print(sqrt(16))  # 제곱근. 4

# 5.랜덤함수
# from random import *
# print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10))  # 0~10 미만의 임의의 값 생성
# print(int(random() * 10))  # 0~10 미만의 임의의 값 생성
# print(int(random() * 10))  # 0~10 미만의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1~10 이하의 임의의 값 생성
# print(int(random() * 10) + 1)  # 1~10 이하의 임의의 값 생성
# 로또 번호
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# # 로또 번호#2
# print(randrange(1, 46))  # 1~46미만의 임의이 값 생성
# print(randrange(1, 46))  # 1~46미만의 임의이 값 생성
# print(randrange(1, 46))  # 1~46미만의 임의이 값 생성
# print(randrange(1, 46))  # 1~46미만의 임의이 값 생성
# print(randrange(1, 46))  # 1~46미만의 임의이 값 생성
# print(randrange(1, 46))  # 1~46미만의 임의이 값 생성
# print(randrange(1, 46))  # 1~46미만의 임의이 값 생성
# # 로또 번호#3
# print(randint(1, 45))  # 1~45이하의 임의이 값 생성
# print(randint(1, 45))  # 1~45이하의 임의이 값 생성
# print(randint(1, 45))  # 1~45이하의 임의이 값 생성
# print(randint(1, 45))  # 1~45이하의 임의이 값 생성
# print(randint(1, 45))  # 1~45이하의 임의이 값 생성
# print(randint(1, 45))  # 1~45이하의 임의이 값 생성

# 6.문자열
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# ㅋㅋㅋ """
# print(sentence3)

# 7. 슬라이싱
# jumin = "811110-1398912"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])  # 0 부터 2 직전까지 (0, 1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:14])
# print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지

# 8.문자열 함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))
# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
# print(python.find("n"))
# print(python.find("Java"))  # -1 반화 후 계속 실행
# print(python.index("Java"))  # 프로그램 종료
# print(python.count("n"))

# 9.문자열 포맷
# print("a" + "b")
# print("a", "b")

# # 방법 1
# print("나는 %d 살입니다." % 20)  # %d <-- 정수값
# print("나는 %s 을 좋아해요." % "파이썬")  # %s <--- 문자값
# print("Apple 은 %c 로 시작해요." % "A")  # %c <--- 문자한개
# # %s
# print("나는 %s 색과 %s 색을 좋아해요." % ("파란", "빨간"))
# # 방법 2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))
# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="파란"))
# # 방법 4
# age = 20
# color = "파란"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# # 10. 탈출문자
# # \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")
# # \" \' 문장내에서 ", ' 사용 가능
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# # \\ :  문장 내에서 \
# print("C:\\users\\etc\\hello")
# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")
# # \t : 탭
# print("Red\tApple")
