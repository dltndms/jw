import pandas as pd
from openpyx1.workbook import workbook        #엑셀
import matplotlib.pyplot as plt

def 표만들기():

    번호 = [1,2,3]
    data = {
        '이름' :['홍길동','아무개','김철수'],
        '키':[175.5, 166.3, 180.0],
        '몸무게':[66.8, 50.7, 80.8]
        }

    df = pd.DataFrame(data, index=번호)
    print(df)

    df.to_csv('myTable.txt',sep='\t')

    df.to_excel('myTable.xlsx', index=False)

    #읽기
    df2 = pd.read_excel('myTable.xlsx')
    print(df2)