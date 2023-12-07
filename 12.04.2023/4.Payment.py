user_Payment = input("Cost: ")

try:
    payment = float(user_Payment)
except ValueError:
    print("Wrong payment value!")
    exit()

user_Discount = input("Discount (%): ")

try:
    row_discount = float(user_Discount)
except ValueError:
    print("Wrong discount value!")
discount = row_discount/100
sum = payment - (payment*discount)
rounded = round(sum, 2)
rounded = str(rounded)
template = "your payment is %s"
message = template % rounded

print(message)

