class 자동차:
    def __init__(self, 차주인, 차종):
        self.name = 차주인
        self.car = 차종
    def 차정보(self):
        print("{}차의 주인은 {} 입니다.".format(self.car,self.name))
    def 차변경(self, 차종):
        self.car = 차종
    def __del__(self):
        print("{}차 안내 종료".format(self.name))

# 클래스 사용
#객체화(클래스 사용을 위해 변수로 만들어줌)
아빠차 = 자동차("아빠","벤츠")                       #클래스 사용1
엄마차 = 자동차("엄마","아반떼")                      #클래스 사용2
내차 = 자동차("나","K5")                                #클래스 사용3

아빠차.차정보()
내차.차정보()
엄마차.차정보()
del 아빠차                                            #아빠차 변수를 강제로 없앰

엄마차.차변경("제네시스")
엄마차.차정보()
