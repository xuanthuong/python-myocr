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

def CutSubBlock(lnRoi,roi,num_roi, outFolder):	
	pre_xpos = 0
	hasLine = False
	(h, w) = roi.shape[:2]
	for xpos in range(w):
		if np.sum(lnRoi[0:h, xpos:xpos+1]) > 30000:
			if (xpos - pre_xpos < 100):
				continue
			subRoi = roi[0:h, pre_xpos:xpos]
			cv2.imwrite(outFolder + str(num_roi) + 'subroi.jpg', subRoi)
			#print(outFolder + str(num_roi) + 'subroi.jpg' + ',')
			pre_xpos = xpos
			hasLine = True
			#print('has line %d' % num_roi)
			num_roi += 1
	if hasLine == False:
		cv2.imwrite(outFolder + str(num_roi) + 'subroi.jpg', roi)
		num_roi += 1
	return num_roi
	
	
def CutBlock(srcImgFile, outFolder):
	src = cv2.imread(srcImgFile)
	(h, w) = src.shape[:2]
	if src is None:
		print "Problem loading image!!!\n"
		exit()
		
	if len(src.shape) > 2:
		gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	else:
		gray = src
	ret2,gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	hKernelSize = int(h/30)
	vKernelSize = int(w/30)
	hKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(hKernelSize,1))
	vKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,vKernelSize))
	hLines = cv2.erode(gray,hKernel,iterations = 1)
	hLines = cv2.dilate(hLines,hKernel,iterations = 2)			
	vLines = cv2.erode(gray,vKernel,iterations = 1)
	vLines = cv2.dilate(vLines,vKernel,iterations = 2)	
	lineImg = hLines + vLines
	#cv2.imwrite(outPath, lineImg)
	cv2.imwrite('lineonly.jpg', lineImg)
	
	# Cutting block
	pre_ypos = 0
	num_roi = 1
	for ypos in range(h):		
		if np.sum(lineImg[ypos:ypos+1,0:w]) > 200000:
			if (ypos - pre_ypos < 100):
				continue
			roi = src[pre_ypos:ypos, 0:w]
			lnRoi = lineImg[pre_ypos:ypos, 0:w]
			#cv2.imwrite("C:\\Users\\Thuong.Tran\\Desktop\\output\\" + str(t) + 'roi.jpg', lnRoi)
			num_roi = CutSubBlock(lnRoi,roi,num_roi, outFolder)
			pre_ypos = ypos

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