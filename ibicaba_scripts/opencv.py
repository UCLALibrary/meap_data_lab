import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image
# import pytesseract

img_filepath = '/Users/jessicali/Documents/MEAP/images/0090_images/'
img_name = 'ibicaba_0090_contacorrente_fazenda_levy_1932_1939_0300.jpg'

# img = cv.imread(img_filepath + img_name, cv.IMREAD_GRAYSCALE)
img = cv.imread('/Users/jessicali/Documents/MEAP/page0000.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
# img = cv.medianBlur(img,5)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

ret, imgf = cv.threshold(img, 127, 255,cv.THRESH_BINARY,cv.THRESH_OTSU) # good for clear text! numbers?
cv.imwrite('/Users/jessicali/Documents/MEAP/images/processed/grayscale_attempt2.png', imgf)

converted_img = cv.cvtColor(imgf, cv.COLOR_GRAY2BGR)
dst = cv.fastNlMeansDenoisingColored(converted_img, None, 10, 10, 7,21) 
# cv.imwrite('/Users/jessicali/Documents/MEAP/images/processed/converted_img2.png', converted_img)
new_img = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
# new_img = cv.adaptiveThreshold(new_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY,11,2)

kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(new_img,kernel,iterations = 1)
cv.imwrite('/Users/jessicali/Documents/MEAP/images/processed/threshold2.png', erosion)


# for i in range(2):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()