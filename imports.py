import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def template_matching(image_path, template_path):
    img = cv.imread(image_path, 0)
    template = cv.imread(template_path, 0)
    w, h = template.shape[::-1]

    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
               'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

    for meth in methods:
        method = eval(meth)
        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        top_left = min_loc if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED] else max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv.rectangle(img, top_left, bottom_right, 255, 2)

        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()

def threshold_demo():
    max_value = 255
    max_type = 4
    window_name = 'Threshold Demo'

    def on_trackbar(val):
        threshold_type = cv.getTrackbarPos('Type', window_name)
        threshold_value = cv.getTrackbarPos('Value', window_name)
        _, dst = cv.threshold(src_gray, threshold_value, max_value, threshold_type)
        cv.imshow(window_name, dst)

    src = cv.imread('template.jpg')
    if src is None:
        print('Could not open or find the image')
        return

    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.namedWindow(window_name)
    cv.createTrackbar('Type', window_name, 3, max_type, on_trackbar)
    cv.createTrackbar('Value', window_name, 0, max_value, on_trackbar)

    on_trackbar(0)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    root = Tk()
    root.withdraw()  # Hide the main window

    image_path = filedialog.askopenfilename(initialdir='D://Music', title="Select Image")
    template_path = 'template.jpg'

    if image_path:
        template_matching(image_path, template_path)
    
    threshold_demo()
