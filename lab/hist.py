import cv2
import matplotlib.pyplot as plt
import numpy as np



def hist(img:np.ndarray)->tuple:
    """
    Создает гистограммы изображения
    :param img: изображение для анализа
    :return: Гистограммы трех цветов
    """
    b = cv2.calcHist([img], [0], None, [256], [0, 256])
    g = cv2.calcHist([img], [1], None, [256], [0, 256])
    r = cv2.calcHist([img], [2], None, [256], [0, 256])
    return b,g,r

def hist_show(b:np.ndarray, g:np.ndarray, r:np.ndarray)->None:
    """
    Отображает гистограммы для трех цветов
    :param b: Синяя гистограмма
    :param g: Зеленая гистограмма
    :param r: Красная гистограмма
    :return:
    """
    plt.figure(figsize=(10, 5))
    plt.plot(b, label='Синяя линия', color='blue')
    plt.plot(g, label='Зеленая линия', color='green')
    plt.plot(r, label='Красная линия', color='red')
    plt.xlim([0, 256])
    plt.title('Гистограмма цвета изображения')
    plt.xlabel('Интенсивность цвета')
    plt.ylabel('Частота')
    plt.grid()
    plt.legend()
    plt.show()