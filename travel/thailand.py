class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


if __name__ == "__main__":
    print("직접 모듈을 실행")
    print("이 문장은 모듈을 직접 실행할때 출력 됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("외부에서 모듈 실행시 출력 됩니다.")
