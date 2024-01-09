import cv2
import numpy as np

img = cv2.imread("MadhyaPradesh.jpg", 1)
cv2.imshow("Color image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Greyscale image", gray)
blur = cv2.blur(gray, (3, 3))
ret, thresh = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary image", thresh)
	
# Finding contours for the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3) 
cv2.imshow("Contoured image", thresh)

hull = []
    
# calculate points for each contour
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))
    
# create an empty black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
    
# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # color for contours
    color = (255, 255, 0) # color for convex hull
    # draw contours
    cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
    cv2.imshow("Contour", drawing)
    # draw convex hull
    cv2.drawContours(drawing, hull, i, color, 2, 8)

cv2.imshow("Output", drawing)

cv2.waitKey(0)
cv2.destroyAllWindows()
