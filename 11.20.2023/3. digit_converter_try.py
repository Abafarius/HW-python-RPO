#Asking a number from user
user_dec = input("Enter decimal number:")

#Translating user data to integer
str_to_int = int(user_dec)

#Translating from decimal to binary 
binary_num = bin(str_to_int)

#Translating from decimal to hex 
hex_num = hex(str_to_int)

#Translating from decimal to oct 
oct_num = oct(str_to_int)

#print result
print("Binary num: ", binary_num, "\nHex num: ", hex_num, "\nOct num:", oct_num)