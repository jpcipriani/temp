import cv2

print "Processamento de Imagem"

cam = cv2.VideoCapture(0)
i = 0

while True:
	
	i = i+1	
	_, img = cam.read()

	#img = cv2.resize(img,(100,100))

	cv2.imshow("lenna",img)
	cv2.imwrite("%d.png"%i,img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break


