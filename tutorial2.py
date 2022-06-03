import cv2
import random

img = cv2.imread('assets/waterfall.jpg', -1)

print(img.shape)

# 2 x 2 array with pixel layout:

#[
#[[b  g, r],  [0, 0, 0]]
#[[255,255,255], [0, 0, 0]] 
#]

# print(img[row]) to print a row, add [col1:col2] to get certain pixels

# To randomly change top 100 pixels colors 

#   for i in range(100):
#        for j in range(img.shape[1]):
#            img[i][j] = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

# To slice out a part of an image and copy it over

tag = img[700:1200, 800:1400]
img[0:500, 0:600] = tag

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()