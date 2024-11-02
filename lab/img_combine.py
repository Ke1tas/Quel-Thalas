import numpy as np


def combine_images(img1:np.ndarray,img2:np.ndarray)->np.ndarray:
    """

    :param img1:
    :param img2:
    :return:
    """
    if(img1.shape[1] != img2.shape[1]):
        raise ValueError(f"Изображения имеют разную высоту: {img1} , {img2}")
    combined_img = np.hstack((img1, img2))
    return combined_img