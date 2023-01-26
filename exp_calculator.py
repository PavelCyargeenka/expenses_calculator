# Counts and stores in a txt file your dayly/monthly spendings


import json
from os.path import exists


class Shopping:
    __months = {1: 'january', 2: 'february', 3: 'march', 4: 'april',
                5: 'may', 6: 'june', 7: 'july', 8: 'august', 9: 'september',
                10: 'october', 11: 'november', 12: 'december'}

    def __init__(self):
        self._month = self.month()
        self._date = self.date()
        self._pay = self.pay()
        self._book = {self._date: self._pay}
        self.behind_the_scenes()

    def behind_the_scenes(self):
        if not exists(f'{self._month}.json'):
            with open(f'{self._month}.json', 'w') as file:
                json.dump({'init': 0}, file)
        with open(f'{self._month}.json', 'r') as file:
            extract = json.load(file)
            for key in extract:
                if key in self._book:
                    extract[key] += self._book[key]
                    break
            self._book.update(extract)
        with open(f'{self._month}.json', 'w') as file:
            json.dump(self._book, file)
        with open(f'{self._month}.txt', 'a') as file:
            total = sum(self._book.values())
            file.write(f'{self._month.capitalize()} {self._date}. Paid {self._pay} eur. '
                       f'Total paid in {self._month.capitalize()}: {total} eur \n\n')
        print(f'Well done! Check {self._month}.txt!')

    @staticmethod
    def month():
        while True:
            try:
                x = int(input('Month number (1-12): '))
            except ValueError:
                print('A number from 1 to 12, please!')
                continue
            if x not in [i for i in range(1, 13)]:
                print('A number from 1 to 12, please!')
                continue
            return Shopping.__months[x]

    @staticmethod
    def date():
        while True:
            try:
                y = int(input('Date (1-31): '))
            except ValueError:
                print('A number from 1 to 31, please')
                continue
            if y not in [j for j in range(1, 32)]:
                print('A number from 1 to 31, please')
                continue
            return str(y)

    @staticmethod
    def pay():
        while True:
            try:
                z = float(input('Paid: '))
            except ValueError:
                print('Only numbers > 0 are accepted')
                continue
            if z <= 0:
                print('Only numbers > 0 are accepted')
                continue
            return round(z, 2)


new_shopping = Shopping()
