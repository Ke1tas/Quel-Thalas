import os

import cv2
import numpy as np


def img_load(path: str)-> np.ndarray:
    """
    Загружает изображение из файла
    :param path:Путь к изображению
    :return: Загруженное изображение
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Изображение не найдено: {path}")
    return cv2.imread(path)


#Отображение изображения
def img_show(img:np.ndarray)->None:
    """
    Создает окно с изображением
    :param img: Изображение для отображения
    :return:
    """
    cv2.imshow('image',img)
    cv2.waitKey(0)


#Разрешение картинки
def print_resolution(img:np.ndarray)->None:
    """
    Выводит в консоль разрешение изображения
    :param img: Изображение
    :return:
    """
    print(img.shape[0],"*",img.shape[1])


#Запись
def img_save(img:np.ndarray, name:str)->None:
    """
    Сохраняет изображение с заданным названием
    :param img: Изображения для сохранения
    :param name: Название для файла нового изображения
    :return:
    """
    cv2.imwrite(name, img)