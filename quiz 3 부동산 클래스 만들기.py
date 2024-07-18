#1. 부동산의 위치 평수 종류 가격 년수를 클래스로 정보로 입력하고 모든 정보 출력하는 클래스 만들기
# class House:
#     def __init__(self, st, sc, k, p, y):
#         self.house_situation = st
#         self.house_section = sc
#         self.house_kind = k
#         self.house_prize = p
#         self.house_years = y
#     def check(self):
#         a = {"위치": st}
#         print(a)
#
# st = input("위치를 입력하세요:")
# sc = input("평수을 입력하세요:")
# k = input("종류를 입력하세요:")
# p = input("가격을 입력하세요:")
# y = input("년수를 입력하세요:")
#
#
# name = House()
# name.check()

# 교수님
class Building:
    def __init__(self, loc, y, p, a):
        self.location = loc
        self.years = y
        self.prize = p
        self.area = a

    def print_info(self):
        print("건물위치:", self.location,"\n건물년수:", self.years,"\n건물가격:", self.prize,"\n건물평수:", self.area)

building = Building("강남", 2, "아파트", 20 )
building.print_info()