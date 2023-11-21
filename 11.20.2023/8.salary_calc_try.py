#Asking size of sales from user 
user_size_sales = input("How much did you sell: ")

#Translating user data to integer
size_sales = int(user_size_sales)

#Declaring constant
salary_const = 250

#Calculating average salary
salary_summ = salary_const+(size_sales*0.1)

#print result
print("Your salary size is: ", salary_summ)