점수 = int(input("점수를 입력하세요>>>"))
if 점수 < 60:
    print('점수는',점수,'점이고, 학점은 F학점입니다.')
elif 점수 < 70:
    print('점수는',점수,'점이고, 학점은 D학점입니다.')
elif 점수 < 80:
    print('점수는',점수,'점이고, 학점은 C학점입니다.')
elif 점수 < 90:
    print('점수는',점수,'점이고, 학점은 B학점입니다.')
elif 점수 <= 100:
    print('점수는',점수,'점이고, 학점은 A학점입니다.')
else:
    print('?')

