population = 0
class person:
    def __init__(self, name):
        global population        # 클래스보다 위에 있는 전역변수를 수정할 때
        population += 1
        print("{} is born.".format(name))
        self.name = name
        
    @staticmethod
    def get_population():
        print('전체인구수 : {}명'.format(population))
    def __del__(self):
        global population
        population -= 1
        print("{} is dead".format(self.name))

  

# 클래스 사용
#객체화(클래스 사용을 위해 변수로 만들어줌)
man = person("james")                       #클래스 사용1
woman = person("emily")                      #클래스 사용2
person.get_population()
del man
person.get_population()


