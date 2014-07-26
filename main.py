import cv2

print "Processamento de Imagem"

img = cv2.imread("lenna.png")

img = cv2.resize(img,(100,100))

cv2.imshow("lenna",img)
cv2.waitKey()

cv2.imwrite("lenna.jpg",img)

