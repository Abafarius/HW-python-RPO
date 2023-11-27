print("Question 1. How many planets in our Solar system?\na)8\nb)9\nc)10")
ans1 = input("\nAnswer is (format answer 'a,b,c'):")
player = 0
addPoint = 2
if ans1 == "a":
    player = addPoint
    print("correct! You got", player, "points.")

    print("\nQuestion 2. What is the main fuel of stars?\na)He2\nb)H2\nc)C")
    ans2 = input("\nAnswer is (format answer 'a,b,c'):")


    if ans2 == "b":
        player += addPoint
        print("\ncorrect! You got", player, "points.")

        print("\nQuestion 3. According to goldilock baby universe theory what was tempereature of universe in range 10-17 million years after the Big Bang?\na)-0K\nb)1000K\nc)100 celsius")
        ans3 = input("Answer is (format answer 'a,b,c'):")


        if ans3 == "c":
            player += addPoint
            print("\nYou are cool! you got",player,"points in total!!!\n")
        else: 
            print("Answer 3 is wrong! Anyway you got",player,"points in total")


    else:
        print("Answer 2 is wrong!")

        print("\nQuestion 3. According to goldilock baby universe theory what was tempereature of universe in range 10-17 million years after the Big Bang?\na)-0K\nb)1000K\nc)100 celsius")
        ans3 = input("Answer is (format answer 'a,b,c'):")


        if ans3 == "c":
            player += addPoint
            print("\nYou are cool! you got",player,"points in total!!!\n")
        else: 
            print("Answer 3 is wrong! Anyway you got",player,"points in total")
else: 
    print("\nanswer 1 is Wrong!\n")

    print("Question 2. What is the main fuel of stars?\na)He2\nb)H2\nc)C")
    ans2 = input("\nAnswer is (format answer 'a,b,c'):")


    if ans2 == "b":
        player += addPoint
        print("\ncorrect! You got", player, "points.")

        print("\nQuestion 3. According to goldilock baby universe theory what was tempereature of universe in range 10-17 million years after the Big Bang?\na)-0K\nb)1000K\nc)100 celsius")
        ans3 = input("\nAnswer is (format answer 'a,b,c'):")


        if ans3 == "c":
            player += addPoint
            print("\nYou are cool! you got",player,"points in total!!!")
        else: 
            print("\nAnswer 3 is wrong! Anyway you got",player,"points in total")

    else:
        print("\nAnswer 2 is wrong!")
        
        print("\nQuestion 3. According to goldilock baby universe theory what was tempereature of universe in range 10-17 million years after the Big Bang?\na)-0K\nb)1000K\nc)100 celsius")
        ans3 = input("\nAnswer is (format answer 'a,b,c'):")


        if ans3 == "c":
            player += addPoint
            print("\nYou are cool! you got",player,"points in total!!!\n")
        else: 
            print("\nAnswer 3 is wrong! Anyway you got",player,"points in total")
    
# VN: здесь прям настоятельно рекомендую убрать подсчёт очков и print'ы, с этим связанные, в конец программы!