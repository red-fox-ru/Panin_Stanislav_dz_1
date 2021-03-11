# Name:        Склонение слова "процент"
# Author:      Панин Станислав
# Created:     11.03.2021


def declination(value):
    if value == 1:
        print(f'{value} процент')
    elif value <= 4:
        print(f'{value} процента')
    else:
        print(f'{value} процентов')


def main():
    try:
        value = int(input('Введите число: '))
    except ValueError:
        value = int(input('Введите цифру от 0: '))
    declination(value)


def example():
    list_num = [5, 1, 3, 10, 8, 19]
    for el in list_num:
        declination(el)


if __name__ == '__main__':
    example()
