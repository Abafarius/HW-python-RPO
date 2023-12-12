filename = 'input.txt'
try:
    my_file = open(filename, encoding='utf-8')
except FileNotFoundError:
    print("File not Found")
    exit()

text = my_file.read()
my_file.close()


error = "wrong e-mail!"
email_list = text.splitlines()
for user_email in email_list:
    print(user_email, end="   -   ")
    chars_ok = True
    for char in user_email:
        chars_ok &= char.isalnum()or char in ".-_@"
        # chars_ok = chars_ok and (char.isalnum()or char in ".-_@")

    email_parts = user_email.split("@")
    parts_ok = len(email_parts) == 2
    first_part = bool(email_parts[0])
    point_exists = not "." in email_parts[1]
    domain = email_parts[1].split(".")
    domain_ok = len(domain[-1]) > 1

    if chars_ok and parts_ok \
        and first_part and point_exists \
        and domain_ok:
            print("your e-mail granted!")
    else:
        print(error)
