import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os


def init_data_frame(annotation_path:str)-> pd.DataFrame:
    """
    Создает фрейм с абсолютными и относительными путями к изображениям.
    :param annotation_path: Путь к файлу с аннотацией.
    :return: Фрейм с абсолютными и относительными путями.
    """
    if not os.path.exists(annotation_path):
        raise FileNotFoundError(f"Файл аннотации не найден: {annotation_path}")
    df = pd.read_csv(annotation_path)
    df.columns = ['absolute_path', 'relative_path']
    return df

def add_h_w_d_cols(df:pd.DataFrame)->None:
    """
    Добавляет столбцы высоты, ширины и глубины изображения во фрейм.
    :param df: Информация об изображениях.
    :return: None
    """
    h = []
    w = []
    d = []
    for i in df["absolute_path"]:
        shape = cv2.imread(i).shape
        h.append(shape[0])
        w.append(shape[1])
        d.append(shape[2])
    df.insert(2, "height", pd.Series(h), True)
    df.insert(3, "width", pd.Series(w), True)
    df.insert(4, "depth", pd.Series(d), True)

def h_w_d_statistical_info(df:pd.DataFrame)->None:
    """
    Выводит статистическую информацию для столбцов высоты, ширины и глубины.
    :param df: Информация об изображениях.
    :return: None
    """
    stats = df[['height', 'width', 'depth']].describe()
    print(stats)

def image_filter(df:pd.DataFrame, max_width:int, max_height:int)->pd.DataFrame:
    """
    Создает отфильтрованный по ширине и высоте фрейм с информацией об изображениях.
    :param df: Информация об изображениях.
    :param max_width: Максимальная ширина изображения.
    :param max_height: Максимальная высота изображения.
    :return: Отфильтрованный фрейм.
    """
    return df[(df['width'] <= max_width) & (df['height'] <= max_height)]

def add_area_col(df:pd.DataFrame)->None:
    """
    Добавляет столбец с площадями изображений.
    :param df: Информация об изображениях.
    :return: None
    """
    df["area"] = df["height"]*df["width"]

def image_area_sorter(df:pd.DataFrame)->None:
    """
    Сортирует информацию об изображениях по возрастанию площади
    :param df: Информация об изображениях.
    :return: None
    """
    df = df.sort_values(by='area')

def area_hist(df:pd.DataFrame)->None:
    """
    Выводит гистограмму площадей изображений.
    :param df: Информация об изображениях.
    :return: None
    """
    plt.figure(figsize=(10, 5))
    plt.hist(df['area'], color='gray')
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь (пиксели)')
    plt.ylabel('Частота')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# df_filtered = filter_images(df,500,500)
# print(df_filtered)
#
# print(df_sorted)
