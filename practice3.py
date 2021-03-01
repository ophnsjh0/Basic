# 1. 함수 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"
#           .format(name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
# def profile(name, age=41, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"
#           .format(name, age, main_lang))
# profile("신정훈")
# profile("오지혜", 40, "자바")
# profile("신비", 5, "C++")
# profile("신담비", 2, "HTML")

# 2. 키워드
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
# profile(main_lang="자바", name="신정훈", age=41)
# profile(age=30, main_lang="파이썬", name="신정훈", )

# 3. 가변함수
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\tskdl : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
# def profile(name, age, *languge):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in languge:
#         print(lang, end=" ")
#     print()
# profile("유재석", 20, "python", "java", "C+", "C#", "C")
# profile("김태호", 25, "kotlin", "swift")

# 4. 지역변수 전역변수
# 1) 지역변수 와 전역변수 차이
# gun = 10
# def checkpoint(soldiers):  # 경계근무
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}". format(gun))
# print("전체 총 : {0}". format(gun))
# checkpoint(3)  # 3 명이 경계 근무 나감
# print("남은 총 : {0}". format(gun))
# 2) 전역변수 사용
# gun = 10
# def checkpoint(soldiers):  # 경계근무
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}". format(gun))
# print("전체 총 : {0}". format(gun))
# checkpoint(3)  # 3 명이 경계 근무 나감
# print("남은 총 : {0}". format(gun))
# gun = 10
# # def checkpoint(soldiers):  # 경계근무
# #     global gun
# #     gun = gun - soldiers
# #     print("[함수 내] 남은 총 : {0}". format(gun))
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}". format(gun))
#     return gun
# print("전체 총 : {0}". format(gun))
# # checkpoint(3)  # 3 명이 경계 근무 나감
# gun = checkpoint_ret(gun, 5)
# print("전체 총 : {0}". format(gun))


# 5. 표준입출력
# print("Python", "Java", "JavaScript", sep=",", end="^^")
# print("무엇이 더 재밌을까요?")
# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)
# 사험성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
# # 은행 대기순번표
# # 001, 002, 003
# for num in range(1, 21):
#     print("대기번호 :" + str(num).zfill(3))
#   input
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")

# 6. 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬학 , 빈칸을 _로 채움
# print("{0:_<10}".format(500))
# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(-100000000000))
# # 3자리마다 콤마를 찍어주기, 부호도 붙이기, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# print("{0:^<+30,}".format(10000000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# print("{0}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3째 자리까지 )
# print("{0:.3f}".format(5/3))

# 7.파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("안녕하세요", file=score_file)
# print("신정훈입니다.", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("\n신비 : 100")
# score_file.write("\n담비 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()


# 8. pickle
# import pickle
# profile_file = open("profile.pickle", "bw")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# 9. with

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())
