from money import Money

class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if type(value) == Money:
            self._balance = value
        else:
            raise TypeError("Balance must be an instance of Money")

    def __iadd__(self, other):
        if type(other) == Money:
            self._balance += other
            return self
        else:
            raise TypeError("Account can only be incremented by Money")