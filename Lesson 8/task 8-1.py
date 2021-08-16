class Date:
    date = ""

    def __init__(self, date):
        self.date = date

    @classmethod
    def expand(cls, date):
        return [int(el) for el in date.split('-')]

    @staticmethod
    def validate(lst):
        try:
            if 1 <= lst[0] and 1 <= lst[1] and 0 <= lst[2]:
                if (lst[1] in [1, 3, 5, 7, 8, 10, 12] and lst[0] <= 31) or \
                        (lst[1] in [4, 6, 9, 11] and lst[0] <= 30) or \
                        (lst[1] == 2 and lst[0] <= 28) or \
                        (lst[1] == 2 and lst[2] % 4 == 0 and lst[2] % 100 != 0 and lst[0] <= 29):
                    print(f"Корректная дата {lst[0]:02}-{lst[1]:02}-{lst[2]}")
                    return True
        except Exception as e:
            print("Невозможно преобразовать дату", e)
        print(f"Некорректная дата {lst[0]:02}-{lst[1]:02}-{lst[2]}")
        return False


print(Date.validate(Date.expand('31-09-2001')))
print(Date.validate(Date.expand('31-08-2001')))
print(Date.validate(Date.expand('31-02-2001')))
print(Date.validate(Date.expand('29-02-2000')))
print(Date.validate(Date.expand('29-02-2004')))
print(Date.validate(Date.expand('29-02-2001')))
print(Date.validate(Date.expand('32-03-2001')))
print(Date.validate(Date.expand('31-11-2021')))
print(Date.validate(Date.expand('31-12-2021')))