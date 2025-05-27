scores = [50, 34, 45, 50, 25]

cart = ['banana', 33, 'juice', 2.5, ['fish', 'palm oil'], True]

print(cart[4][1])

print("we have", len(scores), "scores")

for score in scores:
	print(score)

for index in range(len(scores)):
	print(index)

for index, value in enumerate(cart):
	print(index, value)

