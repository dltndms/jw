# page 146(파이썬 지원함수)
from ast import expr


print(2**3)  # 제곱승
print(4**2)  # 제곱승

# 형변환  (자료형 바꾸기)
str(123)                  #정수 123 -> 문자열 '123' 으로 바뀌게 된다.
int('123')                 # 문자열'123'  -> 정수 123 으로 바뀌게 된다.
float('123.0')              # 문자열 '123.0'   -> 실수 123.0

result = eval('100-50')               # 정수 50
print(result)

# 149 page
expr = input('계산식을 입력하세요>>>')
result = eval(expr)
print(expr + '=' + str(result))

# def 절대값구하기(num):   # ==abs
#      if num < 0
#          num*=-1
#          return num



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(lst))
print(min(lst))


# divmod == %
# pow == **

# round : 반올림
pi = 3.141592
print(round(pi, 2))


# sum : 리스트 안에 있는 값을 전부 더하기 해서 return
print(sum(lst))


# len : 리스트 항목의 갯수
print(len(lst))


# lst 평균
# 리스트평균 / 리스트 항목갯수


print(sum(lst)/len(lst))

for i, j in enumerate(lst):
    print(i, ":", j)
# enumerate : 방번호와 값을 분리
#page 159, page 160 (1,2)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months):
    print('{}월 = {}일'.format(month+1, day))


색깔 = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
for i, 무지개색 in enumerate(색깔):
    print('무지개의 {}번째 색은 {}입니다.'.format(i+1,무지개색) )


lst1 = []
print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요')
while True:
    점수 = int(input('점수입력>>>'))
    if 점수 < 0 :
        break
    lst1.append(점수)


print('평균 = {}, 최대 = {}, 최소 = {}'.format(sum(lst1)/len(lst1),max(lst1),min(lst1) ))

