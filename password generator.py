# import random
# import string
# password_length = 8
# password_type = input("Enter password type: \n password or pin or letters\n")
# if password_type == "password":
#     characters = string.ascii_letters + string.digits + string.punctuation
# elif password_type == "PIN":
#     characters = string.digits
# elif password_type == "letters":
#     characters = string.ascii_letters
# else:
#     print("invalid password type")
#     characters = ""
# password = ""
# for i in range(password_length):
#     password += random.choice(characters)
# print("generated password:",password)








import random
import string
password_length = 8
password_type = input("Enter password type:\n password or pin or letters\n")
if password_type == 'password':
    characters = string.ascii_letters + string.digits + string.punctuation
elif password_type == 'pin':
    characters = string.digits
elif password_type == 'letters':
    characters = string.ascii_letters
else:
    print('invalid password type')
    characters = ''
password = ''
for i in range(password_length):
    password += random.choice(characters)
print('generated password',password)