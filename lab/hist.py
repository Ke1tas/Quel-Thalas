import cv2
import matplotlib.pyplot as plt
import numpy as np



def hist_show(img:np.ndarray)->None:
    """
    Создает гистограмму изображения
    :param img: Изображение для создания гистограммы
    :return:
    """
    colors = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=color)
    plt.xlim([0, 256])
    plt.title('Гистограмма цвета изображения')
    plt.xlabel('Интенсивность цвета')
    plt.ylabel('Частота')
    plt.grid()
    plt.legend()
    plt.show()