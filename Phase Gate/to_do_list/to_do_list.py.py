
	menu = """
	To-Do List Manager;
	1. Add task
	2. View task
	3. Mark task as complete
	4. Delete a task
	5. Exist
	"""
menuselect = True
while menuselect
	print(menu)
	match number
		case 0:
			menuselect = false
		case 1:
			print("Add task")
			input_choice = input("Enter the task: ")
			print("Task added")
		case 2:
			print("view tast")
			input_choice = input("Enter the task: ")
			print("Task viewed")

		case 3: 
			print("mark as complete")
			input_choice = input("Enter the task: ")
			print("Task completed")

		case 4: 
			print("Delecte task")
			input_choice = input("Enter the task: ")
			print("Task delected")

		case 5:
			print("Exit")
		case _:
			print("Invalid number")
		

	