import cv2
import numpy as np

def clahe_preprocessing(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final

def adaptive_ycbcr(img):
    ycbcr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycbcr)
    y = cv2.equalizeHist(y)
    matched = cv2.merge([y, cr, cb])
    return cv2.cvtColor(matched, cv2.COLOR_YCrCb2BGR)

def preprocess_image(img):
    img = clahe_preprocessing(img)
    img = adaptive_ycbcr(img)
    return img
