import cv2

print "Processamento de Imagem"

cam = cv2.VideoCapture(0)
i = 0

while True:
	
	i = i+1	
	_, img = cam.read()

	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	
	cv2.imshow("imgray",imgray)
	ret,thresh = cv2.threshold(imgray,127,255,0)
	cv2.imshow("thresh",thresh)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	cv2.drawContours(img, contours, -1, (0,255,0), 3)
	cv2.imshow("countours",img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break


