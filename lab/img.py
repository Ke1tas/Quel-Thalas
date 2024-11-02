import os

import cv2
import numpy as np


def img_load(path: str)-> np.ndarray:
    """

    :param path:
    :return:
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Изображение не найдено: {path}")
    return cv2.imread(path)


#Отображение изображения
def img_show(img:np.ndarray)->None:
    cv2.imshow('image',img)
    cv2.waitKey(0)


#Разрешение картинки
def print_resolution(img:np.ndarray)->None:
    print(img.shape[0],"*",img.shape[1])


#Запись
def img_save(img:np.ndarray, name:str)->None:
    cv2.imwrite(name, img)
