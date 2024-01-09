word = input(" Введите слово: ")

if word.endswith("ться"):
    print("Мерзавец! Ужос! Как так можно?!")
if word.startswith("шы"):
    print("Мерзавец! Ужос! Как так можно?!")
i = word.find("dog")
if i >= 0: 
    print("I found! The dog starts with %s" % i)
    print(f"I found! The dog starts with {i}")
    print( "I found! The dog starts with {position}".format(position=i) )