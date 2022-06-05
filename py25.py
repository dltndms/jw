# 반복문
# for, while

'''
for 임시변수 in range(횟수):
        반복수행할 코드

while 같은 경우는 기준이 되는 변수를 먼저 적어준다
기준변수 = 0
while 기준변수 < 횟수:
    반복수행할 코드
    기준변수 +=1
    
'''

# 안녕하세요 3번
for i in range(3):
    print('안녕하세요')

flag = 0
while flag < 3:
    print('반갑습니다')
    flag +=1        # flag = flag +1 의 의미임


list = [1, '안녕하세요', 3.14, 30, '반갑습니다']
list.append('추가')
for i in list:
    print(i)
