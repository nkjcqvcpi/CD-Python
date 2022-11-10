import numpy as np
import cv2 as cv
# from memory_profiler import profile
#
#
# @profile(precision=4)
def process():
    img = cv.imread('test.png')
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (360, 100, 820, 1080)
    cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    fg_img = img * mask2[:, :, np.newaxis]
    return img, fg_img


image, fg = process()
# cv.imwrite('grabcut.png', fg)
