numbers = int(input('Enter a five digit number: '))

num1 = (numbers // 10000) % 10
num2 = (numbers // 1000) % 10
num3 = (numbers // 100) % 10
num4 = (numbers // 10) % 10
num5 = (numbers // 1) % 10

reverse = num5, ' ', num4, ' ', num3, ' ', num2, ' ', num1

temp = num1, num2, num3, num4, num5

print(temp)
