userDataValue = input("Enter number:")
userDataCurrency = input("Choose which to which currency you want convert (EUR,KZT,RUB,KGS,CNY,CZK,JPY):")

eurConst = 0.91
kztConst = 460.04
rubConst = 89.28
cnyConst = 7.09
kgsConst = 88.63
czkConst = 22.30
jpyConst = 149.47

try:
    dollarNum = float(userDataValue)
except:
    print("Value error! Enter valid number!")
else:
    curName = userDataCurrency.upper()
    if curName == "EUR":
       eur = dollarNum*eurConst
       print("For 11.25.2023 USD->EUR = ", eur)
    elif curName == "KZT":
        kzt = dollarNum*460.04
        print("For 11.25.2023 USD->KZT = ", kzt)
    elif curName == "RUB":
        rub = dollarNum*rubConst
        print("For 11.25.2023 USD->RUB = ", rub)
    elif curName == "CNY":
        cny = dollarNum*cnyConst
        print("For 11.25.2023 USD->CNY = ", cny)
    elif curName == "KGS":
        kgs = dollarNum*kgsConst
        print("For 11.25.2023 USD->KGS = ", kgs)
    elif curName == "CZK":
        czk = dollarNum*czkConst
        print("For 11.25.2023 USD->CZK = ", czk) 
    elif curName == "JPY":
        jpy = dollarNum*jpyConst
        print("For 11.25.2023 USD->JPY = ", jpy)    
    else:
        print("There is no such available currency")     
