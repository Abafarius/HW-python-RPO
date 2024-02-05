class Account_bank:
    __balance = {}

    def __init__(self, __tenge, __dollar):
        self.__balance["Tenge"] = __tenge
        self.__balance["Dollar"] = __dollar

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount, currency):
        if currency == "Dollar":
            self.__balance["Dollar"] = amount
        elif currency == "Tenge":
            self.__balance["Tenge"] = amount

citibank = Account_bank(50000, 10)
print(citibank.get_balance())

citibank.set_balance(500, "Dollar")
print(citibank.get_balance())