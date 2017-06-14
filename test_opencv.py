#!/usr/bin/env python2

import cv2
import sys

if len(sys.argv) < 3:
    print("Usage: ./test_opencv.py <target image> <destination image path>")
    sys.exit(1)

original = cv2.imread(sys.argv[1])
if original is None:
    print("Cannot load image")
    sys.exit(1)

edges = cv2.Canny(original, 50, 125)

cv2.imwrite(sys.argv[2], edges)
