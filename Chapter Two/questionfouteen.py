age = int(input("Enter your age: "))

heartbeat = 220
result = 220 - age

targetheartrate1 = float(input("Enter first heart rate: "))/100
targetheartrate2 = float(input("Enter second heart rate: "))/100

percentageheatrate1 = result * targetheartrate1 

percentageheatrate2 = result * targetheartrate2 

heatbeatrange = percentageheatrate1 - percentageheatrate2

print(f"Your heart rate is within the range of {percentageheatrate1}")

print(f"Your heart rate is within the range of {percentageheatrate2}")

print(f"The range of your heartbeat is: {heatbeatrange}")





  

