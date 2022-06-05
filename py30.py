입력값 = int(input("몇개의 과일을 보관할까요? >>>"))  
숫자= 0
lst = [] 
for i in range(입력값):
    과일 = input('{}번째 과일을 입력하세요 >>>'.format(숫자+1))
    lst.append(과일)
    숫자 += 1

print('입력받은 과일들은 {}입니다.'.format(lst))   

리스트 = []
숫자 = int(input("몇개의 과일을 보관할까요? >>>")) 
for i in range(입력값):
    과일 = input('{}번째 과일을 입력하세요 >>>'.format(i+1))
    리스트.append(과일)
print('입력받은 과일들은 {}입니다.'.format(리스트))   


리스트 = []
숫자 = int(input("몇개의 과일을 보관할까요? >>>")) 
i=0
while i< 숫자:
    과일 = input('{}번째 과일을 입력하세요 >>>'.format(i+1))
    리스트.append(과일)
    i+=1
print('입력받은 과일들은 {}입니다.'.format(리스트))   
 

