import cv2

#이미지 불러오기
이미지 = cv2.imread('img.jpg')
#크기 변경
크기변경 = cv2.resize(이미지,(600, 600))
#글자넣기
cv2.putText(크기변경,"HI MY STAR",(200, 250), cv2.FONT_HERSHEY_COMPLEX,1,(255,100,95),2)
#이미지 보여주기(제목, 이미지명)
cv2.imshow("title", 크기변경)

#이미지 띄워놓고 대기
cv2.waitKey(0)