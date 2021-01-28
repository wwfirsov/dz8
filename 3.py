class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

spisok = []
n = input('Введите число: ')
while n != 'stop':
    if n.isdigit() is True:
        spisok.append(n)
    n = input('Введите число: ')
    try:
        if n != 'stop' and n.isdigit() is False:
            raise OwnError('Вы ввели не число')
    except OwnError as err:
        print(err)
else:
    print('Готовый список:', spisok)

