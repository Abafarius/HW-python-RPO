#Asking size of sales from user 
user_size_sales = input("How much did you sell: ")
default_sales = 100
salary_const = 250
#Translating user data to integer
try: 
    size_sales = int(user_size_sales)
except ValueError:
    print("Error when transformation. Value of sales choosed to default number")
    size_sales = default_sales


salary_summ = salary_const+(size_sales*0.1)
print("Your salary size is: ", salary_summ, "$", sep="")