list_bonuses = [
    'Michael', 'Jan', 'Jim', 'Pam', 'Oscar', 'Toby', 'Michael',  'Toby', 'Kevin', 'Kelly', 'Andy', 'Angela', 'Dwight',  'Phillys', 'Creed', 'Karen', 'Andy', 'Rayan', 'Stanley']
Cheaters = []
good_employee = []
for i in list_bonuses:
    if i in good_employee:
        if i not in Cheaters:
            Cheaters.append(i)
    else:
        good_employee.append(i)
if Cheaters:

    print("Next employee got double bonuses:", end=" ")
    for i in Cheaters:
        print(i, end=", ")
else:
    print("no cheaters.")