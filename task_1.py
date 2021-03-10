# Name:        Конвертер секунд
# Author:      Панин Станислав
# Created:     10.03.2021


full_step_clock = 60
day_sec = 86400
hour_sec = 3600


def conversion(seconds):
    days = seconds//day_sec
    hour = (seconds // hour_sec) % 24
    mint = (seconds // full_step_clock) % full_step_clock
    sec = seconds % full_step_clock
    return days, hour, mint, sec


def main():
    try:
        duration = int(input('Введите число секунд: '))
    except ValueError:
        duration = int(input('Введите число цифрами от 0: '))

    days, hour, mint, sec = conversion(duration)

    if duration < 0:
        print('Число меньше нуля')
    elif duration < 60:
        print(f'{sec} сек')
    elif duration < hour_sec:
        print(f'{mint} мин, {sec} сек')
    elif duration < day_sec:
        print(f'{hour} час, {mint} мин, {sec} сек')
    elif duration >= day_sec:
        print(f'{days} дн, {hour} час, {mint} мин, {sec} сек')


if __name__ == '__main__':
    main()
