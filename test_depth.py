import cv2
from depth_service import depth_check

img = cv2.imread("spoof test.jpeg")

score = depth_check(img)

print(score)