currentpopulation = 8000500000
growthrate = 0.0085

#print(f"{Yealy:<5}{Population:<25}{Annual increase:<25}")

population = currentpopulation
for year in range(1, 101):
	increase = population * growthrate
	population = population + increase
	print(f"{year:<5}{population:<20}{increase:<20}")

	if population >= (currentpopulation * 2):
		print(f"Population doubled in year {year}")
	if population >= (currentpopulation * 4):
		print(f"Population quadripled in year {year}")