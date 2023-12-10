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
    exit()
discount = row_discount/100
sum = payment - (payment*discount)
rounded = round(sum, 2)
rounded = str(rounded)
template = "your payment is %s"
message = template % rounded

print(message)

"""VN: падение:

Cost: 1000
Discount (%): два
Wrong discount value!
Traceback (most recent call last):
  File "/home/vn/Job/ItStep/HomeWorks/SEP-232.1/Галымжан/12.04.2023/4.Payment.py", line 15, in <module>
    discount = row_discount/100
               ^^^^^^^^^^^^
NameError: name 'row_discount' is not defined. Did you mean: 'user_Discount'?
"""
#AS: Исправил нужно было просто добавить exit в последний except, не заметил =D