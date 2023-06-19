# A failed attempt to recognize page layouts

import numpy
import layoutparser as lp

import cv2 as cv

img_path = '/Users/jessicali/Documents/MEAP/output2.png'
img = cv.imread(img_path)

model = lp.Detectron2LayoutModel('lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
                                 extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
                                 label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"})

layout_result = model.detect(img)

lp.draw_box(img, layout_result, box_width=5, box_alpha=0.2, show_element_type=True).show()