password = input("Enter password: ")
count = 0

for c in password:
	count+= 1

if count < 8:
	print("Password is very weak")

elif count == 8:
	print("Password is weak")

elif count >= 8 and count <= 16:
	print("Password is strong")

else: print("Pass is very strong")
