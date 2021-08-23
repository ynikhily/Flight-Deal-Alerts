# THIS IS AN OPTIONAL FUNCTIONALITY TO SIGN UP USERS FOR THIS APPLICATION ON A SMALL SCALE
first_name = input("Welcome to Nikhil's Flight Club!!\nWe can get you best flight deals\n"
                   "What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_ver = input("Re-enter your email for verification\n")

if email == email_ver and '@' in email and '.com' in email and first_name != '' and last_name != '':
    from data_manager import DataManager
    sheety_object = DataManager()
    sheety_object.add_user(first_name, last_name, email)
    print("You are in the club. Congrats!!")