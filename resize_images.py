import os
import cv2

parkinglot=[]
parkinglot.append([194, 122])
parkinglot.append([203, 217])
parkinglot.append([12, 251])
parkinglot.append([8, 133])

def get_crop_parmeter(parkinglot,outputFileName):
    xmin=99999999
    for x in parkinglot:
        if x[0]< xmin:
            xmin=x[0]
    ymin = 99999999
    for y in parkinglot:
        if y[1] < ymin:
            ymin = y[1]

    xmax = 0
    for x in parkinglot:
        if x[0] > xmax:
            xmax = x[0]
    ymax = 0
    for y in parkinglot:
        if y[1] > ymax:
            ymax = y[1]
    x=xmin
    y=ymin

    h=ymax-ymin
    w=xmax-xmin

    crop_img = img[y: y + h, x: x + w]
    cv2.imwrite(outputFileName, crop_img)

root= 'data'

listOfFiles= [os.path.join(root, f) for f in os.listdir(root) if os.path.isfile(os.path.join(root, f)) and f.__contains__('.JPG')]

for file in listOfFiles:
    img = cv2.imread(file)

    # cv2.imwrite(currentframe, frame)
    print("something")

    nextFrame = True

    while nextFrame:
        resized_image = cv2.resize(img, (800, 600))
        cv2.imshow('window', resized_image)
        ch = cv2.waitKey()
        if ch == 32:
            cv2.destroyAllWindows()
            nextFrame = False

print(listOfFiles)