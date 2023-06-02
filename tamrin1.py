import re
user_pass = input('enter your password: ')
regex = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
if re.match(regex, user_pass):
    print("it is right password")
else:
    print("it's not right password")
