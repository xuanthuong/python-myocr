import cv2
import numpy as np

def DetectLine(imgFile, outPath):
    img = cv2.imread(imgFile)
    (h, w) = img.shape[:2]
    if img is None:
        print "Problem loading image!!!\n"
        exit()
      
    if len(img.shape) > 2:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    ret2,gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    hKernelSize = h/30
    vKernelSize = w/30
    hKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(hKernelSize,1))
    vKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,vKernelSize))
    hLines = cv2.erode(gray,hKernel,iterations = 1)
    hLines = cv2.dilate(hLines,hKernel,iterations = 1)			
    vLines = cv2.erode(gray,vKernel,iterations = 1)
    vLines = cv2.dilate(vLines,vKernel,iterations = 1)		
    cv2.imwrite(outPath, hLines + vLines)

def HistoProj(bnImgFile):		
    img = cv2.imread(bnImgFile)
    sumCols = VerticalProj(img)
    sumRows = HorizontalProj(img)
    return [sumCols, sumRows]
	
def VerticalProj(img):
    (h, w) = img.shape[:2]
    sumCols = []
    for j in range(w):
      col = img[0:h,j:j+1] # y1:y2, x1:x2
      sumCols.append(np.sum(col))
    return sumCols
	
def HorizontalProj(img):
    (h, w) = img.shape[:2]
    sumRows = []
    for k in range(h):
      row = img[k:k+1,0:w]
      sumRows.append(np.sum(row))
    return sumRows