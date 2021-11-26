import cv2
import mediapipe as mp
import time
from pynput.keyboard import Controller
from cvzone.HandTrackingModule import HandDetector as hd

# object to capture image
cap = cv2.VideoCapture(0)
cap.set(2100 , 1920)
cap.set(9, 1080)
detector = hd(detectionCon=0.8)

#keyboard keys
keys = [["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L"],
        ["Z","X","C","V","B","N","M",",",".","/"]]

finalText = ""

keyboard = Controller()

def drawAll(img, buttonList):
        for button in buttonList:
            x,y=button.pos
            w,h=button.size
            cv2.rectangle(img,button.pos, (x+w , y+h),
                        (45, 255, 255),2, cv2.BORDER_TRANSPARENT)
            cv2.putText(img, button.text, (x+10, y+57),
                        cv2.FONT_HERSHEY_COMPLEX,
                        2, (0,167,255),4)
        return img

class Button():
    def __init__(self, pos, text, size=[70, 70]):
        
        self.pos = pos
        self.size = size
        self.text = text

        

buttonList = []

for i in range(len(keys)):
        for j,key in enumerate(keys[i]):
            buttonList.append(Button([90*j+85, 80*i+50], key))



while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxinfo = detector.findPosition(img)
    img = drawAll(img, buttonList)
    
    if lmList:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size

            if x < lmList[8][0] <x+w and y < lmList[8][1] < y+h:
                cv2.rectangle(img,button.pos, (x+w , y+h),
                        (255,255,255), cv2.FILLED)
                cv2.putText(img, button.text, (x+10, y+37),
                        cv2.FONT_HERSHEY_COMPLEX,
                        3, (255,165,0), 4)
                l,_,_ = detector.findDistance(8,12,img,draw=False)
                print(l)


                if l<47:
                    keyboard.press(button.text)
                    cv2.rectangle(img,button.pos, (x+w , y+h),
                        (255,0,0), cv2.FILLED)
                    cv2.putText(img, button.text, (x+10, y+37),
                        cv2.FONT_HERSHEY_PLAIN,
                        3, (255,165,0), 4)
                    finalText += button.text
                    time.sleep(0.18)
                # elif l<47 and button.text == "<=":
                #     finalText -= button.text
                #     time.sleep(0.18)

    cv2.rectangle(img,(50,450), (788,650),
                        (12,12,171), cv2.BORDER_TRANSPARENT)
    cv2.putText(img, finalText, (68,625),
                        cv2.FONT_HERSHEY_PLAIN,
                        5, (0,167,255), 4)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)

