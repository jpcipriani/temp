import cv2

print "Processamento de Imagem"

img = cv2.imread("lenna.png")
cv2.imshow("lenna",img)

cv2.waitKey(3000)
