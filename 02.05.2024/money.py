class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if type(value) in (int, float):
            self._amount = value
        else:
            raise TypeError("Amount must be a number")

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if type(value) == str:
            self._currency = value
        else:
            raise TypeError("Currency must be a string")

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise ValueError("Currencies must be the same for addition")

    def __truediv__(self, other):
        if type(other) in (int, float):
            return [Money(self.amount / other, self.currency) for _ in range(other)]
        else:
            raise TypeError("Money can only be divided by a number")
