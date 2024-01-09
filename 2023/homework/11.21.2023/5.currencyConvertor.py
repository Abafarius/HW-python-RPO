userDataValue = input("Enter number:")
userDataCurrency = input("Choose which to which currency you want convert (EUR,KZT,RUB,KGS,CNY,CZK,JPY):")

eurConst = 0.91
kztConst = 460.04
rubConst = 89.28
cnyConst = 7.09
kgsConst = 88.63
czkConst = 22.30
jpyConst = 149.47
curNameToPrint = ""

try:
    dollarNum = float(userDataValue)
except ValueError:
    print("Value error! Enter valid number!")
else:
    curName = userDataCurrency.upper()

    if curName == "EUR":
       curValue = dollarNum*eurConst

    elif curName == "KZT":
        curValue = dollarNum*460.04

    elif curName == "RUB":
        curValue = dollarNum*rubConst

    elif curName == "CNY":
        curValue = dollarNum*cnyConst

    elif curName == "KGS":
        curValue = dollarNum*kgsConst

    elif curName == "CZK":
        curValue = dollarNum*czkConst

    elif curName == "JPY":
        curValue = dollarNum*jpyConst

    else:
        print("There is no such available currency")     
print("For 11.25.2023 USD->",curName, " = ", curValue, sep="")
    #VN: как думаете, могли бы вы все вызовы print вынести вниз, за пределы конструкции if-elif-else ?
    #AS: да это изи, надо было сразу догадаться =D