#Asking a number from user
user_dec = input("Enter decimal number:")

def_num = 10

try:
    
    #Translating user data to integer
    str_to_int = int(user_dec)

except ValueError as ve:
    print("\nr u f***ng dumb?! Enter that shitty valid god damn decimal number. Well now it is", def_num,"so far by default.\nActually, you got error such as:", ve)

    str_to_int = def_num

#Translating from decimal to binary 
binary_num = bin(str_to_int)

#Translating from decimal to hex 
hex_num = hex(str_to_int)

#Translating from decimal to oct 
oct_num = oct(str_to_int)

#print result
print("Bin num: ", binary_num, "\nHex num: ", hex_num, "\nOct num:", oct_num)