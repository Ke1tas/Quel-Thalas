import cv2
import matplotlib.pyplot as plt
import numpy as np

#Загрузка изображения
img = cv2.imread('babadzaki.png')

#Отображение изображения
cv2.imshow('swamps', img)
cv2.waitKey(0)

#Разрешение картинки
print(img.shape[0],"*",img.shape[1])

#создание гистограммы
colours = ('b', 'g', 'r')
plt.figure(figsize=(10, 5))
for i, color in enumerate(colours):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.title('Гистограмма цвета изображения')
plt.xlabel('Интенсивность цвета')
plt.ylabel('Частота')
plt.grid()
plt.show()

# img2 = cv2.imread('babadzaki.png')
#соединение двух изображений
combined_img = np.hstack((img, img))
#вывод исходного изображения
cv2.imshow('swamps', img)
cv2.waitKey(0)
#вывод нового изображения
cv2.imshow('wft', combined_img)
cv2.waitKey(0)

#Запись
cv2.imwrite('image2.jpg', combined_img)