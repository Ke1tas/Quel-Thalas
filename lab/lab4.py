import pandas as pd
import matplotlib.pyplot as plt
import csv
import cv2

df = pd.read_csv('annot')
df.columns = ['absolute_path','relative_path']


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


stats = df[['height', 'width', 'depth']].describe()
print(stats)
def filter_images(dataframe, max_width, max_height):
    return dataframe[(dataframe['width'] <= max_width) & (dataframe['height'] <= max_height)]
df["area"] = df["height"]*df["width"]
df_filtered = filter_images(df,500,500)
print(df_filtered)
df_sorted = df.sort_values(by='area')
print(df_sorted)

plt.figure(figsize=(10, 5))
plt.hist(df['area'], color='gray')
plt.title('Распределение площадей изображений')
plt.xlabel('Площадь (пиксели)')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()
