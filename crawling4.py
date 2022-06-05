import urllib.request
from bs4 import BeautifulSoup                                                    #pip install bs4

url = urllib.request.urlopen("https://tv.naver.com/r/")
html = url.read()
문자열 = html.decode()

리스트 = []
soup = BeautifulSoup(문자열,"html.parser")
# 규칙성이 있는 최소단위로 모두 추출
tag = soup.find_all("strong",class_="tit")
for i in tag:
    #< >를 기준으로 자르고 < >를 없앤다
    result = i.find("span").text.strip()
    리스트.append(result)

print(리스트)

for j in 리스트:
    print(j)
print("TOP 100 영상은>>>".리스트[0])