class Isc(Exception):
    def __init__(self, txt):
        self.txt = txt

a = input('Введите первое число: ')
b = input('Введите второе число: ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise Isc('На ноль делить нельзя!')
except ValueError:
    print('Вы ввели не число!')
except Isc as err:
    print(err)
else:
    print('Результат деления:', a / b)
