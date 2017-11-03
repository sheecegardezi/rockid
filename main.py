import os
import cv2
import numpy as np


currentframe='currentframe.jpg'
windowName='window'
line1=[]
root= 'data/processed'
cv2.namedWindow(windowName)

listOfFiles= [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f)) and f.__contains__('.png')]
runningIndex=0

nextFrame = True
currentFrame = True

currentframepath='currentframe.png'
drawLine1=False


def draw(event, x, y, flags, param):
    global ix, iy, drawing
    ix, iy = x, y

    if event == cv2.EVENT_RBUTTONDOWN:
        if drawLine1:
            line1.append([ix, iy])


    if event == cv2.EVENT_LBUTTONDOWN:
        print('left btn clicked')


    cframe = cv2.imread(currentframepath)
    pts = np.array(line1, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(cframe, [pts], False, (0, 0, 255))
    cv2.imshow(windowName, cframe)


cv2.setMouseCallback(windowName,draw)


while nextFrame:


    img = os.path.join(root, listOfFiles[runningIndex])
    frame = cv2.imread(img)
    cv2.imwrite(currentframepath, frame)


    while currentFrame:

        # pts = np.array([100,150,170,180], np.int32)
        # pts = pts.reshape((-1, 1, 2))1
        # cv2.polylines(currentframe, [pts], True, (0, 255, 255))
        cframe = cv2.imread(currentframepath)



        pts = np.array(line1, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(cframe, [pts], False, (0, 0, 255))

        cv2.imshow(windowName, cframe)


        ch = cv2.waitKey()
        print(ch)


        if ch==49:
            drawLine1 = True
            drawLine2 = False
            drawCurve = False
        #enter
        if ch == 13:
            drawLine1 = False
            drawLine2 = False
            drawCurve = False

        # Escape
        if ch == 27:
            cv2.destroyAllWindows()
            nextFrame=False
            currentFrame=False

        #sapce
        if ch == 32:
            cv2.destroyAllWindows()
            nextFrame = True
            currentFrame = False

        #draw curve on space


    runningIndex = runningIndex + 1

    if runningIndex >= len(listOfFiles):
        nextFrame = False
