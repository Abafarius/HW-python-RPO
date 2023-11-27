userBuy = input("Enter summ how much you bought:")

try:
    buy = float(userBuy)
except ValueError:
    print("Please enter valid number!")
else:
    if 0<buy<200:
        print("No discount. Summ to pay = ", buy)
    elif 200<=buy<=300:
        payment = buy*1.03
        print("You got discount 3%. Your payment is:", payment)
    elif 300<=buy<=500:
        payment = buy*1.05
        print("You got discount 5%. Your payment is:", payment)
    elif buy>500:
        payment = buy*1.07
        print("You got discount 7%. Your payment is:", payment)
    else:
        print("Error")

    #VN: как думаете, могли бы вы все вызовы print вынести вниз, за пределы конструкции if-elif-else ?