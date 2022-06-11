import cv2
import mediapipe as mp      # pip install mediapipe

mpDetection = mp.solutions.face_detectioin
mpDraw = mp.solutions.drawing_utils
faceDetection = mpDetection.FaceDetection()

img = cv2.imread("img2.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = faceDetection.process(imgRGB)
for id, detection in enumerate(results.detections):
    mpDraw.draw_detection(img, detection)


cv2.imshow("my title", img)
cv2.waitKey(0)