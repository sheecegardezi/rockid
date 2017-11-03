import os
import cv2

root= 'data'

listOfFiles= [os.path.join(root, f) for f in os.listdir(root) if os.path.isfile(os.path.join(root, f)) and f.__contains__('.JPG')]

for file in listOfFiles:
    img = cv2.imread(file)

    # cv2.imwrite(currentframe, frame)
    print("something")

    nextFrame = True

    while nextFrame:
        cv2.imshow('window', img)
        ch = cv2.waitKey()
        if ch == 32:
            cv2.destroyAllWindows()
            nextFrame = False

print(listOfFiles)