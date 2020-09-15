from random_password_creator import Password

pas = Password('ldus',8)
pas.set_the_charset()
pas.generate_password()
print(pas.get_password())