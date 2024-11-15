import  argparse

import data_frame as d_f


def arg_parser() -> argparse.Namespace:
    """
    Получение аргументов из командной строки.
    :return: Возвращает полученные из командной строки аргументы.
    """
    parser = argparse.ArgumentParser(description='Скачивание изображений и создание аннотации.')
    parser.add_argument('--annotation' ,'-a', type=str, required=True, help='Путь к файлу аннотации (CSV).')
    parser.add_argument('--max_width', '-w', type=str, required=True, help='максимальная ширина для фильтрации')
    parser.add_argument('--max_height', '-he', type=str, required=True, help='максимальная высота для фильтрации')
    return parser.parse_args()

def main():
    try:
        args = arg_parser()

        df = d_f.init_data_frame(args.annotation)

        d_f.add_h_w_d_cols(df)
        d_f.h_w_d_statistical_info(df)

        print(df)
        filtered_df = d_f.image_filter(df,args.max_width,args.max_height)
        print(filtered_df)

        d_f.add_area_col(df)
        sorted_df = d_f.image_area_sorter(df)
        print(sorted_df)
        d_f.area_hist(df)

    except Exception as exp:
        print(exp)


if __name__ == "__main__":
    main()