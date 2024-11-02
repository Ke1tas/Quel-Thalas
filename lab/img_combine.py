import numpy as np

#соединение двух изображений
def combine_images(img1:np.ndarray,img2:np.ndarray)->np.ndarray:
    combined_img = np.hstack((img1, img2))
    return combined_img