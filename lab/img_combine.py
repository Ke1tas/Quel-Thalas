import numpy as np


def combine_images(img1:np.ndarray,img2:np.ndarray)->np.ndarray:
    """
    Горизонтально соединяет 2 изображения
    :param img1: Левое изображение
    :param img2: Правое изображение
    :return: Соединенные 2 изображения
    """
    if(img1.shape[1] != img2.shape[1]):
        raise ValueError(f"Изображения имеют разную высоту: {img1} , {img2}")
    combined_img = np.hstack((img1, img2))
    return combined_img