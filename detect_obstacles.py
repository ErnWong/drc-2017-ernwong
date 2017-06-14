#!/usr/bin/env python2
import cv2
import numpy as np

def find_a_better_name():
    pass

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: ./test_opencv.py <target image> <destination image path>")
        sys.exit(1)

    original = cv2.imread(sys.argv[1])
    if original is None:
        print("Cannot load image")
        sys.exit(1)

    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
    lower_pink = np.array([160, 100, 0])
    upper_pink = np.array([170, 255, 255])

    pinkthres = cv2.inRange(hsv, lower_pink, upper_pink)
    kernel_erosion = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    bigpink = cv2.erode(pinkthres,kernel_erosion,iterations=1)
    bigpink = cv2.dilate(bigpink,kernel_erosion,iterations=1)
    # mask = cv2.GaussianBlur(mask,(20,20),0)
    # res = cv2.bitwise_and(original,original,mask=mask)

    # edges = cv2.Canny(res, 50, 125)

    output = bigpink;

    cv2.imwrite(sys.argv[2], output)
