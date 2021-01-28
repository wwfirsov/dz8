class complex_chisla:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, obj):
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y
    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y

x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
a = complex_chisla(x, y)
x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
b = complex_chisla(x, y)
a + b
a * b

print('Сумма: %.2f+%.2fj' % (a.sumax, a.sumay)) # Непонятно что это такое и как это работает - %.2f+%.2fj', зачем нужен знак % перед (a.sumax, a.sumay)?!
print('Произведение: %.2f+%.2fj' % (a.multx, a.multy))
