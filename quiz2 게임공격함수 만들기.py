# # 1. 아이디 성별 직업정보를 받고 클래스를 만들고 기본 공격 함수를 통해 '공격'을 출력하시오
#
# class Game:  # 클래스 앞에 문자는 대문자
#     def __init__(self, id, sex, job):    # 함수 맨 앞에 문자는 소문자
#         self.game_id = id       # 속성 : 개의 이름
#         self.game_sex = sex     # 속성 : 개의 품종
#         self.game_job = job
#
#     def attack(self):
#         print(self.game_id, "공격!")
#
# id = input("아이디를 입력하세요:")
# sex = input("성별을 입력하세요:")
# job = input("직업을 입력하세요:")
#
#
# a = Game(id, sex, job)
# a.attack()


# # 교수님

class Game_char:
    def __init__(self, n, s, j,):
        self.game_id = n
        self.game_sex = s
        self.game_job = j

    def attack(self, a):
        print(self.game_id, "이(가) ", a, "를(을) 공격했다!", sep="") # sep="" 띄어쓰기 지우기

my_char = Game_char("관훈짱짱", " 여", "전사")
my_char.attack("하현수")
