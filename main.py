import os
import cv2
import numpy as np
from utils import *

drawing=False
currentframe='currentframe.jpg'
windowName='window'

def draw(event, x, y, flags, param):
    global ix, iy, drawing
    ix, iy = x, y

    if event == cv2.EVENT_RBUTTONDOWN and not drawing:
        drawing = True

    if event == cv2.EVENT_LBUTTONDOWN:
        print('')


cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName,draw)

root= 'data'

listOfFiles= [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f)) and f.__contains__('.JPG')]
print(listOfFiles)
runningIndex=0

nextFrame = True
currentFrame = True

while nextFrame:


    # if os.path.isfile(listOfFiles[runningIndex]):
    # if frame is not None:

    img = os.path.join(root, listOfFiles[runningIndex])

    frame = cv2.imread(img)
    cv2.imwrite(currentframe, frame)


    while currentFrame:

        # pts = np.array([100,150,170,180], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(currentframe, [pts], True, (0, 255, 255))

        cframe = cv2.imread(currentframe)
        cv2.imshow(windowName, cframe)
        ch = cv2.waitKey()

        # Escape
        if ch == 27:  # or cv2.getWindowProperty(windowName, 0) <= 0:
            cv2.destroyAllWindows()
            nextFrame=False
            currentFrame=False

        #sapce
        if ch == 32:
            cv2.destroyAllWindows()
            nextFrame = True
            currentFrame = False


    runningIndex = runningIndex + 1

    if runningIndex > len(listOfFiles):
       currentFrame = False
