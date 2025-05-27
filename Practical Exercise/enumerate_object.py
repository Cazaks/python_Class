scores = [50, 34, 45, 50, 25]

cart = ['banana', 33, 'juice', 2.5, ['fish', 'palm oil'], True]

print(cart[0].upper())

print("we have", len(scores), "scores")

for score in scores:
	print(score)

for index in range(len(scores)):
	print(index)

for index, value in enumerate(cart):
	print(index, value)


scores.append(99)
scores.pop(1)
cart[4].insert(0, 6)
scores.extend([34, 67, 87, 65])
new_list = cart + scores
print(new_list * 3)
	



