error = "wrong e-mail!"
user_email = input("Enter your e-mail: ")

# for char in user_email:
#     if not (char.isalnum()or char in ".-_@"):
#         print(error)
#         exit()

# email_parts = user_email.split("@")
# if len(email_parts)!=2:
#     print(error)
#     exit()
# if not email_parts[0]:
#     print(error)
#     exit()
# if not "." in email_parts[1]:
#     print(error)
#     exit()
# domain = email_parts[1].split(".")
# if len(domain[-1]) <= 1:
#     print(error)
#     exit()

# print("your e-mail granted!")


# for char in user_email:
#     chars_ok = char.isalnum()or char in ".-_@"

# email_parts = user_email.split("@")
# parts_ok = len(email_parts)!=2
# first_part = bool(email_parts[0])
# point_exists = not "." in email_parts[1]
# domain = email_parts[1].split(".")
# domain_ok = (domain[-1]) <= 1

# if chars_ok and parts_ok \
#     and first_part and point_exists \
#     and domain_ok:
#         print("your e-mail granted!")
# else:
#     print(error)

chars_ok = True
for char in user_email:
    chars_ok &= char.isalnum()or char in ".-_@"
    # chars_ok = chars_ok and (char.isalnum()or char in ".-_@")

email_parts = user_email.split("@")
parts_ok = len(email_parts) != 2
first_part = bool(email_parts[0])
point_exists = not "." in email_parts[1]
domain = email_parts[1].split(".")
domain_ok = (domain[-1]) <= 1

if chars_ok and parts_ok \
    and first_part and point_exists \
    and domain_ok:
        print("your e-mail granted!")
else:
    print(error)