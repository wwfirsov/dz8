import datetime

now = datetime.datetime.now()

class Data:

    @classmethod
    def chislo(cls, param):
        param.split('-')
        date, month, year = param.split('-')
        print('День:', int(date))
        print('Месяц:', int(month))
        print('Год:', int(year))

    @staticmethod
    def valid(param):
        param.split('-')
        date, month, year = param.split('-')
        date = int(date)
        month = int(month)
        year = int(year)
        if date <= 0 or date > 31:
            print('Неверная дата')
        if year <= 0 or year > now.year:
            print('Неверный год')


Data.chislo('16-01-2001')
Data.valid('16-01-1909')



