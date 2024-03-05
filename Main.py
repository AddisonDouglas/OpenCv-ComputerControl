import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)



    cv2.imshow("Test", img)
    cv2.waitKey(1)
