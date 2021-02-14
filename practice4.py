# 1. 클래스

# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"  # 유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력{0}, 공격력 {1}".format(hp, damage))
# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력{0}, 공격력 {1}".format(tank_hp, tank_damage))
# tank2_name = "탱크"
# tank_hp = 150
# tank2_damage = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력{0}, 공격력 {1}".format(tank_hp, tank_damage))
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
#         name, location, damage))
# attack(name, "2시", damage)
# attack(tank_name, "11시", tank_damage)
# attack(tank2_name, "11시", tank2_damage)

# 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("고스트", 100, 200)
# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

## 상속 ##
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격하고 있습니다. [공격력] {2}"
#               .format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp = - damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
# # 파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# 다중상속
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
# 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격하고 있습니다. [공격력] {2}"
#               .format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp = - damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(self, name, location):
#         print("{0}  :  {1} 방향으로 날아갑니다.[속도{2}]"
#               .format(name, location, self.flying_speed))
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


# # 메소드 오버라이딩 #
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
#               .format(self.name, location, self.speed))
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#    def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격하고 있습니다. [공격력] {2}"
#               .format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp = - damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x
# 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다.[속도{2}]"
#               .format(name, location, self.flying_speed))
# # 공중 공격 유닛 클래스


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상  speed  0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)  # 메소드 오버라이딩
# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location
# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)
# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# vulture.move("11시")
# # battlecrusier.fly(battlecrusier.name, "2시")
# battlecrusier.move("9시")
