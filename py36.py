# 함수 
# 1. 개발자가 직접 만드는 기능(연산자)
# 2. 코드를 그룹짓는 기법

# 문제점 : 가독성이 매우 떨어짐
# 제목

def 첫인사():
    print('안녕하세요. 저는 인천에 사는 ㅇㅇㅇ입니다. ')
def 본문():
    print('저는 인천에서 ㅇㅇ중학교를 다녔습니다.')
    print('저는 인천에서 ㅇㅇ고등학교를 다녔습니다.')
    print('저는 인천에서 ㅇㅇ대학교를 다녔습니다.')
    print('저는 인천에서 ㅇㅇ캠프를 다녔습니다.')
def 끝인사():
    print('저는 이 세계에서 필요한 나무가 될 것 입니다.')

첫인사()
본문()
끝인사()

#page 187 중간
def welcome():
    print('hello python')
    print('nice to meet you')

welcome()   


# page 188
def introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))

introduce('제임스',25)

# page 192
def address():
    str1 = "우편번호 12345\n"
    str1 += "서울시 영등포구 여의도동"
    return str1

print(address())

# 함수에 입력해줄때는 ()
# 함수로부터 결과를 받을때는 return
# 함수를 만들때 def
# 함수를 사용할때 함수이름과 소괄호