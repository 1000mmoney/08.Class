class Dog:  # 클래스 앞에 문자는 대문자
    def __init__(self, name, breed):    # 함수 맨 앞에 문자는 소문자
        self.dog_name = name       # 속성 : 개의 이름
        self.dog_breed = breed     # 속성 : 개의 품종
    def bark(self):
        print(self.dog_name + "가 짖습니다.")

a = Dog("초롱이", "말티즈")
a.bark()
a.bark()
a.bark()
a.bark()
a.bark()


#
# my_lsit = [1,2,3,4,5] # 리스트를 만들고 = 클래스를 만들고
# list.append(6)  # 함수를 써서 리스트에 추가 = 변수 입력해서 함수 만들어 놓은 것에 입렧
#
