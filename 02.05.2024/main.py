from money import Money
from account import Account

# Создаем объекты Money
money1 = Money(100, 'USD')
money2 = Money(50, 'USD')

# Вывод информации о деньгах
print(money1)
print(money2)

# Сложение денег
result_money = money1 + money2
print(result_money)

# Деление денег на число
divided_money = money1 / 4
print(divided_money)

# Создаем объект Account
account = Account(Money(200, 'USD'))

# Положить деньги на счет
account += Money(50, 'USD')
print(account.balance)