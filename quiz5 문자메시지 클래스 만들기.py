# class Message:
#     def __init__(self, l):
#         self.length = l
#
#     def find_len(self, l):
#         result = 0
#         if len(l) <= 20:
#             result = 50
#         elif len(l) > 20:
#             result = 100
#         return result
#     def print_prize(self):
#         print("요금은:", self.length)
#
#
# my_m = Message("안녕하세요 반갑습니다")
# my_m.print_prize()

# # 나
# class Message:
#     def __init__(self, l, p1, p2):
#         self.len = l
#         self.p1 = p1
#         self.p2 = p2
#     def print_prize(self):
#
#         if len(self.len) <= 30:
#             a = int(len(self.len))*self.p1
#             print("요금은:", a)
#         else:
#             b = int(len(self.len))*self.p2
#             print("요금은", b)
#
# l= input("문자메시지를 입력하세요:")
# my_m = Message(l,50,100)
# my_m.print_prize()


# # 교수님
text = input("문자메시지를 입력하세요")

class MMS:
    def __init__(self,l ,p1, p2):
        self.len = l
        self.p1 = p1
        self,p2 = p2
    def price(self, text):
        if len(text) <= self.len:
            print(self.p1)
        elif len(text) > self.len:
            print(self.p2)

mms = MMS(100,50,1000)
mms.price("임의의 텍스트 입니다.")




