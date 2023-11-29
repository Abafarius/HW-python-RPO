userBuy = input("Enter summ how much you bought:")
discount = 0

try:
    buy = float(userBuy)
except ValueError:
    print("Please enter valid number!")
else:
    if 0<buy<200:
        discount = 0
        payment = buy

    elif 200<=buy<=300:
        discount = 1.03
        payment = buy*discount
        discount = 3

    elif 300<=buy<=500:
        discount = 1.05
        payment = buy*discount
        discount = 5

    elif buy>500:
        discount = 1.07
        payment = buy*discount
        discount = 7

    else:
        print("Error")
print("You got discount is ", discount,"%. Your payment is: ", payment, sep="")

    #VN: как думаете, могли бы вы все вызовы print вынести вниз, за пределы конструкции if-elif-else ?
    #AS: решил, было довольно легко, нужно было просто немного подумать в начале