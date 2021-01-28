class Sklad_org:
    def __init__(self, conut_printer, count_scaner, count_copyr):
        self.conut_printer = conut_printer
        self.count_scaner = count_scaner
        self.count_copyr = count_copyr

    def __str__(self):
        return f'Количество оргтехники: принтеры - {self.conut_printer}, сканеры - {self.count_scaner}, копиры - {self.count_copyr}'

class Orgtehnika:
    def __init__(self, price, brand):
        self.prise = price
        self.brand = brand

class Printer(Orgtehnika):
    def __init__(self, price, brand, count_print_list):
        super.__init__(price, brand)
        self.count_print_list = count_print_list

class Scaner(Orgtehnika):
    def __init__(self, price, brand, count_scan_list):
        super.__init__(price, brand)
        self.count_scan_list = count_scan_list

class Copyr(Orgtehnika):
    def __init__(self, price, brand, count_copy_list):
        super.__init__(price, brand)
        self.count_copy_list = count_copy_list

count_printer = input('Количество принтеров: ')
while count_printer.isdigit() is False:
    print('Вы ввели не число')
    count_printer = input('Количество принтеров: ')

count_scaner = input('Количество сканеров: ')
while count_scaner.isdigit() is False:
    print('Вы ввели не число')
    count_scaner = input('Количество принтеров: ')

count_copyr = input('Количество копиров: ')
while count_copyr.isdigit() is False:
    print('Вы ввели не число')
    count_copyr = input('Количество принтеров: ')

s = Sklad_org(count_printer, count_scaner, count_copyr)
print(s)

