user_num = 0
user_input = ""
count=0
neg=0
pos=0
zero=0
even=0
odd=0
while count < 10:
  user_input = input("Enter a number: ")
  count += 1
  try:
    user_num = int(user_input)
  except ValueError: 
    print("Value Error.")
    exit()
  
  if user_num < 0: 
    neg+=1
  if user_num >= 1:
    pos+=1
  if user_num == 0:
    zero += 1
  if user_num % 2 == 0:
    even += 1
  else:
    odd += 1
print("Negatives: ",neg,"\nPositives: ",pos,"\nzeroes: ",zero, "\nevens: ",even,"\nOdds:",odd)
    
    