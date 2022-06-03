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

for i in range(100):
    for j in range(img.shape[i]):
        img[i][j] = []