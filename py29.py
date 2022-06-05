'''
# 1. 리스트 
변수명 = []             #리스트 변수 선언(생성)
 # 추가하기
변수명.append(3)
변수명.append(3.14)
변수명.append('안녕하세요')

print(변수명)

for i in 변수명:
    print(i, end=",")

#삽입하기(중간에 추가)
변수명.insert(1,'1번에 추가')

# 수정하기
변수명[1] = "1번방 수정"

#제거하기               # -값은 뒤에서부터 계산(앞에서부턴 0부터, 뒤에서부턴 -1부터)
변수명.pop(-1)


# 잘라내기
print(변수명[0:2])      #0부터 1까지 잘라냄

for i in 변수명:
    print(i, end=",")

'''

입력값 = int(input("몇개의 과일을 보관할까요? >>>"))  

for 입력값 < 0 :
    n = int(input('{}번째 과일을 입력하세요 >>>'.format(count-1)))



count = 0
total = 0
while count < 5:
    n = int(input('{}번째 정수를 입력하세요 >>>'.format(count+1)))
    if n <= 0:
        print('0이하의 정수는 처리할 수 없습니다.')
        continue
    total +=n
    count +=1
print('입력된 5개 양수의 총 합은 {}입니다.'.format(total))
