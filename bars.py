import sys
import json
import argparse


def open_file(file_bars):
    with open(file_bars, encoding='utf-8') as f:
        return json.load(f)
      

def get_biggest_bar(file_with_bars):
    return max(file_with_bars, key=lambda bar:
               bar['Cells']['SeatsCount'])['Cells']['Name']


def get_smallest_bar(file_with_bars):
    return min(file_with_bars, key=lambda bar:
               bar['Cells']['SeatsCount'])['Cells']['Name']


def get_nearest_bar(file_with_bars, longitude, latitude):
    bar_longitude, bar_latitude = bar['Cells']['geoData']['coordinates']
    nearest_bar = min(file_with_bars, key=lambda bar: (
          (bar_longitude - longitude) ** 2 +
          (bar_latitude - latitude) ** 2))
    return nearest_bar['Cells']['Name']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find bar's')
    parser.add_argument('-file', dest='filepath',
                        help='Input filepath and filename')
    args = parser.parse_args()
    try:
        file_with_bars = open_file(args.filepath)
    except (FileNotFoundError, ValueError):
        print('Файл не найден')
        sys.exit(1)                             
    while True:
        answer = input("Что вы хотите узнать?: \n1 - Самые большие бары \
                        \n2 - Самые маленькие бары \
                        \n3 - Узнать бар по координатам \
                        \n4 - Выход из программы \nВведите номер: ")
        if answer == '1':
            print(get_biggest_bar(file_with_bars))
        elif answer == '2':
            print(get_smallest_bar(file_with_bars))
        elif answer == '3':
            try:
                longitude = float(input("Введите ваши координаты широты: "))
                latitude = float(input("Введите ваши координаты долготы: "))       
            except ValueError:
                print('Вы ввели не правильные координаты')
                sys.exit(1)
            print(get_nearest_bar(file_with_bars, longitude, latitude))
        elif answer == '4':
            sys.exit()
        else:
            print("Не правильный ввод\n\n")
