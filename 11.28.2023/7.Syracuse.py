user_num = input("Enter natural number: ")
counter = 0


try:
    num = int(user_num)
except ValueError:
    print("Value error! Galym thinks You way bad stupid non-intellectual  simplest kind of life creature like amoeba...")
    exit()
if num <= 0:
    print("Okay. It must be positive and not zero bc it's natural. Program just shut down try once more.")
else:
    if num == 1:
        print("Sorry we are trying Syracuse theory, so... please enter another natural number, thanks!")
    else:

        while num != 1:
            counter += 1
            if num % 2 ==0:
                result = num/2
            else:
                result = ((num*3)+1)/2
            num = result
            print("Iteraion: ",counter,". Value:",  num, sep="")
#AS: Честно, эта задача намного проще чем тем с цифрами. Цифры очень сложно даются =(