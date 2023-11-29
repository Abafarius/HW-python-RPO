print("\nQuestion 1. How many planets in our Solar system?\na)8\nb)9\nc)10")
q1 = input("\nAnswer is (format answer 'a,b,c'):")
player = 0
addPoint = 2
ans1 = q1.upper()
if ans1 == "A":
    player += addPoint
    print("\nRight! Next question:")
else:
    print('\nWrong! Next question:')


print("\nQuestion 2. What is the main fuel of stars?\na)He2\nb)H2\nc)C")
ans2 = input("\nAnswer is (format answer 'a,b,c'):")


if ans2 == "b":
    player += addPoint
    print("\nRight! Next question:")
else:
    print('\nWrong! Next question:')

print("\nQuestion 3. According to goldilock baby universe theory what was tempereature of universe in range 10-17 million years after the Big Bang?\na)-0K\nb)+1000K\nc)+100 celsius")
ans3 = input("Answer is (format answer 'a,b,c'):")


if ans3 == "c":
    player += addPoint
    print("\nRight!\n")
else:
    print('\nWrong!\n')

print("you got",player,"points in total")


    
# VN: здесь прям настоятельно рекомендую убрать подсчёт очков и print'ы, с этим связанные, в конец программы!
# AS: вроде все исправил