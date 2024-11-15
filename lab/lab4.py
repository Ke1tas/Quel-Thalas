import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os


def init_data_frame(annotation_path:str)-> pd.DataFrame:
    if not os.path.exists(annotation_path):
        raise FileNotFoundError(f"Файл аннотации не найден: {annotation_path}")
    df = pd.read_csv(annotation_path)
    df.columns = ['absolute_path', 'relative_path']
    return df

def add_h_w_d_cols(df:pd.DataFrame)->None:
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
    stats = df[['height', 'width', 'depth']].describe()
    print(stats)

def image_filter(df:pd.DataFrame, max_width:int, max_height:int)->pd.DataFrame:
    return df[(df['width'] <= max_width) & (df['height'] <= max_height)]

def add_area_col(df:pd.DataFrame)->None:
    df["area"] = df["height"]*df["width"]

def image_area_sorter(df:pd.DataFrame)->None:
    df = df.sort_values(by='area')

def area_hist(df:pd.DataFrame)->None:
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
