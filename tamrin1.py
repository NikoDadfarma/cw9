import re

"""this code check password at least 8 charachter (at least one captal)(at least one small)(at least one number)"""

user_pass = input('enter your password: ')
regex = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"

if re.match(regex, user_pass):
    print("it is right password")
else:
    print("it's not right password")
