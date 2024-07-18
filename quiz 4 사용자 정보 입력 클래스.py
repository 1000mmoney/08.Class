class Person:
    def __init__(self, n, a, p):
        self.name = n
        self.age = a
        self.phone = p

    def print_info(self):
        print("이름 :", self.name, "\n나이 :", self.age, "\n연락처 :", self.phone)

my = Person("하현수", 29, "010-6807-8425" )
my.print_info()