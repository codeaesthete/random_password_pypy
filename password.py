import random
password = "ABCDEFGHIJKLMNOPQRSTUVXWXYZ1234567890abcdefghijklmnopqrstuvwxyz!~@#$%^&*()_+=-"
lentgh_password =int(input("Enter the length of the paswword: "))
a="".join(random.sample(password,lentgh_password))
print(f"Your password is : {a}")