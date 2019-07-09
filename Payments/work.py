import datetime

class PayDay(object):

    def __init__(self):
        pass

    def add(self, date, amount):
        self.date = date
        self.amount = amount

    def getPayHistory(self):
        print('\nИстория выплат:')
        txtfile = open('payhistory.txt', 'r')
        for line in txtfile:
            print(line)
        print('---')
        txtfile.close()

    def makePay(self):
        txtfile = open('payhistory.txt', 'a')
        date = datetime.date.today()

        print(date, '- верная дата? Y/N')
        answer = input()

        if answer.lower() != 'y':
            print('Введите дату: ')
            date = input()

        amountIsCorrect = False
        amount = 0
        while amountIsCorrect == False:
            print('Введите количество ($):')
            try:
                amount = int(input())
            except ValueError:
                print('Вы ввели некорректное значение')
            else:
                amountIsCorrect = True

        txtfile.write(str(date) +' $'+ str(amount) + '\n')
        txtfile.close()



    def _getTotalProfit(self):
        txtfile = open('payhistory.txt', 'r')
        history = []
        for line in txtfile:
            history.append(int(line[line.find('$') + 1:]))

        totalp = 0
        for amount in history:
            totalp += int(amount)

        txtfile.close()

        return totalp

    def totalProfit(self):
        totalp = self._getTotalProfit()
        print('\nВсего заработано: $' + str(totalp))




    def _getTotalWithdraw(self):
        txtfile = open('withdrawhistory.txt', 'r')
        history = []
        for line in txtfile:
            history.append(int(line[line.find('$') + 1:]))

        totalw = 0
        for amount in history:
            totalw += int(amount)

        txtfile.close()
        return totalw

    def totalWithdraw(self):
        totalw = self._getTotalWithdraw()

        print('Всего выведено: $' + str(totalw))


    def getWithdawHistory(self):
        print('\nИстория выводов:')
        txtfile = open('withdrawhistory.txt', 'r')
        for line in txtfile:
            print(line)
        print('---')
        txtfile.close()

    def makeWithdraw(self):
        txtfile = open('withdrawhistory.txt', 'a')
        date = datetime.date.today()

        print(date, '- верная дата? Y/N')
        answer = input()

        if answer.lower() != 'y':
            print('Введите дату: ')
            date = input()

        amountIsCorrect = False
        amount = 0
        while amountIsCorrect == False:
            print('Введите количество ($):')
            try:
                amount = int(input())
            except ValueError:
                print('Вы ввели некорректное значение')
            else:
                amountIsCorrect = True

        txtfile.write(str(date) +' $'+ str(amount) + '\n')
        txtfile.close()

    def balance(self):
        balance = self._getBalance()
        print('\nТекущий баланс: $' + str(balance))

    def _getBalance(self):
        totalp = self._getTotalProfit()
        totalw = self._getTotalWithdraw()
        balance = totalp - totalw
        return balance


if __name__ == "__main__":
    p = PayDay()
    while True:
        print('1 Поступление зп \n2 История зарплат \n3 Всего заработано \n4 Сделать вывод\n5 История выводов \n6 Всего выведено  \n7 Баланс')
        answer = int(input())
        if answer == 1:
            p.makePay()
        elif answer == 2:
            p.getPayHistory()
        elif answer == 3:
            p.totalProfit()
        elif answer == 4:
            p.makeWithdraw()
        elif answer == 5:
            p.getWithdawHistory()
        elif answer == 6:
            p.totalWithdraw()
        elif answer == 7:
            p.balance()
